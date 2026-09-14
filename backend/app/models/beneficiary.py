from sqlalchemy import Column, Integer, String, Boolean, Text
from app.database.database import Base


class Beneficiary(Base):
    __tablename__ = "beneficiaries"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=True)

    state = Column(String, nullable=False)
    district = Column(String, nullable=False)
    village = Column(String, nullable=True)

    education_level = Column(String, nullable=False)
    current_occupation = Column(String, nullable=True)

    existing_skills = Column(Text, nullable=True)
    interests = Column(Text, nullable=True)

    preferred_language = Column(String, default="English")

    experience_years = Column(Integer, default=0)

    income_target = Column(Integer, nullable=True)
    willing_to_relocate = Column(Boolean, default=False)