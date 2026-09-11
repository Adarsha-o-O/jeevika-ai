from typing import List, Optional
from pydantic import BaseModel, Field

class EligibilityRoute(BaseModel):
    minimum_education: str
    experience_required: str

    education_eligible: bool
    experience_eligible: bool
    overall_eligible: bool
    eligibility_message: str


class NSQFQualification(BaseModel):
    qualification_name: str
    nsqf_level: str
    qualification_code: str
    duration_hours: str

    eligibility_routes: List[EligibilityRoute] = Field(
        default_factory=list
    )

    overall_eligible: bool
    eligibility_message: str


class RecommendationItem(BaseModel):
    occupation: str
    sector: str
    match_score: int

    matched_skills: List[str]
    matched_interests: List[str]
    reasons: List[str]

    recommendation_explanation: str = ""

    required_skills: List[str]
    skill_gap: List[str]
    skill_gap_count: int

    nsqf_qualifications: List[NSQFQualification]


class RecommendationResponse(BaseModel):
    recommendation_id: int
    beneficiary_id: int
    beneficiary_name: str
    recommendation_count: int
    recommendations: List[RecommendationItem]


class SavedRecommendationData(BaseModel):
    beneficiary_id: int
    beneficiary_name: str
    recommendation_count: int
    recommendations: List[RecommendationItem]


class SavedRecommendationItem(BaseModel):
    recommendation_id: int
    data: SavedRecommendationData


class SavedRecommendationResponse(BaseModel):
    beneficiary_id: int
    saved_count: int
    saved_recommendations: List[SavedRecommendationItem]