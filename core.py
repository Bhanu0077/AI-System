from utils.logger import log

def run_pipeline(input_data):

    log("=================================")
    log("NEW CAMPAIGN STARTED")
    log(f"Input: {input_data}")

    from engine.selector import filter_influencers
    from engine.decision import rank_influencers, select_top
    from actions.outreach import simulate_outreach
    from actions.monitor import simulate_performance
    from data.influencers import influencers
    from engine.selector import filter_influencers
    from data.influencers import influencers as influencer_data

    filtered = filter_influencers(input_data, influencer_data)

    ranked = rank_influencers(filtered) 

    selected, cost = select_top(ranked, input_data["budget"])

    log(f"[Selection] Selected {len(selected)} influencers | Cost: {cost}")

    simulate_outreach(selected)

    performance = simulate_performance(selected)

    log("CAMPAIGN COMPLETED")
    log("=================================")

    return {
        "selected": selected,
        "performance": performance
    }