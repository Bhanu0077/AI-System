from featherless_client import call_featherless
from influencer_generator import generate_influencers

# generate influencers
influencers = generate_influencers(200)

# convert to text (for AI)
prompt = f"""
Find best influencers for:
- Product: tech product
- Audience: students
- Platform: Instagram

Here is data:
{influencers[:20]}  # don't send all 200 (token limit!)
"""

response = call_featherless(prompt)

print(response)