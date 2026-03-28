from data.featherless_client import generate_influencers
def run():
    print("\n Influencer Campaign System (AI Generated Data)\n")

    niche = input("Enter niche: ")
    audience = input("Enter audience: ")
    budget = int(input("Enter budget: "))

    # 🔥 Generate influencers using LLM
    influencers = generate_influencers(niche, audience)

    if not influencers:
        print(" Failed to generate influencers")
        return

    print("\n Generated Influencers:\n")
    for inf in influencers:
        print(inf)

    # Continue same pipeline
    from engine.selector import filter_influencers
    from engine.decision import rank_influencers, select_top_influencers, generate_reason
    from actions.outreach import generate_outreach_message, simulate_outreach
    from actions.monitor import simulate_campaign
    from data.influencer_generator import generate_influencers

    influencers = generate_influencers(niche, audience)
    influencers = generate_influencers(niche, audience)

    filtered = filter_influencers(influencers, niche, audience, budget)
    if not filtered:
        print(" No influencers matched your criteria")
        return

    ranked = rank_influencers(filtered)
    selected = select_top_influencers(ranked, budget)

    print("\n Selected Influencers:\n")

    for inf in selected:
        print(f" {inf['name']}")
        print(f"   Score: {inf['followers'] * (inf['engagement']/100)}")
        print(f"   Reason: {generate_reason(inf)}")

        print("\n Outreach:")
        print(generate_outreach_message(inf, "Awareness", niche))

        print(" Response:", simulate_outreach(inf))
        print(" Performance:", simulate_campaign(inf))
        print("-" * 40)