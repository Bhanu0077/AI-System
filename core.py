def run_pipeline(input_data):
    from engine.selector import filter_influencers
    from engine.decision import rank_influencers, select_top, generate_reasoning
    from actions.outreach import simulate_outreach
    from actions.monitor import simulate_performance

    influencers = filter_influencers(input_data)

    ranked = rank_influencers(influencers)

    selected, total_cost = select_top(ranked, input_data["budget"])

    reasoning = generate_reasoning(selected)

    outreach = simulate_outreach(selected)

    performance = simulate_performance(selected)

    return {
        "selected": selected,
        "cost": total_cost,
        "reasoning": reasoning,
        "outreach": outreach,
        "performance": performance
    }