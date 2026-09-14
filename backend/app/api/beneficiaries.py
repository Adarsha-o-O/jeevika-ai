from fastapi import APIRouter, Depends, HTTPException
import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.beneficiary import Beneficiary
from app.schemas.beneficiary import BeneficiaryProfile


router = APIRouter(
    prefix="/beneficiaries",
    tags=["Beneficiaries"]
)


@router.post("/")
def create_beneficiary(
    profile: BeneficiaryProfile,
    db: Session = Depends(get_db)
):
    beneficiary = Beneficiary(
        name=profile.name,
        age=profile.age,
        gender=profile.gender,
        state=profile.state,
        district=profile.district,
        village=profile.village,
        education_level=profile.education_level,
        current_occupation=profile.current_occupation,
        existing_skills=json.dumps(profile.existing_skills),
        interests=json.dumps(profile.interests),
        preferred_language=profile.preferred_language,
        experience_years=profile.experience_years,
        income_target=profile.income_target,
        willing_to_relocate=profile.willing_to_relocate
    )

    db.add(beneficiary)
    db.commit()
    db.refresh(beneficiary)

    return {
        "message": "Beneficiary profile created successfully",
        "beneficiary_id": beneficiary.id
    }


@router.get("/{beneficiary_id}")
def get_beneficiary(
    beneficiary_id: int,
    db: Session = Depends(get_db)
):
    record = (
        db.query(Beneficiary)
        .filter(Beneficiary.id == beneficiary_id)
        .first()
    )

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Beneficiary not found"
        )

    return {
        "id": record.id,
        "name": record.name,
        "age": record.age,
        "gender": record.gender,
        "state": record.state,
        "district": record.district,
        "village": record.village,
        "education_level": record.education_level,
        "current_occupation": record.current_occupation,
        "existing_skills": json.loads(record.existing_skills or "[]"),
        "interests": json.loads(record.interests or "[]"),
        "preferred_language": record.preferred_language,
        "income_target": record.income_target,
        "willing_to_relocate": record.willing_to_relocate
    }