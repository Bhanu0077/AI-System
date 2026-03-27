import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.match_agent import match_agent
from agents.budget_agent import budget_agent
from agents.reach_agent import reach_agent

influencer = {
    "name": "TechGuru",
    "platform": "Instagram",
    "niche": "tech",
    "followers": 50000,
    "engagement": 8.0,
    "audience": "students",
    "cost": 2000
}

print("Match:", match_agent(influencer, "tech", "students"))
print("Budget:", budget_agent(influencer, 3000))
print("Reach Score:", reach_agent(influencer))