import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.beneficiary import Beneficiary
from app.models.recommendation import Recommendation
from app.ml.livelihood_mapper import map_livelihood

from app.schemas.recommendation import (
    RecommendationResponse,
    SavedRecommendationResponse
)


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.post(
    "/{beneficiary_id}",
    response_model=RecommendationResponse
)
def generate_recommendations(
    beneficiary_id: int,
    db: Session = Depends(get_db)
):
    beneficiary = (
        db.query(Beneficiary)
        .filter(Beneficiary.id == beneficiary_id)
        .first()
    )

    if beneficiary is None:
        raise HTTPException(
            status_code=404,
            detail="Beneficiary not found"
        )

    profile = {
        "beneficiary_id": beneficiary.id,
        "name": beneficiary.name,
        "age": beneficiary.age,
        "gender": beneficiary.gender,
        "state": beneficiary.state,
        "district": beneficiary.district,
        "village": beneficiary.village,
        "education_level": beneficiary.education_level,
        "current_occupation": beneficiary.current_occupation,

        "existing_skills": json.loads(
            beneficiary.existing_skills or "[]"
        ),

        "interests": json.loads(
            beneficiary.interests or "[]"
        ),

        "preferred_language": beneficiary.preferred_language,
        "income_target": beneficiary.income_target,
        "willing_to_relocate": beneficiary.willing_to_relocate,
        "experience_years": beneficiary.experience_years or 0
}

    recommendations = map_livelihood(profile)

    response_data = {
        "beneficiary_id": beneficiary.id,
        "beneficiary_name": beneficiary.name,
        "recommendation_count": len(recommendations),
        "recommendations": recommendations
    }

    saved_recommendation = Recommendation(
        beneficiary_id=beneficiary.id,
        recommendation_data=json.dumps(
            response_data
        )
    )

    db.add(saved_recommendation)
    db.commit()
    db.refresh(saved_recommendation)

    return {
        "recommendation_id":
            saved_recommendation.id,

        **response_data
    }

@router.get(
    "/saved/{beneficiary_id}",
    response_model=SavedRecommendationResponse
)
def get_saved_recommendations(
    beneficiary_id: int,
    db: Session = Depends(get_db)
):
    records = (
        db.query(Recommendation)
        .filter(
            Recommendation.beneficiary_id == beneficiary_id
        )
        .all()
    )

    if not records:
        raise HTTPException(
            status_code=404,
            detail="No saved recommendations found"
        )

    return {
        "beneficiary_id": beneficiary_id,
        "saved_count": len(records),
        "saved_recommendations": [
            {
                "recommendation_id": record.id,
                "data": json.loads(
                    record.recommendation_data
                )
            }
            for record in records
        ]
    }