from difflib import SequenceMatcher
import re
from typing import Dict, List, Set, Tuple

from app.ml.text_matcher import (
    normalize_skill,
    normalize_interest,
    find_matches,
    normalize_text,
)


# ---------------------------------------------------------------------
# Jeevika AI Recommendation Scoring v2
#
# Total profile-fit score = 100
#   Education compatibility      15
#   Required skill coverage      35
#   Interest alignment           15
#   Current occupation relevance 25
#   Related experience           10
#
# NSQF availability is intentionally NOT part of the profile-fit score.
# A livelihood should not rank higher merely because Jeevika currently
# has more training-pathway data for it.
# ---------------------------------------------------------------------

EDUCATION_WEIGHT = 15
SKILL_WEIGHT = 35
INTEREST_WEIGHT = 15
OCCUPATION_WEIGHT = 25
EXPERIENCE_WEIGHT = 10


EDUCATION_ALIASES = {
    "primary": "5th",
    "primary school": "5th",
    "5": "5th",
    "5th standard": "5th",

    "middle school": "8th",
    "8": "8th",
    "8th standard": "8th",

    "secondary": "10th",
    "sslc": "10th",
    "10": "10th",
    "10th standard": "10th",

    "higher secondary": "12th",
    "puc": "12th",
    "pu": "12th",
    "12": "12th",
    "12th standard": "12th",

    "industrial training institute": "iti",
    "iti": "iti",

    "polytechnic": "diploma",
    "diploma": "diploma",

    "degree": "graduate",
    "graduation": "graduate",
    "graduate": "graduate",

    "post graduate": "postgraduate",
    "post-graduate": "postgraduate",
    "postgraduate": "postgraduate",
}


EDUCATION_RANK = {
    "5th": 1,
    "8th": 2,
    "10th": 3,
    "12th": 4,
    "iti": 4,
    "diploma": 5,
    "graduate": 6,
    "postgraduate": 7,
}


ACADEMIC_LEVELS = {
    "5th",
    "8th",
    "10th",
    "12th",
    "graduate",
    "postgraduate",
}


GENERIC_OCCUPATION_WORDS = {
    "assistant",
    "worker",
    "technician",
    "operator",
    "owner",
    "service",
    "services",
    "job",
    "self",
    "employment",
    "light",
    "motor",
    "vehicle",
}


SECTOR_HINTS = {
    "automotive": {
        "mechanic",
        "automobile",
        "vehicle",
        "car",
        "bike",
        "motorcycle",
        "driver",
        "driving",
        "auto",
        "two-wheeler",
        "two wheeler",
        "four-wheeler",
        "four wheeler",
    },

    "repair and maintenance": {
        "mechanic",
        "repair",
        "maintenance",
        "servicing",
        "technician",
    },

    "agriculture": {
        "farmer",
        "farming",
        "agriculture",
        "agricultural",
        "dairy",
        "poultry",
        "horticulture",
        "tractor",
    },

    "construction": {
        "mason",
        "construction",
        "carpenter",
        "plumber",
        "scaffolder",
        "painter",
    },

    "electrical": {
        "electrician",
        "electrical",
        "wireman",
        "wiring",
    },

    "electronics": {
        "electronics",
        "mobile repair",
        "cctv",
        "hardware repair",
    },

    "it-ites": {
        "computer",
        "data entry",
        "web developer",
        "digital marketing",
        "bpo",
        "call center",
    },

    "retail": {
        "sales",
        "retail",
        "cashier",
        "shop",
        "store",
    },

    "logistics": {
        "delivery",
        "warehouse",
        "forklift",
        "logistics",
    },

    "manufacturing": {
        "fitter",
        "welder",
        "machine",
        "manufacturing",
        "production",
        "cnc",
    },

    "hospitality": {
        "hotel",
        "cook",
        "waiter",
        "steward",
        "baker",
        "housekeeping",
        "hospitality",
    },

    "beauty and wellness": {
        "salon",
        "beauty",
        "beautician",
        "hair",
        "makeup",
        "spa",
        "wellness",
        "barber",
    },

    "healthcare support": {
        "healthcare",
        "health",
        "ambulance",
        "patient",
        "lab",
        "physiotherapy",
    },
}


RELATED_REPAIR_WORDS = {
    "mechanic",
    "repair",
    "maintenance",
    "servicing",
}


def normalize_education(value: str) -> str:
    value = normalize_text(value)
    return EDUCATION_ALIASES.get(value, value)


def education_compatibility(
    user_education: str,
    allowed_education: Set[str]
) -> Tuple[int, bool]:

    user_level = normalize_education(
        user_education
    )

    allowed_levels = {
        normalize_education(level)
        for level in allowed_education
        if str(level).strip()
    }

    if not user_level or not allowed_levels:
        return 0, False

    # Exact listed qualification.
    if user_level in allowed_levels:
        return EDUCATION_WEIGHT, True

    user_rank = EDUCATION_RANK.get(
        user_level
    )

    if user_rank is None:
        return 0, False

    # General-school / academic progression.
    # Example: 12th is compatible with a livelihood
    # whose dataset accepts 10th.
    academic_allowed = {
        level
        for level in allowed_levels
        if level in ACADEMIC_LEVELS
    }

    if academic_allowed:
        minimum_rank = min(
            EDUCATION_RANK[level]
            for level in academic_allowed
        )

        if user_rank >= minimum_rank:
            return EDUCATION_WEIGHT, True

    # Vocational progression:
    # Diploma/graduate can satisfy a listed ITI route,
    # but ordinary 12th is not silently treated as ITI.
    if "iti" in allowed_levels:
        if user_level in {
            "diploma",
            "graduate",
            "postgraduate",
        }:
            return EDUCATION_WEIGHT, True

    if "diploma" in allowed_levels:
        if user_level in {
            "graduate",
            "postgraduate",
        }:
            return EDUCATION_WEIGHT, True

    return 0, False


def occupation_tokens(
    value: str
) -> Set[str]:

    cleaned = normalize_text(
        value
    ).replace("-", " ")

    tokens = set(
        re.findall(
            r"[a-z0-9]+",
            cleaned
        )
    )

    return {
        token
        for token in tokens
        if (
            len(token) > 2
            and
            token not in GENERIC_OCCUPATION_WORDS
        )
    }


def sector_affinity(
    current_occupation: str,
    target_sector: str
) -> bool:

    current = normalize_text(
        current_occupation
    )

    sector = normalize_text(
        target_sector
    )

    hints = SECTOR_HINTS.get(
        sector,
        set()
    )

    return any(
        hint in current
        for hint in hints
    )


def occupation_relevance(
    current_occupation: str,
    target_occupation: str,
    target_sector: str
) -> Tuple[int, str]:

    current = normalize_text(
        current_occupation
    )

    target = normalize_text(
        target_occupation
    )

    if not current or not target:
        return 0, ""

    # Exact occupation match.
    if current == target:
        return (
            OCCUPATION_WEIGHT,
            "Current occupation directly matches this livelihood"
        )

    text_similarity = SequenceMatcher(
        None,
        current,
        target
    ).ratio()

    current_tokens = occupation_tokens(
        current
    )

    target_tokens = occupation_tokens(
        target
    )

    overlap_ratio = (
        len(
            current_tokens
            &
            target_tokens
        )
        /
        max(
            len(target_tokens),
            1
        )
    )

    # Strongly related occupation name.
    if (
        text_similarity >= 0.78
        or
        overlap_ratio >= 0.60
    ):
        return (
            20,
            "Current occupation is strongly related to this livelihood"
        )

    # Meaningful occupation-name overlap.
    if overlap_ratio >= 0.33:
        return (
            15,
            "Current occupation is related to this livelihood"
        )

    # Domain / sector relationship.
    if sector_affinity(
        current,
        target_sector
    ):
        return (
            10,
            "Current occupation is in a related work domain"
        )

    # A small cross-sector repair/mechanical relationship.
    if (
        current_tokens
        &
        RELATED_REPAIR_WORDS
        and
        target_tokens
        &
        RELATED_REPAIR_WORDS
    ):
        return (
            8,
            "Current occupation includes related repair experience"
        )

    return 0, ""


def experience_relevance_score(
    experience_years,
    occupation_relation_score: int
) -> int:

    try:
        years = max(
            0.0,
            float(
                experience_years
                or
                0
            )
        )
    except (
        TypeError,
        ValueError
    ):
        years = 0.0

    if (
        years <= 0
        or
        occupation_relation_score <= 0
    ):
        return 0

    # More years strengthen a recommendation only when
    # the beneficiary's current work is relevant to it.
    if years >= 5:
        base_score = 10
    elif years >= 3:
        base_score = 8
    elif years >= 2:
        base_score = 6
    else:
        base_score = 4

    if occupation_relation_score >= 25:
        relation_factor = 1.00
    elif occupation_relation_score >= 20:
        relation_factor = 0.80
    elif occupation_relation_score >= 15:
        relation_factor = 0.60
    else:
        relation_factor = 0.40

    return min(
        EXPERIENCE_WEIGHT,
        round(
            base_score
            *
            relation_factor
        )
    )


def build_explanation(
    occupation_name: str,
    score: int,
    matched_skills: List[str],
    matched_interests: List[str],
    reasons: List[str]
) -> str:

    explanation_parts = []

    if matched_skills:
        explanation_parts.append(
            "your existing skills in "
            + ", ".join(
                matched_skills
            )
            + " match required skills"
        )

    if matched_interests:
        explanation_parts.append(
            "your interests in "
            + ", ".join(
                matched_interests
            )
            + " align with this work"
        )

    if any(
        "Education requirement matched"
        in reason
        for reason in reasons
    ):
        explanation_parts.append(
            "your education is compatible"
        )

    if any(
        (
            "Current occupation"
            in reason
            or
            "current occupation"
            in reason
        )
        for reason in reasons
    ):
        explanation_parts.append(
            "your current work is relevant"
        )

    if any(
        "related experience"
        in reason.lower()
        for reason in reasons
    ):
        explanation_parts.append(
            "your related experience strengthens the match"
        )

    if explanation_parts:
        return (
            f"{occupation_name} is recommended because "
            + "; ".join(
                explanation_parts
            )
            + f". Overall profile match: {score}%."
        )

    return (
        f"{occupation_name} has an overall "
        f"profile match of {score}%."
    )


def calculate_score(
    profile: Dict,
    occupation: Dict
) -> Dict:

    reasons = []

    user_education = str(
        profile.get(
            "education_level",
            ""
        )
    ).strip()

    user_skills = {
        normalize_skill(skill)
        for skill in profile.get(
            "existing_skills",
            []
        )
        if str(skill).strip()
    }

    user_interests = {
        normalize_interest(
            interest
        )
        for interest in profile.get(
            "interests",
            []
        )
        if str(interest).strip()
    }

    allowed_education = {
        str(level).strip()
        for level in occupation.get(
            "minimum_education",
            []
        )
        if str(level).strip()
    }

    occupation_skills = {
        normalize_skill(skill)
        for skill in occupation.get(
            "skills",
            []
        )
        if str(skill).strip()
    }

    occupation_interests = {
        normalize_interest(
            interest
        )
        for interest in occupation.get(
            "interests",
            []
        )
        if str(interest).strip()
    }

    # ---------------------------------------------------------
    # 1. Education compatibility = 15%
    # ---------------------------------------------------------
    (
        education_score,
        education_matched
    ) = education_compatibility(
        user_education,
        allowed_education
    )

    if education_matched:
        reasons.append(
            "Education requirement matched"
        )

    # ---------------------------------------------------------
    # 2. Required skill coverage = 35%
    # ---------------------------------------------------------
    matched_skills = find_matches(
        user_skills,
        occupation_skills
    )

    skill_score = 0

    if matched_skills:
        skill_ratio = (
            len(matched_skills)
            /
            max(
                len(
                    occupation_skills
                ),
                1
            )
        )

        skill_score = round(
            SKILL_WEIGHT
            *
            skill_ratio
        )

        reasons.append(
            "Matched skills: "
            + ", ".join(
                matched_skills
            )
        )

    # ---------------------------------------------------------
    # 3. Interest alignment = 15%
    # ---------------------------------------------------------
    matched_interests = find_matches(
        user_interests,
        occupation_interests
    )

    interest_score = 0

    if matched_interests:
        interest_ratio = (
            len(
                matched_interests
            )
            /
            max(
                len(
                    occupation_interests
                ),
                1
            )
        )

        interest_score = round(
            INTEREST_WEIGHT
            *
            interest_ratio
        )

        reasons.append(
            "Matched interests: "
            + ", ".join(
                matched_interests
            )
        )

    # ---------------------------------------------------------
    # 4. Current occupation relevance = 25%
    # ---------------------------------------------------------
    current_occupation = str(
        profile.get(
            "current_occupation",
            ""
        )
    ).strip()

    (
        occupation_score,
        occupation_reason
    ) = occupation_relevance(
        current_occupation=current_occupation,
        target_occupation=str(
            occupation.get(
                "occupation",
                ""
            )
        ),
        target_sector=str(
            occupation.get(
                "sector",
                ""
            )
        )
    )

    if occupation_reason:
        reasons.append(
            occupation_reason
        )

    # ---------------------------------------------------------
    # 5. Related experience = 10%
    # ---------------------------------------------------------
    experience_score = (
        experience_relevance_score(
            profile.get(
                "experience_years",
                0
            ),
            occupation_score
        )
    )

    if experience_score > 0:
        reasons.append(
            "Related experience strengthened this match"
        )

    score = min(
        100,
        (
            education_score
            +
            skill_score
            +
            interest_score
            +
            occupation_score
            +
            experience_score
        )
    )

    recommendation_explanation = (
        build_explanation(
            occupation_name=occupation.get(
                "occupation",
                "This occupation"
            ),
            score=score,
            matched_skills=matched_skills,
            matched_interests=matched_interests,
            reasons=reasons
        )
    )

    return {
        "score": score,

        "reasons": reasons,

        "matched_skills":
            matched_skills,

        "matched_interests":
            matched_interests,

        "recommendation_explanation":
            recommendation_explanation,

        # Internal scoring details.
        # rank_occupations() uses these for tie-breaking
        # but does not expose them in the API response.
        "_education_score":
            education_score,

        "_skill_score":
            skill_score,

        "_interest_score":
            interest_score,

        "_occupation_score":
            occupation_score,

        "_experience_score":
            experience_score,
    }


def rank_occupations(
    profile: Dict,
    occupations: List[Dict],
    minimum_score: int = 25,
    top_n: int = 5
) -> List[Dict]:

    ranked = []

    for occupation in occupations:

        result = calculate_score(
            profile,
            occupation
        )

        has_personal_match = (
            len(
                result[
                    "matched_skills"
                ]
            )
            > 0
            or
            len(
                result[
                    "matched_interests"
                ]
            )
            > 0
            or
            result[
                "_occupation_score"
            ]
            > 0
        )

        if (
            result["score"]
            >= minimum_score
            and
            has_personal_match
        ):
            ranked.append({
                "occupation":
                    occupation[
                        "occupation"
                    ],

                "sector":
                    occupation[
                        "sector"
                    ],

                "match_score":
                    result[
                        "score"
                    ],

                "matched_skills":
                    result[
                        "matched_skills"
                    ],

                "matched_interests":
                    result[
                        "matched_interests"
                    ],

                "reasons":
                    result[
                        "reasons"
                    ],

                "recommendation_explanation":
                    result[
                        "recommendation_explanation"
                    ],

                # Private fields are removed
                # before returning recommendations.
                "_occupation_score":
                    result[
                        "_occupation_score"
                    ],

                "_skill_score":
                    result[
                        "_skill_score"
                    ],

                "_interest_score":
                    result[
                        "_interest_score"
                    ],

                "_experience_score":
                    result[
                        "_experience_score"
                    ],
            })

    # Stable and meaningful tie-breaking:
    # total score -> occupation relevance -> skills
    # -> interests -> experience -> occupation name.
    ranked.sort(
        key=lambda item: (
            item[
                "match_score"
            ],

            item[
                "_occupation_score"
            ],

            item[
                "_skill_score"
            ],

            item[
                "_interest_score"
            ],

            item[
                "_experience_score"
            ],

            item[
                "occupation"
            ].lower()
        ),
        reverse=True
    )

    output = []

    for item in ranked[:top_n]:

        cleaned_item = {
            key: value
            for key, value
            in item.items()
            if not key.startswith(
                "_"
            )
        }

        output.append(
            cleaned_item
        )

    return output
