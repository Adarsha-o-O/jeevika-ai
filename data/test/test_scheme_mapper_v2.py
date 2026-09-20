"""
Jeevika AI scheme relevance v2 tests.

Run from repository root:

    python -u data/test/test_scheme_mapper_v2.py
"""

import sys
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

from app.ml.scheme_mapper import (
    map_schemes,
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
        "skill_gap": (
            ["skill-a"] * skill_gap_count
        ),
        "skill_gap_count":
            skill_gap_count,
        "nsqf_qualifications":
            ([{
                "qualification_name":
                    "Test Qualification"
            }] if nsqf else []),
    }]


def scheme_ids(result):
    return [
        item["scheme_id"]
        for item in result[
            "government_schemes"
        ]
    ]


def main():
    mechanic_profile = {
        "age": 22,
        "gender": "Male",
        "state": "Karnataka",
        "district": "Shivamogga",
        "village": "Sagara",
        "education_level": "10th",
        "current_occupation":
            "Mechanic Helper",
        "existing_skills": [
            "mechanical work"
        ],
        "interests": [
            "automobiles"
        ],
        "experience_years": 2,
        "willing_to_relocate": False,
    }

    mechanic = map_schemes(
        mechanic_profile,
        recommendation(
            "Two-Wheeler Mechanic",
            "Automotive",
            skill_gap_count=3,
            nsqf=True
        )
    )[0]

    ids = scheme_ids(mechanic)

    expect(
        "naps" in ids,
        "mechanic gets apprenticeship relevance"
    )

    expect(
        "pmkvy" in ids,
        "mechanic gets skilling relevance"
    )

    expect(
        "pm_svanidhi" not in ids,
        "mechanic does not get street-vendor scheme"
    )

    expect(
        "pmegp" not in ids
        and
        "pmmy" not in ids,
        "ordinary mechanic is not automatically treated as an entrepreneur"
    )

    shop_profile = {
        "age": 29,
        "gender": "Male",
        "state": "Karnataka",
        "village": "",
        "education_level": "10th",
        "current_occupation":
            "Retail Worker",
        "interests": [
            "own business"
        ],
        "experience_years": 3,
    }

    shop = map_schemes(
        shop_profile,
        recommendation(
            "Shop Owner (Kirana Store)",
            "Retail",
            skill_gap_count=1
        )
    )[0]

    ids = scheme_ids(shop)

    expect(
        "pmmy" in ids,
        "shop-owner pathway gets MUDRA relevance"
    )

    expect(
        "pmegp" in ids,
        "shop-owner pathway gets PMEGP relevance"
    )

    expect(
        "pm_svanidhi" not in ids,
        "kirana owner is not treated as a street vendor"
    )

    street_vendor_profile = {
        "age": 31,
        "gender": "Female",
        "state": "Karnataka",
        "current_occupation":
            "Street Vendor",
        "interests": [],
        "experience_years": 4,
    }

    street = map_schemes(
        street_vendor_profile,
        recommendation(
            "Street Vendor",
            "Retail",
            skill_gap_count=0
        )
    )[0]

    ids = scheme_ids(street)

    expect(
        ids[0] == "pm_svanidhi",
        "street-vendor scheme is top-ranked for street vending"
    )

    poultry_profile = {
        "age": 26,
        "gender": "Male",
        "state": "Karnataka",
        "village": "Village A",
        "education_level": "8th",
        "current_occupation":
            "Agriculture Worker",
        "interests": [
            "poultry"
        ],
        "experience_years": 2,
    }

    poultry = map_schemes(
        poultry_profile,
        recommendation(
            "Poultry Farmer",
            "Agriculture",
            skill_gap_count=2
        )
    )[0]

    ids = scheme_ids(poultry)

    expect(
        "pmmy" in ids,
        "poultry pathway gets MUDRA allied-agriculture relevance"
    )

    young_rural = map_schemes(
        {
            "age": 24,
            "gender": "Male",
            "state": "Karnataka",
            "village": "Village A",
            "current_occupation": "",
            "interests": [],
            "experience_years": 0,
        },
        recommendation(
            "Agricultural Labourer",
            "Agriculture",
            skill_gap_count=2
        )
    )[0]

    expect(
        "ddu_gky"
        in scheme_ids(
            young_rural
        ),
        "young profile with rural location signal gets DDU-GKY verification path"
    )

    older_male = map_schemes(
        {
            "age": 40,
            "gender": "Male",
            "state": "Karnataka",
            "village": "Village A",
            "current_occupation": "",
            "interests": [],
            "experience_years": 0,
        },
        recommendation(
            "Agricultural Labourer",
            "Agriculture",
            skill_gap_count=2
        )
    )[0]

    expect(
        "ddu_gky"
        not in scheme_ids(
            older_male
        ),
        "40-year-old male is not shown DDU-GKY from age alone"
    )

    older_female = map_schemes(
        {
            "age": 40,
            "gender": "Female",
            "state": "Karnataka",
            "village": "Village A",
            "current_occupation": "",
            "interests": [],
            "experience_years": 0,
        },
        recommendation(
            "Agricultural Labourer",
            "Agriculture",
            skill_gap_count=2
        )
    )[0]

    expect(
        "ddu_gky"
        in scheme_ids(
            older_female
        ),
        "40-year-old woman gets DDU-GKY verification path under the extended age provision"
    )

    expect(
        all(
            len(item[
                "government_schemes"
            ]) <= 3
            for item in [
                mechanic,
                shop,
                street,
                poultry,
                young_rural,
                older_male,
                older_female,
            ]
        ),
        "scheme list is capped at three relevant schemes"
    )

    for result in [
        mechanic,
        shop,
        street,
        poultry,
    ]:
        for scheme in result[
            "government_schemes"
        ]:
            expect(
                "relevance_reasons"
                in scheme
                and
                "verification_points"
                in scheme
                and
                "screening_note"
                in scheme,
                f"{scheme['scheme_id']} carries explainable relevance and verification metadata"
            )

    print()
    print(
        "ALL SCHEME MAPPER V2 TESTS PASSED"
    )


if __name__ == "__main__":
    main()
