# actions/monitor.py

import random


def simulate_campaign(influencer):
    """
    Input: influencer dict
    Output: dict with:
        - engagement (float)
        - reach (int)
        - success (bool)
    """

    # Simulated engagement variation
    engagement = round(random.uniform(5.0, 15.0), 2)

    # Calculate reach
    reach = int(influencer["followers"] * (engagement / 100))

    # Define success condition
    success = engagement > 8.0

    return {
        "engagement": engagement,
        "reach": reach,
        "success": success
    }


def update_profile(profile):
    """
    Input: profile dict
    Output: updated profile
    """

    # Simulate follower change
    follower_change = random.randint(-10, 25)
    profile["followers"] += follower_change

    # Simulate engagement change
    engagement_change = random.uniform(-2.0, 2.0)
    profile["engagement"] += engagement_change

    # Keep values realistic
    profile["engagement"] = max(0, min(profile["engagement"], 100))

    return profile