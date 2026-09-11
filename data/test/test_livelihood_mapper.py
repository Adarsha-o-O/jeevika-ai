import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT / "backend"))

from app.ml.livelihood_mapper import map_livelihood


profile = {
    "beneficiary_id": 2,
    "age": 24,
    "education_level": "10th",
    "current_occupation": "Agricultural Labourer",
    "existing_skills": [
        "farming",
        "driving"
    ],
    "interests": [
        "mechanical work",
        "automobiles"
    ],
    "state": "Karnataka",
    "district": "Shivamogga",
    "preferred_language": "Kannada",
    "income_target": 18000,
    "willing_to_relocate": False
}

results = map_livelihood(profile)

for result in results:
    print(result)