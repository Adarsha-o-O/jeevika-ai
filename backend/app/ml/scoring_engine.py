from typing import Dict, List


def calculate_score(profile: Dict, occupation: Dict) -> Dict:
    """
    Calculate a more detailed compatibility score between
    a beneficiary and an occupation.
    """

    score = 0
    reasons = []

    user_education = profile.get("education_level", "").lower()

    user_skills = {
        skill.lower()
        for skill in profile.get("existing_skills", [])
    }

    user_interests = {
        interest.lower()
        for interest in profile.get("interests", [])
    }

    allowed_education = {
        level.lower()
        for level in occupation.get("minimum_education", [])
    }

    occupation_skills = {
        skill.lower()
        for skill in occupation.get("skills", [])
    }

    occupation_interests = {
        interest.lower()
        for interest in occupation.get("interests", [])
    }

    # Education = 20%
    if user_education in allowed_education:
        score += 20
        reasons.append("Education requirement matched")

    # Existing skills = maximum 40%
    matched_skills = user_skills.intersection(occupation_skills)

    if matched_skills:
        skill_ratio = len(matched_skills) / max(
            len(occupation_skills), 1
        )

        skill_score = round(40 * skill_ratio)
        score += skill_score

        reasons.append(
            f"Matched skills: {', '.join(sorted(matched_skills))}"
        )

    # Interests = maximum 30%
    matched_interests = user_interests.intersection(
        occupation_interests
    )

    if matched_interests:
        interest_ratio = len(matched_interests) / max(
            len(occupation_interests), 1
        )

        interest_score = round(30 * interest_ratio)
        score += interest_score

        reasons.append(
            f"Matched interests: {', '.join(sorted(matched_interests))}"
        )

    # Current occupation relationship = 10%
    current_occupation = profile.get(
        "current_occupation", ""
    ).lower()

    sector = occupation.get("sector", "").lower()

    if (
        "agricultur" in current_occupation
        and sector == "agriculture"
    ):
        score += 10
        reasons.append(
            "Related to beneficiary's current work experience"
        )

    return {
        "score": min(score, 100),
        "reasons": reasons,
        "matched_skills": sorted(matched_skills),
        "matched_interests": sorted(matched_interests)
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

        # Avoid recommendations based only on education.
        has_personal_match = (
            len(result["matched_skills"]) > 0
            or len(result["matched_interests"]) > 0
        )

        if (
            result["score"] >= minimum_score
            and has_personal_match
        ):
            ranked.append({
                "occupation": occupation["occupation"],
                "sector": occupation["sector"],
                "match_score": result["score"],
                "matched_skills": result["matched_skills"],
                "matched_interests": result["matched_interests"],
                "reasons": result["reasons"]
            })

    ranked.sort(
        key=lambda item: item["match_score"],
        reverse=True
    )

    return ranked[:top_n]