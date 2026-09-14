from typing import Dict, List

from app.ml.text_matcher import (
    normalize_skill,
    normalize_interest,
    find_matches
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
            "your skills in "
            + ", ".join(matched_skills)
            + " match this occupation"
        )

    if matched_interests:
        explanation_parts.append(
            "your interests in "
            + ", ".join(matched_interests)
            + " are relevant"
        )

    if any(
        "Education requirement matched" in reason
        for reason in reasons
    ):
        explanation_parts.append(
            "your education matches the occupation requirement"
        )

    if any(
        "current work experience" in reason
        for reason in reasons
    ):
        explanation_parts.append(
            "your current work experience is related to this field"
        )

    if explanation_parts:
        return (
            f"{occupation_name} is recommended because "
            + "; ".join(explanation_parts)
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

    score = 0
    reasons = []

    user_education = str(
        profile.get("education_level", "")
    ).lower().strip()

    user_skills = {
        normalize_skill(skill)
        for skill in profile.get(
            "existing_skills",
            []
        )
    }

    user_interests = {
        normalize_interest(interest)
        for interest in profile.get(
            "interests",
            []
        )
    }

    allowed_education = {
        str(level).lower().strip()
        for level in occupation.get(
            "minimum_education",
            []
        )
    }

    occupation_skills = {
        normalize_skill(skill)
        for skill in occupation.get(
            "skills",
            []
        )
    }

    occupation_interests = {
        normalize_interest(interest)
        for interest in occupation.get(
            "interests",
            []
        )
    }

    # Education = 20%
    if user_education in allowed_education:
        score += 20
        reasons.append(
            "Education requirement matched"
        )

    # Skill matching = maximum 40%
    matched_skills = find_matches(
        user_skills,
        occupation_skills
    )

    if matched_skills:
        skill_ratio = (
            len(matched_skills)
            / max(
                len(occupation_skills),
                1
            )
        )

        skill_score = round(
            40 * skill_ratio
        )

        score += skill_score

        reasons.append(
            "Matched skills: "
            + ", ".join(matched_skills)
        )

    # Interest matching = maximum 30%
    matched_interests = find_matches(
        user_interests,
        occupation_interests
    )

    if matched_interests:
        interest_ratio = (
            len(matched_interests)
            / max(
                len(occupation_interests),
                1
            )
        )

        interest_score = round(
            30 * interest_ratio
        )

        score += interest_score

        reasons.append(
            "Matched interests: "
            + ", ".join(matched_interests)
        )

    # Current occupation relationship = 10%
    current_occupation = str(
        profile.get(
            "current_occupation",
            ""
        )
    ).lower()

    sector = str(
        occupation.get(
            "sector",
            ""
        )
    ).lower()

    if (
        "agricultur" in current_occupation
        and sector == "agriculture"
    ):
        score += 10

        reasons.append(
            "Related to beneficiary's "
            "current work experience"
        )

    score = min(score, 100)

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
        "matched_skills": matched_skills,
        "matched_interests": matched_interests,
        "recommendation_explanation":
            recommendation_explanation
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
            len(result["matched_skills"]) > 0
            or
            len(result["matched_interests"]) > 0
        )

        if (
            result["score"] >= minimum_score
            and has_personal_match
        ):
            ranked.append({
                "occupation":
                    occupation["occupation"],

                "sector":
                    occupation["sector"],

                "match_score":
                    result["score"],

                "matched_skills":
                    result["matched_skills"],

                "matched_interests":
                    result["matched_interests"],

                "reasons":
                    result["reasons"],

                "recommendation_explanation":
                    result[
                        "recommendation_explanation"
                    ]
            })

    ranked.sort(
        key=lambda item:
            item["match_score"],
        reverse=True
    )

    return ranked[:top_n]