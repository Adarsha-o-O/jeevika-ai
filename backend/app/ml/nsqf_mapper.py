import csv
from pathlib import Path
from typing import Dict, List

from app.ml.eligibility_engine import evaluate_eligibility


PROJECT_ROOT = Path(__file__).resolve().parents[3]

NSQF_FILE = (
    PROJECT_ROOT
    / "data"
    / "nsqf"
    / "nsqf_qualifications.csv"
)


def load_nsqf_qualifications() -> List[Dict]:
    qualifications = []

    with open(
        NSQF_FILE,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            qualifications.append(row)

    return qualifications


def map_nsqf_courses(
    profile: Dict,
    recommendations: List[Dict]
) -> List[Dict]:

    qualifications = load_nsqf_qualifications()

    mapped_results = []

    for recommendation in recommendations:

        occupation_name = (
            recommendation
            .get("occupation", "")
            .lower()
            .strip()
        )

        matching_qualifications = []

        for qualification in qualifications:

            nsqf_occupation = (
                qualification
                .get("occupation", "")
                .lower()
                .strip()
            )

            if occupation_name == nsqf_occupation:

                eligibility = evaluate_eligibility(
                    profile,
                    qualification
                )

                qualification_result = {
                    "qualification_name":
                        qualification.get(
                            "qualification_name",
                            ""
                        ),

                    "nsqf_level":
                        qualification.get(
                            "nsqf_level",
                            ""
                        ),

                    "qualification_code":
                        qualification.get(
                            "qualification_code",
                            ""
                        ),

                    "minimum_education":
                        qualification.get(
                            "minimum_education",
                            ""
                        ),

                    "experience_required":
                        qualification.get(
                            "experience_required",
                            ""
                        ),

                    "duration_hours":
                        qualification.get(
                            "duration_hours",
                            ""
                        ),

                    "education_eligible":
                        eligibility[
                            "education_eligible"
                        ],

                    "experience_eligible":
                        eligibility[
                            "experience_eligible"
                        ],

                    "overall_eligible":
                        eligibility[
                            "overall_eligible"
                        ],

                    "eligibility_message":
                        eligibility[
                            "eligibility_message"
                        ]
                }

                matching_qualifications.append(
                    qualification_result
                )

        enriched_recommendation = {
            **recommendation,
            "nsqf_qualifications":
                matching_qualifications
        }

        mapped_results.append(
            enriched_recommendation
        )

    return mapped_results