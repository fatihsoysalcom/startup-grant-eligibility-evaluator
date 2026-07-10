import json

def evaluate_startup_for_grant(startup_profile, grant_criteria, min_score_threshold):
    """
    Evaluates a startup's eligibility for a grant based on predefined criteria.
    """
    total_score = 0
    detailed_scores = {}

    print(f"Evaluating startup: {startup_profile['name']}")
    print("-" * 30)

    # Iterate through each grant criterion defined by the grant-giving organization.
    # The article emphasizes that grant providers prioritize social, economic, or technological benefits.
    for criterion, weight in grant_criteria.items():
        # Get the startup's self-assessed or pre-evaluated score for this specific criterion
        startup_score = startup_profile.get('scores', {}).get(criterion, 0)

        # Calculate the weighted score for the criterion
        weighted_score = startup_score * weight
        total_score += weighted_score
        detailed_scores[criterion] = {
            "startup_score": startup_score,
            "weight": weight,
            "weighted_score": weighted_score
        }
        print(f"  - {criterion.replace('_', ' ').title()}: Score={startup_score}, Weight={weight}, Weighted Score={weighted_score:.2f}")

    print("-" * 30)
    print(f"Total Weighted Score: {total_score:.2f}")

    # Determine eligibility based on the total score against a minimum threshold.
    # This simulates the decision point for receiving non-repayable financial support (grant).
    if total_score >= min_score_threshold:
        print(f"Decision: QUALIFIED! (Score {total_score:.2f} >= Threshold {min_score_threshold})")
        return True, total_score, detailed_scores
    else:
        print(f"Decision: NOT QUALIFIED (Score {total_score:.2f} < Threshold {min_score_threshold})")
        return False, total_score, detailed_scores

if __name__ == "__main__":
    # Define the grant criteria and their relative importance (weights).
    # These criteria reflect the 'purpose' mentioned in the article for which grants are provided.
    grant_criteria = {
        "social_impact": 0.25,      # High weight for social benefit (e.g., community projects)
        "innovation_level": 0.30,   # High weight for technological benefit (e.g., R&D grants)
        "market_potential": 0.20,   # Economic benefit (e.g., job creation, market growth)
        "team_strength": 0.15,      # Importance of the founding team's capability
        "sustainability_plan": 0.10 # Long-term viability and environmental responsibility
    }

    # Normalize weights if they don't sum to 1 (optional, but good practice for clarity)
    total_weight = sum(grant_criteria.values())
    if abs(total_weight - 1.0) > 1e-6: # Check if sum is not approximately 1.0
        print(f"Warning: Grant criteria weights sum to {total_weight:.2f}, normalizing...")
        grant_criteria = {k: v / total_weight for k, v in grant_criteria.items()}
        print(f"Normalized weights: {json.dumps(grant_criteria, indent=2)}")

    # Define the minimum total score required to qualify for the grant.
    # Scores for each criterion are assumed to be out of 10. A threshold of 7.0 means roughly 70% of the maximum possible score.
    MIN_QUALIFYING_SCORE = 7.0

    # Example startup profiles applying for the grant
    startup_applications = [
        {
            "name": "EcoSolutions Inc.",
            "scores": {
                "social_impact": 9,
                "innovation_level": 8,
                "market_potential": 7,
                "team_strength": 8,
                "sustainability_plan": 9
            }
        },
        {
            "name": "QuickFix Tech",
            "scores": {
                "social_impact": 5,
                "innovation_level": 7,
                "market_potential": 8,
                "team_strength": 6,
                "sustainability_plan": 6
            }
        },
        {
            "name": "Community Connect",
            "scores": {
                "social_impact": 10,
                "innovation_level": 6,
                "market_potential": 6,
                "team_strength": 9,
                "sustainability_plan": 8
            }
        }
    ]

    print("\n--- Grant Evaluation Process ---")
    for i, startup in enumerate(startup_applications):
        print(f"\n--- Application {i+1} ---")
        is_qualified, final_score, details = evaluate_startup_for_grant(
            startup, grant_criteria, MIN_QUALIFYING_SCORE
        )
        # In a real system, these results would typically be stored or used for further processing.
