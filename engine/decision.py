# engine/decision.py

from utils.logger import log
from agents.reach_agent import reach_agent


def rank_influencers(influencers):
    """
    Use reach_agent
    Return list sorted by score (highest first)
    """

    scored_list = []

    for influencer in influencers:
        try:
            score = reach_agent(influencer)
            influencer["score"] = score
            scored_list.append(influencer)
        except Exception:
            continue

    # Sort descending by score
    ranked = sorted(scored_list, key=lambda x: x["score"], reverse=True)

    return ranked


def select_top(influencers, budget):
    selected = []
    total_cost = 0

    for inf in influencers:
        if total_cost + inf["cost"] <= budget:
            selected.append(inf)
            total_cost += inf["cost"]

    return selected, total_cost

def generate_reason(influencer):
    """
    Return string explaining why selected
    """

    name = influencer.get("name", "This influencer")
    score = influencer.get("score", 0)
    niche = influencer.get("niche", "relevant niche")
    audience = influencer.get("audience", "target audience")

    reason = (
        f"{name} was selected due to a high reach score of {score}, "
        f"strong alignment with the {niche} niche, and relevance to the "
        f"{audience} audience. Additionally, the influencer fits within the campaign budget."
    )

    return reason

def rank_influencers(influencers):
    return sorted(influencers, key=lambda x: x["reach_score"], reverse=True)