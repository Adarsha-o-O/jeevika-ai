from fastapi import FastAPI

from app.api.beneficiaries import router as beneficiary_router
from app.api.recommendations import router as recommendations_router

from app.database.database import Base, engine

from app.models.beneficiary import Beneficiary
from app.models.recommendation import Recommendation


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Jeevika AI API",
    description="AI-driven livelihood mapping and NSQF-aligned skilling recommendation platform",
    version="0.1.0"
)

app.include_router(beneficiary_router)
app.include_router(recommendations_router)


@app.get("/")
def root():
    return {
        "message": "Jeevika AI backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }