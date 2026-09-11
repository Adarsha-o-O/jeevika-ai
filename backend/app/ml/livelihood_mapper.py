import csv
from pathlib import Path
from typing import Dict, List

from app.ml.scoring_engine import rank_occupations
from app.ml.skill_recommender import add_skill_gaps
from app.ml.nsqf_mapper import map_nsqf_courses


PROJECT_ROOT = Path(__file__).resolve().parents[3]

OCCUPATIONS_FILE = (
    PROJECT_ROOT
    / "data"
    / "occupations"
    / "occupations.csv"
)


def split_field(value: str) -> List[str]:
    if not value:
        return []

    return [
        item.strip()
        for item in value.split("|")
        if item.strip()
    ]


def load_occupations() -> List[Dict]:
    occupations = []

    with open(
        OCCUPATIONS_FILE,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            occupations.append({
                "occupation":
                    row.get(
                        "occupation",
                        ""
                    ).strip(),

                "sector":
                    row.get(
                        "sector",
                        ""
                    ).strip(),

                "minimum_education":
                    split_field(
                        row.get(
                            "minimum_education",
                            ""
                        )
                    ),

                "skills":
                    split_field(
                        row.get(
                            "skills",
                            ""
                        )
                    ),

                "interests":
                    split_field(
                        row.get(
                            "interests",
                            ""
                        )
                    )
            })

    return occupations


def map_livelihood(
    profile: Dict
) -> List[Dict]:

    occupations = load_occupations()

    ranked = rank_occupations(
        profile=profile,
        occupations=occupations,
        minimum_score=25,
        top_n=5
    )

    skill_gap_results = add_skill_gaps(
        profile=profile,
        recommendations=ranked,
        occupations=occupations
    )

    return map_nsqf_courses(
        profile=profile,
        recommendations=skill_gap_results
    )