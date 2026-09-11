
from typing import Dict, List

from app.ml.scoring_engine import rank_occupations
from app.ml.skill_recommender import add_skill_gaps
from app.ml.nsqf_mapper import map_nsqf_courses


OCCUPATIONS = [
    {
        "occupation": "Automotive Service Technician",
        "sector": "Automotive",
        "minimum_education": ["10th", "12th", "Diploma"],
        "skills": ["driving", "mechanical work", "tools"],
        "interests": ["automobiles", "mechanical work"]
    },
    {
        "occupation": "Tractor Mechanic",
        "sector": "Agriculture",
        "minimum_education": ["8th", "10th", "12th"],
        "skills": ["farming", "mechanical work", "tools"],
        "interests": ["agriculture", "mechanical work"]
    },
    {
        "occupation": "Electrician",
        "sector": "Electrical",
        "minimum_education": ["10th", "12th", "ITI"],
        "skills": ["electrical work", "tools"],
        "interests": ["electrical", "technical work"]
    },
    {
        "occupation": "Tailor",
        "sector": "Apparel",
        "minimum_education": ["5th", "8th", "10th", "12th"],
        "skills": ["stitching", "sewing"],
        "interests": ["fashion", "clothing", "design"]
    },
    {
        "occupation": "Data Entry Operator",
        "sector": "IT-ITES",
        "minimum_education": ["10th", "12th", "Diploma"],
        "skills": ["typing", "computer basics"],
        "interests": ["computers", "office work"]
    }
]


def map_livelihood(profile: Dict) -> List[Dict]:

    ranked = rank_occupations(
        profile=profile,
        occupations=OCCUPATIONS,
        minimum_score=25,
        top_n=5
    )

    skill_gap_results = add_skill_gaps(
        profile=profile,
        recommendations=ranked,
        occupations=OCCUPATIONS
    )

    return map_nsqf_courses(
        profile=profile,
        recommendations=skill_gap_results
    )