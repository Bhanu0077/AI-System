from engine.decision import rank_influencers, select_top_influencers, generate_reason

# Mock reach_agent (so your test doesn't depend on real agent)
import engine.decision

def mock_reach_agent(influencer):
    return influencer["followers"] * 0.01  # simple scoring logic

engine.decision.reach_agent = mock_reach_agent


# Test data
influencers = [
    {"name": "A", "followers": 10000, "cost": 500, "niche": "tech", "audience": "students"},
    {"name": "B", "followers": 50000, "cost": 2000, "niche": "fitness", "audience": "youth"},
    {"name": "C", "followers": 30000, "cost": 1500, "niche": "fashion", "audience": "women"},
]

budget = 2500


# Test ranking
ranked = rank_influencers(influencers)
print("Ranked:")
for i in ranked:
    print(i["name"], i["score"])


# Test selection
selected = select_top_influencers(ranked, budget)
print("\nSelected:")
for i in selected:
    print(i["name"], i["cost"])


# Test reason generation
print("\nReasons:")
for i in selected:
    print(generate_reason(i))