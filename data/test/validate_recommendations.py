import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT / "backend"))

from app.ml.livelihood_mapper import map_livelihood


profiles = [
    {
        "name": "Agriculture Worker",
        "expected": ["farmer", "agriculture", "dairy", "poultry"],
        "profile": {
            "education_level": "8th",
            "current_occupation": "Agricultural Labourer",
            "existing_skills": ["farming", "tools", "animal care"],
            "interests": ["agriculture", "farming"],
            "experience_years": 3,
        }
    },

    {
        "name": "Tailoring Worker",
        "expected": ["tailor", "apparel", "stitch"],
        "profile": {
            "education_level": "8th",
            "current_occupation": "Tailoring Worker",
            "existing_skills": ["stitching", "sewing"],
            "interests": ["design", "fashion"],
            "experience_years": 2,
        }
    },

    {
        "name": "Two-Wheeler Mechanic",
        "expected": ["two-wheeler", "mechanic", "automotive"],
        "profile": {
            "education_level": "10th",
            "current_occupation": "Mechanic Helper",
            "existing_skills": ["mechanical work", "vehicle repair"],
            "interests": ["automobiles", "repair work"],
            "experience_years": 2,
        }
    },

    {
        "name": "Data Entry Candidate",
        "expected": ["data entry", "office assistant", "computer"],
        "profile": {
            "education_level": "10th",
            "current_occupation": "Student",
            "existing_skills": ["typing", "computer basics"],
            "interests": ["computers", "office work"],
            "experience_years": 0,
        }
    },

    {
        "name": "Retail Sales Worker",
        "expected": ["retail", "sales"],
        "profile": {
            "education_level": "10th",
            "current_occupation": "Shop Assistant",
            "existing_skills": ["sales", "customer service"],
            "interests": ["retail", "business"],
            "experience_years": 1,
        }
    },

    {
        "name": "Electrician",
        "expected": ["electrician", "electrical"],
        "profile": {
            "education_level": "10th",
            "current_occupation": "Electrician Helper",
            "existing_skills": ["electrical work", "wiring"],
            "interests": ["repair work", "technical work"],
            "experience_years": 2,
        }
    },

    {
        "name": "Welder",
        "expected": ["welder", "welding", "fabrication"],
        "profile": {
            "education_level": "10th",
            "current_occupation": "Workshop Helper",
            "existing_skills": ["welding", "metal work"],
            "interests": ["repair work", "technical work"],
            "experience_years": 2,
        }
    },

    {
        "name": "Driver",
        "expected": ["driver", "driving", "transport"],
        "profile": {
            "education_level": "10th",
            "current_occupation": "Driver",
            "existing_skills": ["driving", "road safety"],
            "interests": ["automobiles", "driving"],
            "experience_years": 3,
        }
    },

    {
        "name": "Beauty & Wellness Worker",
        "expected": ["beauty", "salon", "wellness", "hair"],
        "profile": {
            "education_level": "10th",
            "current_occupation": "Salon Helper",
            "existing_skills": ["beauty care", "customer service"],
            "interests": ["beauty", "wellness"],
            "experience_years": 1,
        }
    },

    {
        "name": "Low Education Rural Worker",
        "expected": ["farmer", "agriculture", "dairy", "poultry"],
        "profile": {
            "education_level": "5th",
            "current_occupation": "Farm Labourer",
            "existing_skills": ["farming", "animal care"],
            "interests": ["agriculture"],
            "experience_years": 4,
        }
    },
]


def matches_expected(result, expected):
    text = (
        str(result.get("occupation", "")) + " " +
        str(result.get("sector", ""))
    ).lower()

    return any(word.lower() in text for word in expected)


passed = 0
needs_check = 0
failed = 0

for number, item in enumerate(profiles, 1):

    profile = item["profile"]

    profile.update({
        "beneficiary_id": number,
        "state": "Karnataka",
        "district": "Shivamogga",
        "preferred_language": "Kannada",
        "willing_to_relocate": False,
    })

    results = map_livelihood(profile)

    print("\n" + "=" * 75)
    print(f"{number}. {item['name']}")
    print("=" * 75)

    if not results:
        print("STATUS: FAIL - No recommendations")
        failed += 1
        continue

    for rank, result in enumerate(results, 1):
        print(
            f"{rank}. {result['occupation']} | "
            f"{result['match_score']}% | "
            f"Skills: {result.get('matched_skills', [])} | "
            f"Gaps: {result.get('skill_gap', [])} | "
            f"NSQF: {len(result.get('nsqf_qualifications', []))}"
        )

    top1_ok = matches_expected(
        results[0],
        item["expected"]
    )

    top5_ok = any(
        matches_expected(result, item["expected"])
        for result in results
    )

    if top1_ok:
        print("STATUS: PASS")
        passed += 1

    elif top5_ok:
        print("STATUS: CHECK - Relevant occupation exists but ranking needs review")
        needs_check += 1

    else:
        print("STATUS: FAIL - Expected livelihood missing from top recommendations")
        failed += 1


print("\n" + "=" * 75)
print("FINAL VALIDATION SUMMARY")
print("=" * 75)
print(f"PASS  : {passed}/10")
print(f"CHECK : {needs_check}/10")
print(f"FAIL  : {failed}/10")

if failed == 0 and needs_check <= 2:
    print("RESULT: Recommendation engine is in strong condition.")
elif failed <= 2:
    print("RESULT: Minor ranking improvements required.")
else:
    print("RESULT: Ranking/scoring requires correction before finalization.")
