from pydantic import BaseModel, Field
from typing import List, Optional


class BeneficiaryProfile(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    age: int = Field(
        ...,
        ge=18,
        le=100
    )

    gender: Optional[str] = None

    state: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    district: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    village: Optional[str] = None

    education_level: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    current_occupation: Optional[str] = None

    existing_skills: List[str] = Field(
        default_factory=list
    )

    interests: List[str] = Field(
        default_factory=list
    )

    preferred_language: str = Field(
        default="English",
        min_length=2,
        max_length=50
    )

    experience_years: int = Field(
        default=0,
        ge=0,
        le=60
    )

    income_target: Optional[int] = Field(
        default=None,
        ge=0
    )

    willing_to_relocate: bool = False