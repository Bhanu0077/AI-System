# engine/selector.py

from agents.match_agent import match_agent
from agents.budget_agent import budget_agent
from utils.logger import log


def filter_influencers(influencers, niche, audience, budget):
    """
    Use match_agent and budget_agent
    Return list of valid influencers
    """

    valid_influencers = []

    for influencer in influencers:
        try:
            # Step 1: Check niche & audience match
            match_score = match_agent(influencer, niche, audience)

            # Step 2: Check if within budget
            is_affordable = budget_agent(influencer, budget)

            # Step 3: Filter condition
            if match_score and is_affordable:
                valid_influencers.append(influencer)

        except Exception as e:
            # Skip problematic influencer safely
            continue

    return valid_influencers

def filter_influencers(input_data):
    log("[Selector] Starting filtering process")

    # your logic
    filtered = []

    log(f"[Selector] {len(filtered)} influencers passed filtering")

    return filtered