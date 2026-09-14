from typing import Dict, List

from app.ml.text_matcher import normalize_skill


def add_skill_gaps(
    profile: Dict,
    recommendations: List[Dict],
    occupations: List[Dict]
) -> List[Dict]:

    occupation_lookup = {
        item["occupation"]: item
        for item in occupations
    }

    enriched_results = []

    for recommendation in recommendations:

        occupation_name = recommendation["occupation"]

        occupation = occupation_lookup.get(
            occupation_name
        )

        if occupation is None:
            continue

        required_skills = sorted({
            normalize_skill(skill)
            for skill in occupation.get(
                "skills",
                []
            )
        })

        # Reuse skills already matched by scoring_engine
        matched_skills = {
            normalize_skill(skill)
            for skill in recommendation.get(
                "matched_skills",
                []
            )
        }

        missing_skills = [
            skill
            for skill in required_skills
            if skill not in matched_skills
        ]

        enriched_recommendation = {
            **recommendation,

            "required_skills":
                required_skills,

            "skill_gap":
                missing_skills,

            "skill_gap_count":
                len(missing_skills)
        }

        enriched_results.append(
            enriched_recommendation
        )

    return enriched_results