from utils.logger import log

def run_pipeline(input_data):

    log("=================================")
    log("NEW CAMPAIGN STARTED")
    log(f"Input: {input_data}")

    from engine.selector import filter_influencers
    from engine.decision import rank_influencers, select_top
    from actions.outreach import simulate_outreach
    from actions.monitor import simulate_performance
    from data.influencers import get_influencers

    # ── 1. Generate influencer data ───────────────────────────────
    influencer_data = get_influencers(
        count=100,
        niche=input_data["query"],
        audience=input_data["audience"],
    )

    # ── 2. Filter influencers ─────────────────────────────────────
    filtered = filter_influencers(input_data, influencer_data)

    # ── 3. Rank influencers ───────────────────────────────────────
    ranked = rank_influencers(filtered)

    # ── 4. Select top influencers based on budget ────────────────
    selected, cost = select_top(ranked, input_data["budget"])

    log(f"[Selection] Selected {len(selected)} influencers | Cost: {cost}")

    # ── 5. Simulate outreach (FIXED) ─────────────────────────────
    outreach_results = []
    for influencer in selected:
        result = simulate_outreach(influencer)
        outreach_results.append(result)

    # ── 6. Simulate performance ──────────────────────────────────
    performance = simulate_performance(selected)

    log("CAMPAIGN COMPLETED")
    log("=================================")

    return {
        "selected": selected,
        "outreach": outreach_results,
        "performance": performance
    }