from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.beneficiaries import router as beneficiary_router
from app.api.recommendations import router as recommendations_router

from app.database.database import Base, engine

from app.models.beneficiary import Beneficiary
from app.models.recommendation import Recommendation

from app.api.assistant import router as assistant_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Jeevika AI API",
    description="AI-driven livelihood mapping and NSQF-aligned skilling recommendation platform",
    version="0.1.0"
)

ALLOWED_ORIGINS = [
    "https://jeevika-ai-sooty.vercel.app",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(beneficiary_router)
app.include_router(recommendations_router)

app.include_router(assistant_router)

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