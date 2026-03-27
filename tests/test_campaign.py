from data.influencers import influencers
from actions.monitor import simulate_campaign, update_profile

profile = {
    "followers": 1000,
    "engagement": 60
}

result = simulate_campaign(influencers[0])
print(result)

updated = update_profile(profile)
print(updated)