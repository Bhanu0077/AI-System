def budget_agent(influencer, budget):
    """
    Returns True if influencer cost <= budget
    """

    cost = influencer.get("cost", 0)

    if cost <= budget:
        return True

    return False