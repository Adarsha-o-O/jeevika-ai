from difflib import SequenceMatcher
import re
from typing import List, Set


SKILL_ALIASES = {
    "car repair": "mechanical work",
    "vehicle repair": "mechanical work",
    "mechanic work": "mechanical work",
    "car mechanic": "mechanical work",

    "bike repair": "mechanical work",
    "motorcycle repair": "mechanical work",
    "two wheeler repair": "mechanical work",
    "two-wheeler repair": "mechanical work",
    "vehicle servicing": "mechanical work",
    "bike servicing": "mechanical work",
    "automobile servicing": "mechanical work",

    "computer knowledge": "computer basics",
    "basic computer": "computer basics",
    "computer skills": "computer basics",
    "computer operating": "computer basics",

    "customer handling": "customer service",
    "customer support": "customer service",
    "customer dealing": "customer service",

    "salesmanship": "sales",
    "selling": "sales",

    "typing skills": "typing",

    "electrical repair": "electrical work",
    "electrical maintenance": "electrical work",
    "electric wiring": "wiring",

    "pipe work": "pipe fitting",
    "plumbing work": "plumbing",

    "metal fabrication": "metal work",

    "farm work": "farming",
    "agricultural work": "farming",

    "sewing work": "sewing",
    "tailoring": "stitching",

    "mobile repairing": "electronics repair",

    "cooking skills": "cooking",
    "cleaning work": "cleaning",

    "beauty care": "beauty services",
    "salon work": "beauty services",
    "beauty work": "beauty services"
}


INTEREST_ALIASES = {
    "cars": "automobiles",
    "vehicles": "automobiles",
    "motorcycles": "automobiles",
    "bikes": "automobiles",

    "vehicle servicing": "automobiles",
    "automobile servicing": "automobiles",
    "bike servicing": "automobiles",
    "car servicing": "automobiles",

    "computer": "computers",
    "technology": "technical work",

    "farming": "agriculture",

    "fashion designing": "design",

    "repairing": "repair work",
    "mechanics": "repair work",

    "helping people": "healthcare",

    "food": "cooking",

    "beauty": "beauty and wellness",
    "wellness": "beauty and wellness",
    "salon": "beauty and wellness"
}


def normalize_text(
    value: str
) -> str:

    value = str(
        value
    ).lower().strip()

    # Normalize repeated spaces without
    # changing meaningful punctuation.
    return re.sub(
        r"\s+",
        " ",
        value
    )


def normalize_skill(
    value: str
) -> str:

    value = normalize_text(
        value
    )

    return SKILL_ALIASES.get(
        value,
        value
    )


def normalize_interest(
    value: str
) -> str:

    value = normalize_text(
        value
    )

    return INTEREST_ALIASES.get(
        value,
        value
    )


def similarity_score(
    value1: str,
    value2: str
) -> float:

    return SequenceMatcher(
        None,
        normalize_text(
            value1
        ),
        normalize_text(
            value2
        )
    ).ratio()


def is_similar(
    value1: str,
    value2: str,
    threshold: float = 0.82
) -> bool:

    value1 = normalize_text(
        value1
    )

    value2 = normalize_text(
        value2
    )

    if value1 == value2:
        return True

    # Direct phrase containment.
    if (
        len(value1) >= 4
        and
        len(value2) >= 4
        and
        (
            value1 in value2
            or
            value2 in value1
        )
    ):
        return True

    # Prevent common false fuzzy matches such as:
    # technical work vs mechanical work.
    if (
        len(value1) >= 2
        and
        len(value2) >= 2
        and
        value1[:2]
        !=
        value2[:2]
    ):
        return False

    return (
        similarity_score(
            value1,
            value2
        )
        >=
        threshold
    )


def find_matches(
    user_values: Set[str],
    required_values: Set[str]
) -> List[str]:

    matched = set()

    for required in required_values:

        for user_value in user_values:

            if is_similar(
                user_value,
                required
            ):
                matched.add(
                    required
                )
                break

    return sorted(
        matched
    )
