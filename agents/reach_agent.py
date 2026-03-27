
def reach_agent(influencer):
    """
    Returns a score = followers * (engagement / 100)
    """

    followers = influencer.get("followers", 0)
    engagement = influencer.get("engagement", 0)

    score = followers * (engagement / 100)

    return score


# Alias for compatibility (IMPORTANT)
def compute_reach(influencer):
    return reach_agent(influencer)