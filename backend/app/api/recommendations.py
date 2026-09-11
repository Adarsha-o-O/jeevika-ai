import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.beneficiary import Beneficiary
from app.ml.livelihood_mapper import map_livelihood


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.post("/{beneficiary_id}")
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

        "experience_years": 0
    }

    recommendations = map_livelihood(profile)

    return {
        "beneficiary_id": beneficiary.id,
        "beneficiary_name": beneficiary.name,
        "recommendation_count": len(recommendations),
        "recommendations": recommendations
    }