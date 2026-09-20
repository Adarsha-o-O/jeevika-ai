import re
from typing import Dict, Optional, Tuple


def normalize_text(value: str) -> str:
    return re.sub(
        r"\s+",
        " ",
        str(value or "").lower().strip()
    )


ACADEMIC_LEVELS = {
    "no formal education": 0,
    "5th": 1,
    "8th": 2,
    "9th": 3,
    "10th": 4,
    "11th": 5,
    "12th": 6,
    "diploma": 7,
    "graduate": 8,
    "postgraduate": 9,
}


def normalize_education(value: str) -> str:
    value = normalize_text(value)

    aliases = {
        "no formal schooling": "no formal education",
        "no schooling": "no formal education",

        "primary": "5th",
        "primary school": "5th",
        "5": "5th",
        "5th pass": "5th",
        "5th standard": "5th",
        "class 5": "5th",
        "grade 5": "5th",

        "8": "8th",
        "8th pass": "8th",
        "8th standard": "8th",
        "class 8": "8th",
        "grade 8": "8th",

        "9": "9th",
        "9th pass": "9th",
        "9th standard": "9th",
        "class 9": "9th",
        "grade 9": "9th",

        "10": "10th",
        "10th pass": "10th",
        "10th standard": "10th",
        "class 10": "10th",
        "grade 10": "10th",
        "sslc": "10th",

        "11": "11th",
        "11th pass": "11th",
        "11th standard": "11th",
        "class 11": "11th",
        "grade 11": "11th",

        "12": "12th",
        "12th pass": "12th",
        "12th standard": "12th",
        "class 12": "12th",
        "grade 12": "12th",
        "puc": "12th",
        "2nd puc": "12th",
        "higher secondary": "12th",

        "industrial training institute": "iti",
        "iti pass": "iti",

        "polytechnic": "diploma",

        "degree": "graduate",
        "graduation": "graduate",
        "ug": "graduate",

        "post graduate": "postgraduate",
        "post-graduate": "postgraduate",
        "pg": "postgraduate",

        "read and write": "ability to read and write",
        "literate": "ability to read and write",
    }

    return aliases.get(value, value)


def extract_experience_years(profile: Dict) -> float:
    value = profile.get("experience_years", 0)

    try:
        return max(0.0, float(value))
    except (TypeError, ValueError):
        return 0.0


def required_experience_years(
    qualification: Dict
) -> float:
    requirement = normalize_text(
        qualification.get(
            "experience_required",
            ""
        )
    )

    if (
        not requirement
        or "no experience" in requirement
        or requirement in {
            "none",
            "n/a",
            "na"
        }
    ):
        return 0.0

    number_match = re.search(
        r"(\d+(?:\.\d+)?)",
        requirement
    )

    if not number_match:
        return 0.0

    value = float(
        number_match.group(1)
    )

    if (
        "month" in requirement
        and
        "year" not in requirement
    ):
        return value / 12.0

    return value


def _education_status(
    profile: Dict,
    qualification: Dict
) -> str:
    """
    Returns:
        eligible
        not_eligible
        needs_verification
    """

    user_education = normalize_education(
        profile.get(
            "education_level",
            ""
        )
    )

    required_education = normalize_education(
        qualification.get(
            "minimum_education",
            ""
        )
    )

    if not required_education:
        return "eligible"

    if required_education == "no formal education":
        return "eligible"

    if required_education == "ability to read and write":
        if user_education in ACADEMIC_LEVELS:
            return (
                "eligible"
                if ACADEMIC_LEVELS[
                    user_education
                ] >= 1
                else "needs_verification"
            )

        if user_education in {
            "iti",
            "diploma",
            "graduate",
            "postgraduate",
        }:
            return "eligible"

        return "needs_verification"

    # Vocational entry requirements should not be silently
    # treated as ordinary school levels.
    if required_education == "iti":
        return (
            "eligible"
            if user_education == "iti"
            else "not_eligible"
        )

    user_rank = ACADEMIC_LEVELS.get(
        user_education
    )

    required_rank = ACADEMIC_LEVELS.get(
        required_education
    )

    if (
        user_rank is not None
        and
        required_rank is not None
    ):
        return (
            "eligible"
            if user_rank >= required_rank
            else "not_eligible"
        )

    # Diploma/degree holders can satisfy school-level
    # education requirements.
    if (
        required_rank is not None
        and
        user_education in {
            "diploma",
            "graduate",
            "postgraduate",
        }
    ):
        return "eligible"

    if not user_education:
        return "needs_verification"

    return (
        "eligible"
        if user_education
        == required_education
        else "not_eligible"
    )


def check_education_eligibility(
    profile: Dict,
    qualification: Dict
) -> bool:
    return (
        _education_status(
            profile,
            qualification
        )
        == "eligible"
    )


def check_experience_eligibility(
    profile: Dict,
    qualification: Dict
) -> bool:
    user_years = extract_experience_years(
        profile
    )

    required_years = (
        required_experience_years(
            qualification
        )
    )

    return (
        user_years
        >= required_years
    )


def _profile_training_terms(
    profile: Dict
) -> set:
    values = []

    raw_many = profile.get(
        "training_qualifications",
        []
    )

    if isinstance(
        raw_many,
        (list, tuple, set)
    ):
        values.extend(
            str(item)
            for item in raw_many
        )

    raw_single = profile.get(
        "training_qualification",
        ""
    )

    if raw_single:
        values.append(
            str(raw_single)
        )

    user_education = normalize_education(
        profile.get(
            "education_level",
            ""
        )
    )

    if user_education == "iti":
        values.append("iti")

    normalized = set()

    for value in values:
        text = normalize_text(
            value
        )

        for token in re.split(
            r"[/,|;]+",
            text
        ):
            token = token.strip()

            if token:
                normalized.add(
                    token
                )

    return normalized


def _training_status(
    profile: Dict,
    qualification: Dict
) -> str:
    requirement = normalize_text(
        qualification.get(
            "training_qualification",
            ""
        )
    )

    if (
        not requirement
        or requirement in {
            "none",
            "n/a",
            "na"
        }
    ):
        return "eligible"

    required_terms = {
        term.strip()
        for term in re.split(
            r"[/,|;]+",
            requirement
        )
        if term.strip()
    }

    profile_terms = (
        _profile_training_terms(
            profile
        )
    )

    if not profile_terms:
        return "needs_verification"

    for required in required_terms:
        if any(
            required in present
            or present in required
            for present in profile_terms
        ):
            return "eligible"

    return "not_eligible"


def _prior_nsqf_status(
    profile: Dict,
    qualification: Dict
) -> str:
    required = normalize_text(
        qualification.get(
            "previous_nsqf_level",
            ""
        )
    )

    if not required:
        return "eligible"

    try:
        required_level = float(
            required
        )
    except ValueError:
        return "needs_verification"

    profile_value = profile.get(
        "previous_nsqf_level",
        None
    )

    if (
        profile_value is None
        or str(
            profile_value
        ).strip() == ""
    ):
        return "needs_verification"

    try:
        profile_level = float(
            profile_value
        )
    except (
        TypeError,
        ValueError
    ):
        return "needs_verification"

    return (
        "eligible"
        if profile_level
        >= required_level
        else "not_eligible"
    )


def _education_progress_status(
    profile: Dict,
    qualification: Dict
) -> str:
    requirement = normalize_text(
        qualification.get(
            "education_status",
            ""
        )
    )

    if (
        not requirement
        or requirement in {
            "passed",
            "none",
            "n/a",
            "na"
        }
    ):
        return "eligible"

    if "pursuing" in requirement:
        # A completed qualification at the same/higher level
        # already passes the ordinary education threshold.
        # If the route specifically depends on being enrolled,
        # Jeevika should not guess.
        explicit_status = normalize_text(
            profile.get(
                "education_status",
                ""
            )
        )

        if "pursuing" in explicit_status:
            return "eligible"

        return "needs_verification"

    return "needs_verification"


def evaluate_eligibility(
    profile: Dict,
    qualification: Dict
) -> Dict:
    education_status = (
        _education_status(
            profile,
            qualification
        )
    )

    experience_ok = (
        check_experience_eligibility(
            profile,
            qualification
        )
    )

    training_status = (
        _training_status(
            profile,
            qualification
        )
    )

    prior_nsqf_status = (
        _prior_nsqf_status(
            profile,
            qualification
        )
    )

    progress_status = (
        _education_progress_status(
            profile,
            qualification
        )
    )

    required_years = (
        required_experience_years(
            qualification
        )
    )

    statuses = [
        education_status,
        (
            "eligible"
            if experience_ok
            else "not_eligible"
        ),
        training_status,
        prior_nsqf_status,
        progress_status,
    ]

    if "not_eligible" in statuses:
        overall_status = (
            "not_eligible"
        )
    elif "needs_verification" in statuses:
        overall_status = (
            "needs_verification"
        )
    else:
        overall_status = "eligible"

    overall_eligible = (
        overall_status
        == "eligible"
    )

    if overall_status == "eligible":
        message = (
            "Beneficiary meets this "
            "recorded eligibility route."
        )

    elif overall_status == "needs_verification":
        message = (
            "This route may be relevant, "
            "but Jeevika needs an additional "
            "qualification detail to verify it."
        )

    elif (
        education_status == "eligible"
        and
        not experience_ok
    ):
        message = (
            "Education requirement is met, "
            f"but {required_years:g} years "
            "of relevant experience is required."
        )

    elif education_status == "not_eligible":
        message = (
            "The recorded education "
            "requirement is not currently met."
        )

    elif training_status == "not_eligible":
        message = (
            "The recorded training "
            "qualification requirement is "
            "not currently met."
        )

    elif prior_nsqf_status == "not_eligible":
        message = (
            "The recorded previous NSQF "
            "level requirement is not "
            "currently met."
        )

    else:
        message = (
            "Beneficiary does not currently "
            "meet this recorded eligibility route."
        )

    return {
        "education_eligible":
            education_status
            == "eligible",

        "experience_eligible":
            experience_ok,

        "training_eligible":
            training_status
            == "eligible",

        "previous_nsqf_eligible":
            prior_nsqf_status
            == "eligible",

        "verification_needed":
            overall_status
            == "needs_verification",

        "eligibility_status":
            overall_status,

        "overall_eligible":
            overall_eligible,

        "required_experience_years":
            required_years,

        "eligibility_message":
            message,
    }
