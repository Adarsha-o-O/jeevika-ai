import json

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.beneficiary import Beneficiary
from app.ml.livelihood_mapper import map_livelihood


router = APIRouter(
    prefix="/assistant",
    tags=["Voice Assistant"]
)


class AssistantQuery(BaseModel):
    query: str
    language: str = "English"


def build_profile(
    beneficiary: Beneficiary
):
    return {
        "beneficiary_id":
            beneficiary.id,

        "name":
            beneficiary.name,

        "age":
            beneficiary.age,

        "gender":
            beneficiary.gender,

        "state":
            beneficiary.state,

        "district":
            beneficiary.district,

        "village":
            beneficiary.village,

        "education_level":
            beneficiary.education_level,

        "current_occupation":
            beneficiary.current_occupation,

        "existing_skills":
            json.loads(
                beneficiary.existing_skills
                or "[]"
            ),

        "interests":
            json.loads(
                beneficiary.interests
                or "[]"
            ),

        "preferred_language":
            beneficiary.preferred_language,

        "experience_years":
            beneficiary.experience_years
            or 0,

        "income_target":
            beneficiary.income_target,

        "willing_to_relocate":
            beneficiary.willing_to_relocate
    }


def build_response(
    recommendations,
    language
):
    if not recommendations:
        if language.lower() == "kannada":
            return (
                "ನಿಮ್ಮ ಪ್ರೊಫೈಲ್‌ಗೆ ಈಗ ಸೂಕ್ತವಾದ "
                "ಉದ್ಯೋಗ ಶಿಫಾರಸು ಸಿಗಲಿಲ್ಲ."
            )

        if language.lower() == "hindi":
            return (
                "आपकी प्रोफ़ाइल के लिए अभी कोई "
                "उपयुक्त रोजगार सुझाव नहीं मिला।"
            )

        return (
            "I could not find a suitable livelihood "
            "recommendation for your profile."
        )

    top = recommendations[0]

    occupation = top.get(
        "occupation",
        ""
    )

    score = top.get(
        "match_score",
        0
    )

    gaps = top.get(
        "skill_gap",
        []
    )

    gap_text = (
        ", ".join(gaps)
        if gaps
        else "none"
    )

    language = language.lower()

    if language == "kannada":
        return (
            f"ನಿಮಗೆ ಸೂಕ್ತವಾದ ಪ್ರಮುಖ ಉದ್ಯೋಗ "
            f"{occupation}. "
            f"ಹೊಂದಾಣಿಕೆ ಅಂಕ {score} ಶೇಕಡಾ. "
            f"ಅಭಿವೃದ್ಧಿಪಡಿಸಬೇಕಾದ ಕೌಶಲ್ಯಗಳು: "
            f"{gap_text}."
        )

    if language == "hindi":
        return (
            f"आपके लिए सबसे उपयुक्त रोजगार "
            f"{occupation} है। "
            f"मैच स्कोर {score} प्रतिशत है। "
            f"आपको इन कौशलों पर काम करना चाहिए: "
            f"{gap_text}."
        )

    return (
        f"Your strongest livelihood recommendation "
        f"is {occupation}. "
        f"Your profile match is {score}%. "
        f"Skills to improve: {gap_text}."
    )


@router.post(
    "/query/{beneficiary_id}"
)
def assistant_query(
    beneficiary_id: int,
    request: AssistantQuery,
    db: Session = Depends(get_db)
):

    beneficiary = (
        db.query(Beneficiary)
        .filter(
            Beneficiary.id
            == beneficiary_id
        )
        .first()
    )

    if beneficiary is None:
        raise HTTPException(
            status_code=404,
            detail="Beneficiary not found"
        )

    profile = build_profile(
        beneficiary
    )

    recommendations = (
        map_livelihood(profile)
    )

    assistant_response = (
        build_response(
            recommendations,
            request.language
        )
    )

    return {
        "beneficiary_id":
            beneficiary.id,

        "language":
            request.language,

        "user_query":
            request.query,

        "assistant_response":
            assistant_response,

        "top_recommendations":
            recommendations[:3]
    }