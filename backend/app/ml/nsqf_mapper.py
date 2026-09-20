import csv
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional

from app.ml.eligibility_engine import (
    evaluate_eligibility
)


PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

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

        reader = csv.DictReader(
            file
        )

        for row in reader:
            qualifications.append({
                key: (
                    value.strip()
                    if isinstance(
                        value,
                        str
                    )
                    else value
                )
                for key, value
                in row.items()
            })

    return qualifications


def normalize_occupation(
    value: str
) -> str:
    return (
        str(value or "")
        .lower()
        .replace("–", "-")
        .replace("—", "-")
        .strip()
    )


def parse_iso_date(
    value: str
) -> Optional[date]:
    value = str(
        value or ""
    ).strip()

    if not value:
        return None

    try:
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()
    except ValueError:
        return None


def qualification_validity_status(
    qualification: Dict,
    as_of_date: Optional[date] = None
) -> str:
    as_of_date = (
        as_of_date
        or date.today()
    )

    valid_from = parse_iso_date(
        qualification.get(
            "valid_from",
            ""
        )
    )

    valid_till = parse_iso_date(
        qualification.get(
            "valid_till",
            ""
        )
    )

    if (
        valid_from
        and
        as_of_date < valid_from
    ):
        return "not_yet_active"

    if (
        valid_till
        and
        as_of_date > valid_till
    ):
        return "expired"

    if valid_till:
        return "active"

    return "validity_unconfirmed"


def _validity_message(
    status: str,
    qualification: Dict
) -> str:
    if status == "active":
        valid_till = (
            qualification.get(
                "valid_till",
                ""
            )
        )

        return (
            "Official NQR validity is "
            f"recorded through {valid_till}."
            if valid_till
            else
            "Official NQR entry is active."
        )

    if status == "expired":
        return (
            "The recorded NQR validity "
            "period has ended."
        )

    if status == "not_yet_active":
        return (
            "The recorded validity period "
            "has not started yet."
        )

    return (
        "The qualification is present in "
        "the official NQR source used by "
        "Jeevika, but a current validity-end "
        "date was not confirmed in this dataset."
    )


def map_nsqf_courses(
    profile: Dict,
    recommendations: List[Dict],
    include_expired: bool = False,
    as_of_date: Optional[date] = None
) -> List[Dict]:

    qualifications = (
        load_nsqf_qualifications()
    )

    mapped_results = []

    for recommendation in recommendations:

        occupation_name = (
            normalize_occupation(
                recommendation.get(
                    "occupation",
                    ""
                )
            )
        )

        all_matching_rows = [
            qualification
            for qualification
            in qualifications
            if normalize_occupation(
                qualification.get(
                    "occupation",
                    ""
                )
            )
            == occupation_name
        ]

        matching_rows = []

        for qualification in all_matching_rows:
            status = (
                qualification_validity_status(
                    qualification,
                    as_of_date=as_of_date
                )
            )

            qualification = {
                **qualification,
                "_validity_status":
                    status,
            }

            if (
                include_expired
                or
                status
                not in {
                    "expired",
                    "not_yet_active",
                }
            ):
                matching_rows.append(
                    qualification
                )

        grouped = {}

        for qualification in matching_rows:

            code = qualification.get(
                "qualification_code",
                ""
            )

            group_key = (
                code
                or qualification.get(
                    "qualification_name",
                    ""
                )
            )

            mapping_type = (
                qualification.get(
                    "mapping_type",
                    "exact"
                )
                or "exact"
            )

            group_key = (
                group_key,
                mapping_type
            )

            if group_key not in grouped:

                grouped[group_key] = {
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
                        code,

                    "duration_hours":
                        qualification.get(
                            "duration_hours",
                            ""
                        ),

                    "mapping_type":
                        mapping_type,

                    "mapping_note":
                        qualification.get(
                            "mapping_note",
                            ""
                        ),

                    "official_source_url":
                        qualification.get(
                            "official_source_url",
                            ""
                        ),

                    "valid_from":
                        qualification.get(
                            "valid_from",
                            ""
                        ),

                    "valid_till":
                        qualification.get(
                            "valid_till",
                            ""
                        ),

                    "validity_status":
                        qualification.get(
                            "_validity_status",
                            "validity_unconfirmed"
                        ),

                    "source_status":
                        qualification.get(
                            "source_status",
                            "verified_official_source"
                        ),

                    "source_verified":
                        "nqr.gov.in"
                        in qualification.get(
                            "official_source_url",
                            ""
                        ).lower(),

                    "eligibility_routes": []
                }

            eligibility = (
                evaluate_eligibility(
                    profile,
                    qualification
                )
            )

            route = {
                "minimum_education":
                    qualification.get(
                        "minimum_education",
                        ""
                    ),

                "education_status":
                    qualification.get(
                        "education_status",
                        ""
                    ),

                "experience_required":
                    qualification.get(
                        "experience_required",
                        ""
                    ),

                "training_qualification":
                    qualification.get(
                        "training_qualification",
                        ""
                    ),

                "previous_nsqf_level":
                    qualification.get(
                        "previous_nsqf_level",
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

                "training_eligible":
                    eligibility[
                        "training_eligible"
                    ],

                "previous_nsqf_eligible":
                    eligibility[
                        "previous_nsqf_eligible"
                    ],

                "verification_needed":
                    eligibility[
                        "verification_needed"
                    ],

                "eligibility_status":
                    eligibility[
                        "eligibility_status"
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

            grouped[group_key][
                "eligibility_routes"
            ].append(route)

        matching_qualifications = []

        for qualification in grouped.values():

            routes = qualification[
                "eligibility_routes"
            ]

            if any(
                route[
                    "overall_eligible"
                ]
                for route in routes
            ):
                overall_status = "eligible"
                message = (
                    "Beneficiary meets at least "
                    "one recorded eligibility route."
                )

            elif any(
                route[
                    "verification_needed"
                ]
                for route in routes
            ):
                overall_status = (
                    "needs_verification"
                )
                message = (
                    "A potentially relevant route "
                    "exists, but an additional "
                    "qualification detail is needed "
                    "before eligibility can be verified."
                )

            else:
                overall_status = (
                    "not_eligible"
                )
                message = (
                    "Beneficiary does not currently "
                    "meet any automatically verifiable "
                    "eligibility route."
                )

            qualification[
                "overall_eligible"
            ] = (
                overall_status
                == "eligible"
            )

            qualification[
                "eligibility_status"
            ] = overall_status

            qualification[
                "eligibility_message"
            ] = message

            qualification[
                "validity_message"
            ] = _validity_message(
                qualification[
                    "validity_status"
                ],
                qualification
            )

            matching_qualifications.append(
                qualification
            )

        validity_order = {
            "active": 2,
            "validity_unconfirmed": 1,
            "expired": 0,
            "not_yet_active": 0,
        }

        mapping_order = {
            "exact": 2,
            "related_pathway": 1,
        }

        matching_qualifications.sort(
            key=lambda item: (
                mapping_order.get(
                    item.get(
                        "mapping_type",
                        ""
                    ),
                    0
                ),
                validity_order.get(
                    item.get(
                        "validity_status",
                        ""
                    ),
                    0
                ),
                str(
                    item.get(
                        "nsqf_level",
                        ""
                    )
                )
            ),
            reverse=True
        )

        if matching_qualifications:
            mapping_status = "mapped"

        elif all_matching_rows:
            mapping_status = (
                "expired_or_inactive_only"
            )

        else:
            mapping_status = "not_mapped"

        enriched_recommendation = {
            **recommendation,

            "nsqf_mapping_status":
                mapping_status,

            "nsqf_qualifications":
                matching_qualifications,
        }

        mapped_results.append(
            enriched_recommendation
        )

    return mapped_results
