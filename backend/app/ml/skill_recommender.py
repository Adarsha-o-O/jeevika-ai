from typing import Dict, List

from app.ml.scoring_engine import normalize_skill


def detect_skill_gap(
    profile: Dict,
    occupation: Dict
) -> Dict:
    """
    Compare beneficiary skills with occupation requirements
    using the same skill normalization as the scoring engine.
    """

    user_skills = {
        normalize_skill(skill)
        for skill in profile.get(
            "existing_skills",
            []
        )
    }

    required_skills = {
        normalize_skill(skill)
        for skill in occupation.get(
            "skills",
            []
        )
    }

    matched_skills = sorted(
        user_skills.intersection(
            required_skills
        )
    )

    missing_skills = sorted(
        required_skills.difference(
            user_skills
        )
    )

    return {
        "occupation":
            occupation.get(
                "occupation"
            ),

        "sector":
            occupation.get(
                "sector"
            ),

        "matched_skills":
            matched_skills,

        "missing_skills":
            missing_skills,

        "skill_gap_count":
            len(
                missing_skills
            )
    }


def add_skill_gaps(
    profile: Dict,
    recommendations: List[Dict],
    occupations: List[Dict]
) -> List[Dict]:
    """
    Add normalized skill-gap information
    to livelihood recommendations.
    """

    occupation_lookup = {
        item["occupation"]: item
        for item in occupations
    }

    enriched_results = []

    for recommendation in recommendations:

        occupation_name = (
            recommendation[
                "occupation"
            ]
        )

        occupation = (
            occupation_lookup.get(
                occupation_name
            )
        )

        if occupation is None:
            continue

        gap = detect_skill_gap(
            profile,
            occupation
        )

        required_skills = sorted({
            normalize_skill(skill)
            for skill in occupation.get(
                "skills",
                []
            )
        })

        enriched_recommendation = {
            **recommendation,

            "required_skills":
                required_skills,

            "skill_gap":
                gap[
                    "missing_skills"
                ],

            "skill_gap_count":
                gap[
                    "skill_gap_count"
                ]
        }

        enriched_results.append(
            enriched_recommendation
        )

    return enriched_results