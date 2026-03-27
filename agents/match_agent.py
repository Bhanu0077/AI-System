from utils.logger import log

def match_agent(influencer, niche, audience):
    """
    Returns True if influencer matches niche and audience, else False
    """

    # Normalize strings (avoid case issues)
    inf_niche = influencer.get("niche", "").lower()
    inf_audience = influencer.get("audience", "").lower()

    niche = niche.lower()
    audience = audience.lower()

    # Check match
    if inf_niche == niche and audience in inf_audience:
        return True

    return False

def match(influencer, query):
    return query.lower() in influencer["niche"].lower()