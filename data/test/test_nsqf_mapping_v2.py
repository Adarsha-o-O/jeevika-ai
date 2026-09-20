"""
Jeevika AI NSQF mapping v2 smoke/regression tests.

Run from repository root:

    python -u data/test/test_nsqf_mapping_v2.py
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

from app.ml.eligibility_engine import (
    required_experience_years,
    evaluate_eligibility,
)
from app.ml.nsqf_mapper import (
    map_nsqf_courses,
)


AS_OF = date(
    2026,
    9,
    20
)


def recommendation(
    occupation
):
    return [{
        "occupation": occupation,
        "sector": "Test",
        "match_score": 50,
        "matched_skills": [],
        "matched_interests": [],
        "reasons": [],
        "recommendation_explanation": "",
    }]


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


def main():
    expect(
        abs(
            required_experience_years({
                "experience_required":
                    "6 months"
            })
            - 0.5
        )
        < 0.0001,
        "6 months is parsed as 0.5 years"
    )

    route = {
        "minimum_education":
            "10th",

        "experience_required":
            "No Experience",

        "training_qualification":
            "NTC/NAC",
    }

    normal_profile = {
        "education_level":
            "10th",

        "experience_years":
            1,
    }

    status = evaluate_eligibility(
        normal_profile,
        route
    )

    expect(
        status[
            "eligibility_status"
        ]
        == "needs_verification",
        "missing NTC/NAC detail is not guessed"
    )

    four_wheeler_profile = {
        "education_level":
            "10th",

        "experience_years":
            2,

        "current_occupation":
            "Four-Wheeler Mechanic",
    }

    mapped = map_nsqf_courses(
        four_wheeler_profile,
        recommendation(
            "Four-Wheeler Mechanic (Light Motor Vehicle)"
        ),
        as_of_date=AS_OF
    )[0]

    names = [
        item[
            "qualification_name"
        ]
        for item in mapped[
            "nsqf_qualifications"
        ]
    ]

    expect(
        "Four Wheeler Service Technician"
        in names,
        "current four-wheeler qualification maps"
    )

    expect(
        "Electric Vehicle Service Technician"
        in names,
        "related EV pathway maps separately"
    )

    exact = next(
        item
        for item
        in mapped[
            "nsqf_qualifications"
        ]
        if item[
            "qualification_name"
        ]
        == "Four Wheeler Service Technician"
    )

    expect(
        exact[
            "mapping_type"
        ]
        == "exact",
        "exact and related pathways are distinguished"
    )

    expect(
        exact[
            "overall_eligible"
        ]
        is True,
        "10th + 2 years satisfies recorded four-wheeler route"
    )

    two_wheeler = map_nsqf_courses(
        {
            "education_level":
                "10th",

            "experience_years":
                2,
        },
        recommendation(
            "Two-Wheeler Mechanic"
        ),
        as_of_date=AS_OF
    )[0]

    two_names = [
        item[
            "qualification_name"
        ]
        for item in two_wheeler[
            "nsqf_qualifications"
        ]
    ]

    expect(
        "Two Wheeler Service Technician"
        not in two_names,
        "expired conventional two-wheeler qualification is filtered"
    )

    expect(
        "Electric Vehicle Service Technician"
        in two_names,
        "current related EV pathway remains available"
    )

    tailor = map_nsqf_courses(
        {
            "education_level":
                "8th",

            "experience_years":
                1,
        },
        recommendation(
            "Tailor (Apparel Making)"
        ),
        as_of_date=AS_OF
    )[0]

    expect(
        tailor[
            "nsqf_qualifications"
        ][0][
            "overall_eligible"
        ]
        is True,
        "8th + 1 year satisfies current tailor route"
    )

    electrician = map_nsqf_courses(
        {
            "education_level":
                "10th",

            "experience_years":
                0,
        },
        recommendation(
            "Electrician (Domestic)"
        ),
        as_of_date=AS_OF
    )[0]

    expect(
        electrician[
            "nsqf_qualifications"
        ][0][
            "qualification_name"
        ]
        == "Assistant Electrician (Domestic cum Industrial)",
        "electrician receives clearly labelled related pathway"
    )

    office = map_nsqf_courses(
        {
            "education_level":
                "10th",

            "experience_years":
                0,
        },
        recommendation(
            "Office Assistant"
        ),
        as_of_date=AS_OF
    )[0]

    expect(
        office[
            "nsqf_qualifications"
        ]
        == [],
        "expired office-assistant qualification is not shown"
    )

    expect(
        office[
            "nsqf_mapping_status"
        ]
        == "expired_or_inactive_only",
        "expired-only state is explicitly available to the UI"
    )

    print()
    print(
        "ALL NSQF V2 TESTS PASSED"
    )


if __name__ == "__main__":
    main()
