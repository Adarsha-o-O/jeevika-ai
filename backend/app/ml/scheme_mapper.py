import csv
import re
from pathlib import Path
from typing import Dict, List, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[3]

SCHEMES_FILE = (
    PROJECT_ROOT
    / "data"
    / "schemes"
    / "government_schemes.csv"
)


# Technical/service roles where apprenticeship is a realistic pathway.
APPRENTICESHIP_SECTORS = {
    "automotive",
    "capital goods & manufacturing",
    "construction",
    "electrical",
    "electronics",
    "healthcare support",
    "it-ites",
    "logistics",
    "retail",
    "apparel & textiles",
    "beauty & wellness",
}

APPRENTICESHIP_OCCUPATION_TERMS = {
    "mechanic",
    "technician",
    "electrician",
    "wireman",
    "welder",
    "operator",
    "assistant",
    "associate",
    "fitter",
    "machinist",
    "plumber",
    "carpenter",
    "mason",
    "tailor",
    "stylist",
    "therapist",
    "repair",
}

ENTREPRENEURSHIP_TERMS = {
    "owner",
    "business",
    "shop",
    "self employed",
    "self-employed",
    "entrepreneur",
    "enterprise",
    "service owner",
    "parlour owner",
    "store owner",
    "taxi service",
}

BUSINESS_INTEREST_TERMS = {
    "business",
    "self employment",
    "self-employment",
    "entrepreneurship",
    "start a business",
    "own business",
    "shop",
    "enterprise",
}

ALLIED_AGRICULTURE_TERMS = {
    "poultry",
    "dairy",
    "beekeeping",
    "apiculture",
}

STREET_VENDOR_TERMS = {
    "street vendor",
    "street vending",
    "hawker",
    "pushcart",
    "push cart",
    "food cart",
    "cart vendor",
    "roadside vendor",
    "stall vendor",
}


def normalize_text(value) -> str:
    return re.sub(
        r"\s+",
        " ",
        str(value or "").lower().strip()
    )


def split_terms(value) -> List[str]:
    if isinstance(value, (list, tuple, set)):
        raw_values = value
    else:
        raw_values = re.split(
            r"[,|;\n]+",
            str(value or "")
        )

    return [
        normalize_text(item)
        for item in raw_values
        if normalize_text(item)
    ]


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
            schemes.append({
                key: (
                    value.strip()
                    if isinstance(value, str)
                    else value
                )
                for key, value in row.items()
            })

    return schemes


def _profile_age(profile: Dict) -> int:
    try:
        return int(float(profile.get("age", 0)))
    except (TypeError, ValueError):
        return 0


def _experience_years(profile: Dict) -> float:
    try:
        return max(
            0.0,
            float(profile.get("experience_years", 0))
        )
    except (TypeError, ValueError):
        return 0.0


def _profile_gender(profile: Dict) -> str:
    return normalize_text(
        profile.get("gender", "")
    )


def _combined_profile_text(profile: Dict) -> str:
    values = [
        profile.get("current_occupation", ""),
        profile.get("village", ""),
        profile.get("district", ""),
        profile.get("state", ""),
    ]

    values.extend(
        profile.get("existing_skills", [])
        if isinstance(
            profile.get("existing_skills", []),
            list
        )
        else []
    )

    values.extend(
        profile.get("interests", [])
        if isinstance(
            profile.get("interests", []),
            list
        )
        else split_terms(
            profile.get("interests", "")
        )
    )

    return " ".join(
        normalize_text(value)
        for value in values
        if normalize_text(value)
    )


def _contains_any(
    text: str,
    terms
) -> bool:
    text = normalize_text(text)

    return any(
        normalize_text(term) in text
        for term in terms
    )


def _is_entrepreneurial_path(
    profile: Dict,
    recommendation: Dict
) -> bool:
    occupation = normalize_text(
        recommendation.get("occupation", "")
    )

    if _contains_any(
        occupation,
        ENTREPRENEURSHIP_TERMS
    ):
        return True

    interests = " ".join(
        split_terms(
            profile.get("interests", [])
        )
    )

    current_occupation = normalize_text(
        profile.get("current_occupation", "")
    )

    return (
        _contains_any(
            interests,
            BUSINESS_INTEREST_TERMS
        )
        or
        _contains_any(
            current_occupation,
            ENTREPRENEURSHIP_TERMS
        )
    )


def _is_allied_agriculture_path(
    profile: Dict,
    recommendation: Dict
) -> bool:
    text = " ".join([
        normalize_text(
            recommendation.get(
                "occupation",
                ""
            )
        ),
        normalize_text(
            recommendation.get(
                "sector",
                ""
            )
        ),
        _combined_profile_text(
            profile
        ),
    ])

    return _contains_any(
        text,
        ALLIED_AGRICULTURE_TERMS
    )


def _is_street_vendor_path(
    profile: Dict,
    recommendation: Dict
) -> bool:
    text = " ".join([
        normalize_text(
            recommendation.get(
                "occupation",
                ""
            )
        ),
        normalize_text(
            profile.get(
                "current_occupation",
                ""
            )
        ),
    ])

    return _contains_any(
        text,
        STREET_VENDOR_TERMS
    )


def _is_apprenticeship_path(
    recommendation: Dict
) -> bool:
    occupation = normalize_text(
        recommendation.get(
            "occupation",
            ""
        )
    )

    sector = normalize_text(
        recommendation.get(
            "sector",
            ""
        )
    )

    if _contains_any(
        occupation,
        ENTREPRENEURSHIP_TERMS
    ):
        return False

    return (
        sector in APPRENTICESHIP_SECTORS
        or
        _contains_any(
            occupation,
            APPRENTICESHIP_OCCUPATION_TERMS
        )
    )


def _state_match(
    profile: Dict,
    scheme: Dict
) -> bool:
    user_state = normalize_text(
        profile.get("state", "")
    )

    scheme_state = normalize_text(
        scheme.get("state", "")
    )

    return (
        not scheme_state
        or scheme_state in {
            "all",
            "india",
            "national",
        }
        or scheme_state == user_state
    )


def _active_scheme(
    scheme: Dict
) -> bool:
    status = normalize_text(
        scheme.get("status", "active")
    )

    return status in {
        "",
        "active",
        "current",
    }


def _base_result(
    scheme: Dict
) -> Dict:
    return {
        "scheme_id":
            scheme.get("scheme_id", ""),

        "scheme_name":
            scheme.get("scheme_name", ""),

        "scheme_type":
            scheme.get("scheme_type", ""),

        "description":
            scheme.get("description", ""),

        "benefit":
            scheme.get("benefit", ""),

        "eligibility":
            scheme.get("eligibility", ""),

        "application_mode":
            scheme.get("application_mode", ""),

        "official_url":
            scheme.get("official_url", ""),

        "status":
            scheme.get("status", ""),

        "last_verified":
            scheme.get("last_verified", ""),

        "verification_note":
            scheme.get(
                "verification_note",
                ""
            ),
    }


def _relevance_level(
    score: int
) -> str:
    if score >= 80:
        return "high"

    if score >= 60:
        return "relevant"

    return "possible"


def _score_pmkvy(
    profile: Dict,
    recommendation: Dict
) -> Tuple[int, List[str], List[str]]:
    score = 25
    reasons = []
    verify = [
        "Aadhaar/identity and job-role eligibility",
        "availability of the relevant approved training pathway",
    ]

    age = _profile_age(profile)
    experience = _experience_years(profile)
    skill_gap_count = int(
        recommendation.get(
            "skill_gap_count",
            0
        )
        or 0
    )

    qualifications = recommendation.get(
        "nsqf_qualifications",
        []
    ) or []

    if skill_gap_count > 0:
        score += 30
        reasons.append(
            "The recommended livelihood has identified skill gaps that may benefit from formal skilling."
        )

    if qualifications:
        score += 15
        reasons.append(
            "Jeevika has an NSQF pathway mapped for this livelihood."
        )

    if 15 <= age <= 45:
        score += 15
        reasons.append(
            "The beneficiary is within the PMKVY 4.0 Short-Term Training age range."
        )

    elif (
        18 <= age <= 59
        and experience > 0
    ):
        score += 12
        reasons.append(
            "Prior work experience may make Recognition of Prior Learning worth checking."
        )
        verify.append(
            "whether the prior experience satisfies the selected RPL job role"
        )

    elif age:
        score -= 25

    return (
        max(0, min(100, score)),
        reasons,
        verify,
    )


def _score_naps(
    profile: Dict,
    recommendation: Dict
) -> Tuple[int, List[str], List[str]]:
    age = _profile_age(profile)

    if not _is_apprenticeship_path(
        recommendation
    ):
        return 0, [], []

    score = 45
    reasons = [
        "The recommended occupation is suitable for an apprenticeship or on-the-job training pathway."
    ]

    verify = [
        "trade-specific education and physical requirements",
        "availability of a registered establishment and apprenticeship contract",
    ]

    if age >= 14:
        score += 15
        reasons.append(
            "The beneficiary meets the general minimum apprenticeship age threshold."
        )

    if recommendation.get(
        "nsqf_qualifications"
    ):
        score += 10
        reasons.append(
            "A mapped skill qualification makes structured work-based training especially relevant."
        )

    if int(
        recommendation.get(
            "skill_gap_count",
            0
        )
        or 0
    ) > 0:
        score += 10

    return (
        min(100, score),
        reasons,
        verify,
    )


def _score_pmegp(
    profile: Dict,
    recommendation: Dict
) -> Tuple[int, List[str], List[str]]:
    if not _is_entrepreneurial_path(
        profile,
        recommendation
    ):
        return 0, [], []

    age = _profile_age(profile)

    if age and age < 18:
        return 0, [], []

    score = 70
    reasons = [
        "The livelihood or beneficiary preference points toward self-employment or starting a micro-enterprise."
    ]

    verify = [
        "whether this is a new eligible enterprise/project",
        "project activity and project-cost rules",
        "previous government-subsidy assistance",
        "education requirement where the project-cost threshold makes it applicable",
    ]

    if age >= 18:
        score += 10
        reasons.append(
            "The beneficiary meets the basic PMEGP adult-age condition."
        )

    return (
        min(100, score),
        reasons,
        verify,
    )


def _score_ddugky(
    profile: Dict,
    recommendation: Dict
) -> Tuple[int, List[str], List[str]]:
    age = _profile_age(profile)
    gender = _profile_gender(profile)

    age_fit = (
        15 <= age <= 35
        or (
            gender == "female"
            and
            15 <= age <= 45
        )
    )

    if not age_fit:
        return 0, [], []

    score = 45
    reasons = [
        "The beneficiary falls within an age band that can be relevant for DDU-GKY."
    ]

    village = normalize_text(
        profile.get("village", "")
    )

    if village:
        score += 10
        reasons.append(
            "A village/town location is recorded, so rural-programme relevance is worth verifying."
        )

    if profile.get(
        "willing_to_relocate",
        False
    ):
        score += 5

    verify = [
        "rural residence",
        "poor-household / programme target-group criteria",
        "other DDU-GKY admission conditions",
    ]

    return (
        min(100, score),
        reasons,
        verify,
    )


def _score_pmsvanidhi(
    profile: Dict,
    recommendation: Dict
) -> Tuple[int, List[str], List[str]]:
    if not _is_street_vendor_path(
        profile,
        recommendation
    ):
        return 0, [], []

    return (
        95,
        [
            "The occupation/current work explicitly matches a street-vending livelihood."
        ],
        [
            "street-vendor identification and local-body / scheme documentation requirements",
        ],
    )


def _score_pmmy(
    profile: Dict,
    recommendation: Dict
) -> Tuple[int, List[str], List[str]]:
    entrepreneurial = (
        _is_entrepreneurial_path(
            profile,
            recommendation
        )
    )

    allied_agriculture = (
        _is_allied_agriculture_path(
            profile,
            recommendation
        )
    )

    if (
        not entrepreneurial
        and
        not allied_agriculture
    ):
        return 0, [], []

    score = 65
    reasons = []

    if entrepreneurial:
        score += 15
        reasons.append(
            "The livelihood or beneficiary preference points toward a micro-enterprise/self-employment pathway."
        )

    if allied_agriculture:
        score += 15
        reasons.append(
            "The livelihood is an allied-agriculture activity such as poultry, dairy or beekeeping, which falls within PMMY's stated activity scope."
        )

    verify = [
        "enterprise and loan-purpose details",
        "lender appraisal and applicable PMMY category",
    ]

    return (
        min(100, score),
        reasons,
        verify,
    )


SCORERS = {
    "pmkvy": _score_pmkvy,
    "naps": _score_naps,
    "pmegp": _score_pmegp,
    "ddu_gky": _score_ddugky,
    "pm_svanidhi": _score_pmsvanidhi,
    "pmmy": _score_pmmy,
}


def evaluate_scheme_relevance(
    profile: Dict,
    recommendation: Dict,
    scheme: Dict
) -> Dict:
    scheme_id = normalize_text(
        scheme.get(
            "scheme_id",
            ""
        )
    )

    scorer = SCORERS.get(
        scheme_id
    )

    if scorer is None:
        return {
            "show": False,
            "relevance_score": 0,
            "relevance_level": "possible",
            "relevance_reasons": [],
            "verification_points": [],
        }

    score, reasons, verify = scorer(
        profile,
        recommendation
    )

    return {
        "show": score >= 45,
        "relevance_score": score,
        "relevance_level":
            _relevance_level(score),

        "relevance_reasons":
            reasons,

        "verification_points":
            verify,
    }


def map_schemes(
    profile: Dict,
    recommendations: List[Dict],
    max_schemes: int = 3
) -> List[Dict]:

    schemes = load_schemes()
    enriched = []

    for recommendation in recommendations:

        matched_schemes = []

        for scheme in schemes:

            if not _active_scheme(
                scheme
            ):
                continue

            if not _state_match(
                profile,
                scheme
            ):
                continue

            screening = (
                evaluate_scheme_relevance(
                    profile,
                    recommendation,
                    scheme
                )
            )

            if not screening[
                "show"
            ]:
                continue

            result = _base_result(
                scheme
            )

            result.update({
                "relevance_score":
                    screening[
                        "relevance_score"
                    ],

                "relevance_level":
                    screening[
                        "relevance_level"
                    ],

                "relevance_reasons":
                    screening[
                        "relevance_reasons"
                    ],

                "verification_required":
                    True,

                "verification_points":
                    screening[
                        "verification_points"
                    ],

                "screening_note":
                    (
                        "Jeevika has screened this scheme "
                        "for relevance only. Official "
                        "eligibility must be verified "
                        "with the scheme authority."
                    ),
            })

            matched_schemes.append(
                result
            )

        matched_schemes.sort(
            key=lambda item: (
                item.get(
                    "relevance_score",
                    0
                ),
                item.get(
                    "scheme_name",
                    ""
                ),
            ),
            reverse=True
        )

        if max_schemes > 0:
            matched_schemes = (
                matched_schemes[
                    :max_schemes
                ]
            )

        enriched.append({
            **recommendation,
            "government_schemes":
                matched_schemes,
        })

    return enriched
