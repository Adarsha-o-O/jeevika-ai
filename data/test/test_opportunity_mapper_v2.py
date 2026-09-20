"""
Jeevika AI opportunity intelligence v2 tests.

Run from repository root:

    python -u data/test/test_opportunity_mapper_v2.py
"""

import sys
from datetime import date
from pathlib import Path


PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parents[2]
)

sys.path.insert(
    0,
    str(
        PROJECT_ROOT
        / "backend"
    )
)

from app.ml.opportunity_mapper import (
    map_opportunities,
)


AS_OF = date(
    2026,
    9,
    20
)


def expect(
    condition,
    message
):
    if not condition:
        raise AssertionError(
            message
        )

    print(
        "PASS:",
        message
    )


def recommendation(
    occupation,
    sector,
    skill_gap_count=2,
    nsqf=False
):
    return [{
        "occupation": occupation,
        "sector": sector,
        "match_score": 60,
        "matched_skills": [],
        "matched_interests": [],
        "reasons": [],
        "recommendation_explanation": "",
        "required_skills": [],
        "skill_gap":
            ["skill"] * skill_gap_count,
        "skill_gap_count":
            skill_gap_count,
        "nsqf_qualifications":
            (
                [{
                    "qualification_name":
                        "Test Qualification"
                }]
                if nsqf
                else []
            ),
        "government_schemes": [],
    }]


def ids(result):
    return [
        item["opportunity_id"]
        for item in result[
            "local_opportunities"
        ]
    ]


def main():
    karnataka_profile = {
        "age": 22,
        "state": "Karnataka",
        "district": "Shivamogga",
        "current_occupation":
            "Mechanic Helper",
        "experience_years": 2,
    }

    mechanic = map_opportunities(
        karnataka_profile,
        recommendation(
            "Two-Wheeler Mechanic",
            "Automotive",
            skill_gap_count=3,
            nsqf=True
        ),
        as_of_date=AS_OF
    )[0]

    mechanic_ids = ids(
        mechanic
    )

    expect(
        "karnataka_skill_connect"
        in mechanic_ids,
        "Karnataka profile gets Karnataka SkillConnect"
    )

    expect(
        "apprenticeship_india"
        in mechanic_ids,
        "mechanic gets Apprenticeship India"
    )

    expect(
        len(
            mechanic[
                "local_opportunities"
            ]
        )
        <= 3,
        "opportunity results are capped at three"
    )

    expect(
        all(
            item[
                "official_url"
            ]
            for item in mechanic[
                "local_opportunities"
            ]
        ),
        "every displayed opportunity source has an official URL"
    )

    expect(
        all(
            item[
                "record_kind"
            ]
            == "channel"
            for item in mechanic[
                "local_opportunities"
            ]
        ),
        "current dataset uses verified channels rather than invented live listings"
    )

    non_karnataka = map_opportunities(
        {
            "age": 24,
            "state": "Maharashtra",
            "district": "Pune",
        },
        recommendation(
            "Data Entry Operator",
            "IT-ITeS",
            skill_gap_count=2,
            nsqf=True
        ),
        as_of_date=AS_OF
    )[0]

    expect(
        "karnataka_skill_connect"
        not in ids(
            non_karnataka
        ),
        "Karnataka SkillConnect is not shown outside Karnataka"
    )

    expect(
        "national_career_service"
        in ids(
            non_karnataka
        ),
        "national job source remains available outside Karnataka"
    )

    expect(
        "skill_india_digital"
        in ids(
            non_karnataka
        ),
        "skill-gap profile gets Skill India Digital course discovery"
    )

    owner = map_opportunities(
        {
            "age": 29,
            "state": "Karnataka",
            "district": "Shivamogga",
        },
        recommendation(
            "Shop Owner (Kirana Store)",
            "Retail",
            skill_gap_count=1,
            nsqf=False
        ),
        as_of_date=AS_OF
    )[0]

    expect(
        "national_career_service"
        not in ids(
            owner
        ),
        "self-employment pathway does not automatically get NCS job search"
    )

    expect(
        owner[
            "opportunity_discovery_status"
        ]
        == "verified_sources_available",
        "mapper exposes a clear verified-source discovery status"
    )

    print()
    print(
        "ALL OPPORTUNITY MAPPER V2 TESTS PASSED"
    )


if __name__ == "__main__":
    main()
