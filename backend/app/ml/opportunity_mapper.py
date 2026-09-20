import csv
import re
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[3]

OPPORTUNITIES_FILE = (
    PROJECT_ROOT
    / "data"
    / "opportunities"
    / "local_opportunities.csv"
)


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

SELF_EMPLOYMENT_TERMS = {
    "owner",
    "business",
    "self employed",
    "self-employed",
    "entrepreneur",
    "enterprise",
}


def normalize_text(value) -> str:
    return re.sub(
        r"\s+",
        " ",
        str(value or "").lower().strip()
    )


def parse_date(value: str) -> Optional[date]:
    value = str(value or "").strip()

    if not value:
        return None

    try:
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()
    except ValueError:
        return None


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
            opportunities.append({
                key: (
                    value.strip()
                    if isinstance(value, str)
                    else value
                )
                for key, value in row.items()
            })

    return opportunities


def _contains_any(
    text: str,
    terms
) -> bool:
    text = normalize_text(text)

    return any(
        normalize_text(term) in text
        for term in terms
    )


def _is_self_employment_path(
    recommendation: Dict
) -> bool:
    occupation = normalize_text(
        recommendation.get(
            "occupation",
            ""
        )
    )

    return _contains_any(
        occupation,
        SELF_EMPLOYMENT_TERMS
    )


def _is_apprenticeship_path(
    recommendation: Dict
) -> bool:
    if _is_self_employment_path(
        recommendation
    ):
        return False

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

    return (
        sector in APPRENTICESHIP_SECTORS
        or
        _contains_any(
            occupation,
            APPRENTICESHIP_OCCUPATION_TERMS
        )
    )


def _location_match_level(
    profile: Dict,
    opportunity: Dict
) -> str:
    user_state = normalize_text(
        profile.get("state", "")
    )

    user_district = normalize_text(
        profile.get("district", "")
    )

    item_state = normalize_text(
        opportunity.get("state", "")
    )

    item_district = normalize_text(
        opportunity.get("district", "")
    )

    if (
        item_district
        and
        user_district
        and
        item_district == user_district
        and
        (
            not item_state
            or item_state == user_state
        )
    ):
        return "district"

    if (
        item_state
        and
        item_state not in {
            "all",
            "india",
            "national",
        }
        and
        item_state == user_state
    ):
        return "state"

    if (
        not item_state
        or item_state in {
            "all",
            "india",
            "national",
        }
    ):
        return "national"

    return "none"


def _record_is_current(
    opportunity: Dict,
    as_of_date: Optional[date] = None
) -> bool:
    as_of_date = (
        as_of_date
        or date.today()
    )

    status = normalize_text(
        opportunity.get(
            "status",
            "active"
        )
    )

    if status not in {
        "",
        "active",
        "current",
        "verified",
    }:
        return False

    valid_from = parse_date(
        opportunity.get(
            "valid_from",
            ""
        )
    )

    valid_till = parse_date(
        opportunity.get(
            "valid_till",
            ""
        )
    )

    if (
        valid_from
        and
        as_of_date < valid_from
    ):
        return False

    if (
        valid_till
        and
        as_of_date > valid_till
    ):
        return False

    return True


def _listing_match(
    profile: Dict,
    recommendation: Dict,
    opportunity: Dict
) -> Tuple[int, List[str]]:
    location_level = (
        _location_match_level(
            profile,
            opportunity
        )
    )

    if location_level == "none":
        return 0, []

    item_occupation = normalize_text(
        opportunity.get(
            "occupation",
            ""
        )
    )

    item_sector = normalize_text(
        opportunity.get(
            "sector",
            ""
        )
    )

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

    occupation_match = (
        not item_occupation
        or item_occupation in {
            "all",
            "any",
        }
        or item_occupation == occupation
    )

    sector_match = (
        not item_sector
        or item_sector in {
            "all",
            "any",
        }
        or item_sector == sector
    )

    if not (
        occupation_match
        and sector_match
    ):
        return 0, []

    score = {
        "district": 95,
        "state": 80,
        "national": 60,
    }[location_level]

    reasons = [
        (
            "This verified listing matches your district."
            if location_level == "district"
            else
            (
                "This verified listing matches your state."
                if location_level == "state"
                else
                "This verified listing is available at national scope."
            )
        )
    ]

    if (
        item_occupation
        and
        item_occupation == occupation
    ):
        score += 5
        reasons.append(
            "The listing directly matches the recommended occupation."
        )

    return (
        min(score, 100),
        reasons,
    )


def _score_karnataka_skill_connect(
    profile: Dict,
    recommendation: Dict,
    opportunity: Dict
) -> Tuple[int, List[str]]:
    if normalize_text(
        profile.get("state", "")
    ) != "karnataka":
        return 0, []

    score = 82

    reasons = [
        "The beneficiary is in Karnataka and this is Karnataka Skill Development Corporation's official opportunity platform."
    ]

    if _is_apprenticeship_path(
        recommendation
    ):
        score += 6
        reasons.append(
            "The portal also supports apprenticeship and work-based opportunity discovery."
        )

    if int(
        recommendation.get(
            "skill_gap_count",
            0
        )
        or 0
    ) > 0:
        score += 4
        reasons.append(
            "The portal includes courses and employability resources in addition to jobs."
        )

    return min(score, 100), reasons


def _score_ncs(
    profile: Dict,
    recommendation: Dict,
    opportunity: Dict
) -> Tuple[int, List[str]]:
    if _is_self_employment_path(
        recommendation
    ):
        return 0, []

    score = 68

    reasons = [
        "National Career Service provides official job-search resources for jobseekers across India."
    ]

    occupation = normalize_text(
        recommendation.get(
            "occupation",
            ""
        )
    )

    if occupation:
        score += 5
        reasons.append(
            "The recommended occupation can be used as the search role/designation on NCS."
        )

    return min(score, 100), reasons


def _score_apprenticeship_india(
    profile: Dict,
    recommendation: Dict,
    opportunity: Dict
) -> Tuple[int, List[str]]:
    if not _is_apprenticeship_path(
        recommendation
    ):
        return 0, []

    score = 86

    reasons = [
        "The recommended occupation is suitable for an apprenticeship or on-the-job training pathway."
    ]

    if recommendation.get(
        "nsqf_qualifications"
    ):
        score += 6
        reasons.append(
            "A mapped skill qualification makes apprenticeship exploration especially relevant."
        )

    return min(score, 100), reasons


def _score_skill_india_digital(
    profile: Dict,
    recommendation: Dict,
    opportunity: Dict
) -> Tuple[int, List[str]]:
    skill_gap_count = int(
        recommendation.get(
            "skill_gap_count",
            0
        )
        or 0
    )

    qualifications = (
        recommendation.get(
            "nsqf_qualifications",
            []
        )
        or []
    )

    if (
        skill_gap_count <= 0
        and
        not qualifications
    ):
        return 0, []

    score = 72
    reasons = []

    if skill_gap_count > 0:
        score += min(
            9,
            skill_gap_count * 3
        )

        reasons.append(
            "The recommendation has identified skill gaps that can be used to search for relevant training."
        )

    if qualifications:
        score += 7
        reasons.append(
            "The livelihood has an NSQF-linked qualification pathway, so verified skill-course discovery is relevant."
        )

    return min(score, 100), reasons


CHANNEL_SCORERS = {
    "karnataka_skill_connect":
        _score_karnataka_skill_connect,

    "national_career_service":
        _score_ncs,

    "apprenticeship_india":
        _score_apprenticeship_india,

    "skill_india_digital":
        _score_skill_india_digital,
}


def _relevance_level(
    score: int
) -> str:
    if score >= 85:
        return "high"

    if score >= 70:
        return "relevant"

    return "possible"


def evaluate_opportunity(
    profile: Dict,
    recommendation: Dict,
    opportunity: Dict,
    as_of_date: Optional[date] = None
) -> Dict:

    if not _record_is_current(
        opportunity,
        as_of_date=as_of_date
    ):
        return {
            "show": False,
            "score": 0,
            "reasons": [],
        }

    record_kind = normalize_text(
        opportunity.get(
            "record_kind",
            "channel"
        )
    )

    if record_kind == "listing":
        score, reasons = (
            _listing_match(
                profile,
                recommendation,
                opportunity
            )
        )

    else:
        opportunity_id = normalize_text(
            opportunity.get(
                "opportunity_id",
                ""
            )
        )

        scorer = CHANNEL_SCORERS.get(
            opportunity_id
        )

        if scorer is None:
            return {
                "show": False,
                "score": 0,
                "reasons": [],
            }

        score, reasons = scorer(
            profile,
            recommendation,
            opportunity
        )

    return {
        "show": score >= 60,
        "score": score,
        "reasons": reasons,
    }


def _base_result(
    opportunity: Dict,
    profile: Dict
) -> Dict:
    return {
        "opportunity_id":
            opportunity.get(
                "opportunity_id",
                ""
            ),

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

        "record_kind":
            opportunity.get(
                "record_kind",
                "channel"
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
            ),

        "state":
            opportunity.get(
                "state",
                ""
            ),

        "district":
            opportunity.get(
                "district",
                ""
            ),

        "delivery_mode":
            opportunity.get(
                "delivery_mode",
                ""
            ),

        "official_url":
            opportunity.get(
                "official_url",
                ""
            ),

        "status":
            opportunity.get(
                "status",
                ""
            ),

        "last_verified":
            opportunity.get(
                "last_verified",
                ""
            ),

        "verification_note":
            opportunity.get(
                "verification_note",
                ""
            ),

        "location_match_level":
            _location_match_level(
                profile,
                opportunity
            ),
    }


def map_opportunities(
    profile: Dict,
    recommendations: List[Dict],
    max_opportunities: int = 3,
    as_of_date: Optional[date] = None
) -> List[Dict]:

    opportunities = load_opportunities()
    enriched = []

    for recommendation in recommendations:

        matches = []

        for opportunity in opportunities:

            evaluation = (
                evaluate_opportunity(
                    profile,
                    recommendation,
                    opportunity,
                    as_of_date=as_of_date
                )
            )

            if not evaluation[
                "show"
            ]:
                continue

            result = _base_result(
                opportunity,
                profile
            )

            result.update({
                "relevance_score":
                    evaluation[
                        "score"
                    ],

                "relevance_level":
                    _relevance_level(
                        evaluation[
                            "score"
                        ]
                    ),

                "relevance_reasons":
                    evaluation[
                        "reasons"
                    ],

                "freshness_note":
                    (
                        "This is a verified official opportunity source. "
                        "Individual openings and availability can change, "
                        "so check the official source for the latest listing."
                        if normalize_text(
                            opportunity.get(
                                "record_kind",
                                "channel"
                            )
                        )
                        == "channel"
                        else
                        "This listing was checked against the recorded validity period."
                    ),
            })

            matches.append(
                result
            )

        matches.sort(
            key=lambda item: (
                item.get(
                    "relevance_score",
                    0
                ),

                {
                    "district": 3,
                    "state": 2,
                    "national": 1,
                    "none": 0,
                }.get(
                    item.get(
                        "location_match_level",
                        "none"
                    ),
                    0
                ),

                item.get(
                    "opportunity_name",
                    ""
                ),
            ),
            reverse=True
        )

        if max_opportunities > 0:
            matches = matches[
                :max_opportunities
            ]

        enriched.append({
            **recommendation,
            "local_opportunities":
                matches,

            "opportunity_discovery_status":
                (
                    "verified_sources_available"
                    if matches
                    else
                    "no_verified_source_match"
                ),
        })

    return enriched
