# tests/run_system.py

from data.influencers import influencers
from engine.selector import filter_influencers
from engine.decision import rank_influencers, select_top_influencers, generate_reason
from actions.monitor import simulate_campaign
from actions.outreach import generate_outreach_message, simulate_outreach


def run():

    print("\n🚀 Influencer Campaign System\n")

    # TAKE INPUT
    niche = input("Enter niche (e.g. tech, fitness): ").lower()
    audience = input("Enter target audience (e.g. students): ").lower()
    budget = int(input("Enter budget: "))

    print("\n🔍 Running system...\n")

    # STEP 1: FILTER
    filtered = filter_influencers(influencers, niche, audience, budget)

    if not filtered:
        print("❌ No influencers found matching criteria.")
        return

    # STEP 2: RANK
    ranked = rank_influencers(filtered)

    # STEP 3: SELECT
    selected = select_top_influencers(ranked, budget)

    print("🏆 Selected Influencers:\n")

    for inf in selected:
        print(f"👉 {inf['name']}")
        print(f"   Followers: {inf['followers']}")
        print(f"   Engagement: {inf['engagement']}%")
        print(f"   Cost: ₹{inf['cost']}")

        # REASON
        reason = generate_reason(inf)
        print(f"   Reason: {reason}")

        # OUTREACH
        msg = generate_outreach_message(inf, "Mass Awareness", niche)
        print("\n📧 Outreach Message:")
        print(msg)

        status = simulate_outreach(inf)
        print("📨 Outreach Status:", status)

        # CAMPAIGN RESULT
        perf = simulate_campaign(inf)
        print("📈 Campaign Result:", perf)

        print("-" * 50)

    print("\n✅ System execution complete!\n")


if __name__ == "__main__":
    run()