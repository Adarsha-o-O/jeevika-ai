import csv
from pathlib import Path
from typing import Dict, List


PROJECT_ROOT = Path(__file__).resolve().parents[3]

SCHEMES_FILE = (
    PROJECT_ROOT
    / "data"
    / "schemes"
    / "government_schemes.csv"
)


def load_schemes() -> List[Dict]:
    schemes = []

    with open(
        SCHEMES_FILE,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            schemes.append(row)

    return schemes


def map_schemes(
    profile: Dict,
    recommendations: List[Dict]
) -> List[Dict]:

    schemes = load_schemes()

    user_state = str(
        profile.get("state", "")
    ).lower().strip()

    enriched = []

    for recommendation in recommendations:

        occupation = str(
            recommendation.get(
                "occupation",
                ""
            )
        ).lower().strip()

        sector = str(
            recommendation.get(
                "sector",
                ""
            )
        ).lower().strip()

        matched_schemes = []

        for scheme in schemes:

            scheme_occupation = str(
                scheme.get(
                    "occupation",
                    ""
                )
            ).lower().strip()

            scheme_sector = str(
                scheme.get(
                    "sector",
                    ""
                )
            ).lower().strip()

            scheme_state = str(
                scheme.get(
                    "state",
                    ""
                )
            ).lower().strip()

            occupation_match = (
                not scheme_occupation
                or scheme_occupation in {
                    "all",
                    "any"
                }
                or scheme_occupation == occupation
            )

            sector_match = (
                not scheme_sector
                or scheme_sector in {
                    "all",
                    "any"
                }
                or scheme_sector == sector
            )

            state_match = (
                not scheme_state
                or scheme_state in {
                    "all",
                    "india",
                    "national"
                }
                or scheme_state == user_state
            )

            if (
                occupation_match
                and sector_match
                and state_match
            ):
                matched_schemes.append({
                    "scheme_name":
                        scheme.get(
                            "scheme_name",
                            ""
                        ),

                    "description":
                        scheme.get(
                            "description",
                            ""
                        ),

                    "benefit":
                        scheme.get(
                            "benefit",
                            ""
                        ),

                    "eligibility":
                        scheme.get(
                            "eligibility",
                            ""
                        ),

                    "official_url":
                        scheme.get(
                            "official_url",
                            ""
                        )
                })

        enriched.append({
            **recommendation,
            "government_schemes":
                matched_schemes
        })

    return enriched