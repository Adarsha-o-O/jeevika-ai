from typing import Dict, List


def build_explanation(
    occupation_name: str,
    score: int,
    matched_skills: List[str],
    matched_interests: List[str],
    reasons: List[str]
) -> str:
    """
    Build a simple human-readable explanation
    for the recommendation.
    """

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
        explanation = (
            f"{occupation_name} is recommended because "
            + "; ".join(explanation_parts)
            + f". Overall profile match: {score}%."
        )
    else:
        explanation = (
            f"{occupation_name} has an overall "
            f"profile match of {score}%."
        )

    return explanation


def calculate_score(
    profile: Dict,
    occupation: Dict
) -> Dict:
    """
    Calculate compatibility score between
    a beneficiary and an occupation.
    """

    score = 0
    reasons = []

    user_education = str(
        profile.get("education_level", "")
    ).lower().strip()

    user_skills = {
        str(skill).lower().strip()
        for skill in profile.get(
            "existing_skills",
            []
        )
    }

    user_interests = {
        str(interest).lower().strip()
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
        str(skill).lower().strip()
        for skill in occupation.get(
            "skills",
            []
        )
    }

    occupation_interests = {
        str(interest).lower().strip()
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

    # Existing skills = maximum 40%
    matched_skills = user_skills.intersection(
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
            + ", ".join(
                sorted(matched_skills)
            )
        )

    # Interests = maximum 30%
    matched_interests = (
        user_interests.intersection(
            occupation_interests
        )
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
            + ", ".join(
                sorted(matched_interests)
            )
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

    score = min(
        score,
        100
    )

    matched_skills_list = sorted(
        matched_skills
    )

    matched_interests_list = sorted(
        matched_interests
    )

    recommendation_explanation = (
        build_explanation(
            occupation_name=occupation.get(
                "occupation",
                "This occupation"
            ),
            score=score,
            matched_skills=matched_skills_list,
            matched_interests=matched_interests_list,
            reasons=reasons
        )
    )

    return {
        "score": score,
        "reasons": reasons,
        "matched_skills":
            matched_skills_list,

        "matched_interests":
            matched_interests_list,

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

        # Avoid recommendations
        # based only on education.
        has_personal_match = (
            len(
                result[
                    "matched_skills"
                ]
            ) > 0

            or

            len(
                result[
                    "matched_interests"
                ]
            ) > 0
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
                    result["score"],

                "matched_skills":
                    result[
                        "matched_skills"
                    ],

                "matched_interests":
                    result[
                        "matched_interests"
                    ],

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