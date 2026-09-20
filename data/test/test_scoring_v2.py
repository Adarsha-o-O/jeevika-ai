"""
Quick smoke test for Jeevika AI scoring v2.

Run from repository root:

    python -u data/test/test_scoring_v2.py
"""

import csv
import sys
from pathlib import Path


PROJECT_ROOT = Path(
    __file__
).resolve().parents[2]

BACKEND_DIR = (
    PROJECT_ROOT
    / "backend"
)

sys.path.insert(
    0,
    str(BACKEND_DIR)
)

from app.ml.scoring_engine import rank_occupations


OCCUPATIONS_FILE = (
    PROJECT_ROOT
    / "data"
    / "occupations"
    / "occupations.csv"
)


def split_field(value):
    return [
        item.strip()
        for item in str(
            value or ""
        ).split("|")
        if item.strip()
    ]


def load_occupations():
    occupations = []

    with open(
        OCCUPATIONS_FILE,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(
            file
        )

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


def main():

    profile = {
        "education_level":
            "10th",

        "current_occupation":
            "Two-Wheeler Mechanic",

        "existing_skills": [
            "vehicle repair"
        ],

        "interests": [
            "automobile servicing"
        ],

        "experience_years":
            6
    }

    recommendations = rank_occupations(
        profile=profile,
        occupations=load_occupations(),
        minimum_score=25,
        top_n=5
    )

    print(
        "\nJeevika AI scoring v2 "
        "smoke test\n"
    )

    for index, item in enumerate(
        recommendations,
        start=1
    ):
        print(
            f"{index}. "
            f"{item['occupation']} "
            f"- "
            f"{item['match_score']}%"
        )

        print(
            "   Skills:",
            item[
                "matched_skills"
            ]
        )

        print(
            "   Interests:",
            item[
                "matched_interests"
            ]
        )

        print(
            "   Reasons:",
            item[
                "reasons"
            ]
        )

        print()


if __name__ == "__main__":
    main()
