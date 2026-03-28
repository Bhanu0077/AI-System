# data/influencer_generator.py

import random


_PLATFORMS = ("Instagram", "YouTube", "TikTok", "Twitter")


def generate_influencers(count, niche=None, audience=None):
    """
    Build a synthetic influencer list for the pipeline.

    When *niche* / *audience* are provided, most rows embed those strings so
    selector matching can succeed.
    """
    niche = (niche or "lifestyle").strip()
    audience = (audience or "general").strip()

    influencers = []
    for i in range(max(1, int(count))):
        use_campaign = random.random() < 0.85
        inf_niche = niche if use_campaign else random.choice(
            [niche, f"{niche} creators", "lifestyle", "tech reviews", "fitness"]
        )
        inf_audience = (
            f"{audience} followers"
            if use_campaign
            else f"{audience} and {random.choice(['students', 'professionals', 'creators'])}"
        )

        followers = random.randint(5_000, 500_000)
        engagement = round(random.uniform(3.0, 12.0), 2)
        cost = max(100, int(followers * random.uniform(0.0008, 0.004)))

        influencers.append(
            {
                "name": f"Creator_{i + 1}_{random.randint(100, 999)}",
                "platform": random.choice(_PLATFORMS),
                "niche": inf_niche,
                "followers": followers,
                "engagement": engagement,
                "audience": inf_audience,
                "cost": cost,
            }
        )

    return influencers
