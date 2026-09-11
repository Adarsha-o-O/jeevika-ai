from typing import Dict


def normalize_text(value: str) -> str:
    return str(value).lower().strip()


def check_education_eligibility(
    profile: Dict,
    qualification: Dict
) -> bool:
    user_education = normalize_text(
        profile.get("education_level", "")
    )

    required_education = normalize_text(
        qualification.get("minimum_education", "")
    )

    return user_education == required_education


def extract_experience_years(profile: Dict) -> float:
    """
    Expected profile field:
    experience_years

    Example:
    "experience_years": 2
    """

    value = profile.get("experience_years", 0)

    try:
        return float(value)
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
        requirement == ""
        or "no experience" in requirement
        or "none" in requirement
    ):
        return 0.0

    parts = requirement.split()

    for part in parts:
        try:
            return float(part)
        except ValueError:
            continue

    return 0.0


def check_experience_eligibility(
    profile: Dict,
    qualification: Dict
) -> bool:

    user_years = extract_experience_years(
        profile
    )

    required_years = required_experience_years(
        qualification
    )

    return user_years >= required_years


def evaluate_eligibility(
    profile: Dict,
    qualification: Dict
) -> Dict:

    education_ok = check_education_eligibility(
        profile,
        qualification
    )

    experience_ok = check_experience_eligibility(
        profile,
        qualification
    )

    overall_eligible = (
        education_ok and experience_ok
    )

    required_years = required_experience_years(
        qualification
    )

    if overall_eligible:
        message = (
            "Beneficiary meets the current "
            "education and experience requirements."
        )

    elif education_ok and not experience_ok:
        message = (
            f"Education requirement is met, "
            f"but {required_years:g} years of "
            f"experience is required."
        )

    elif not education_ok and experience_ok:
        message = (
            "Experience requirement is met, "
            "but education requirement is not met."
        )

    else:
        message = (
            "Beneficiary does not currently meet "
            "the education and experience requirements."
        )

    return {
        "education_eligible": education_ok,
        "experience_eligible": experience_ok,
        "overall_eligible": overall_eligible,
        "eligibility_message": message
    }