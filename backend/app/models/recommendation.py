from sqlalchemy import Column, Integer, Text, ForeignKey
from app.database.database import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    beneficiary_id = Column(
        Integer,
        ForeignKey("beneficiaries.id"),
        nullable=False,
        index=True
    )

    recommendation_data = Column(
        Text,
        nullable=False
    )