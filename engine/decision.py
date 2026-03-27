# engine/decision.py

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


def select_top_influencers(ranked_list, budget):
    """
    Select top influencers within budget
    Return selected list
    """

    selected = []
    total_spent = 0

    for influencer in ranked_list:
        cost = influencer.get("cost", 0)

        if total_spent + cost <= budget:
            selected.append(influencer)
            total_spent += cost
        else:
            continue

    return selected


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