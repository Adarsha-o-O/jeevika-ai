import csv
from pathlib import Path
from typing import Dict, List


PROJECT_ROOT = Path(__file__).resolve().parents[3]

OPPORTUNITIES_FILE = (
    PROJECT_ROOT
    / "data"
    / "opportunities"
    / "local_opportunities.csv"
)


def load_opportunities() -> List[Dict]:
    opportunities = []

    with open(
        OPPORTUNITIES_FILE,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            opportunities.append(row)

    return opportunities


def map_opportunities(
    profile: Dict,
    recommendations: List[Dict]
) -> List[Dict]:

    opportunities = load_opportunities()

    user_state = str(
        profile.get("state", "")
    ).lower().strip()

    user_district = str(
        profile.get("district", "")
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

        matched_opportunities = []

        for opportunity in opportunities:

            item_occupation = str(
                opportunity.get(
                    "occupation",
                    ""
                )
            ).lower().strip()

            item_sector = str(
                opportunity.get(
                    "sector",
                    ""
                )
            ).lower().strip()

            item_state = str(
                opportunity.get(
                    "state",
                    ""
                )
            ).lower().strip()

            item_district = str(
                opportunity.get(
                    "district",
                    ""
                )
            ).lower().strip()

            occupation_match = (
                not item_occupation
                or item_occupation == occupation
            )

            sector_match = (
                not item_sector
                or item_sector == sector
            )

            state_match = (
                not item_state
                or item_state == user_state
            )

            district_match = (
                not item_district
                or item_district == user_district
            )

            if (
                occupation_match
                and sector_match
                and state_match
                and district_match
            ):
                matched_opportunities.append({
                    "opportunity_name":
                        opportunity.get(
                            "opportunity_name",
                            ""
                        ),

                    "opportunity_type":
                        opportunity.get(
                            "opportunity_type",
                            ""
                        ),

                    "provider":
                        opportunity.get(
                            "provider",
                            ""
                        ),

                    "description":
                        opportunity.get(
                            "description",
                            ""
                        )
                })

        enriched.append({
            **recommendation,
            "local_opportunities":
                matched_opportunities
        })

    return enriched