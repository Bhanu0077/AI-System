
from agents.match_agent import match
from agents.budget_agent import within_budget
from agents.reach_agent import compute_reach
from utils.logger import log


def filter_influencers(input_data, influencers):
    """
    Filters influencers based on:
    - niche match
    - audience match
    - budget constraint
    """

    log("----- SELECTOR START -----")

    filtered = []
    total = len(influencers)

    log(f"Total influencers: {total}")

    for inf in influencers:

        log(f"Checking: {inf['name']}")

        # ---- MATCH CHECK ----
        if not match(inf, input_data["query"]):
            log(f"[REJECTED] Match failed → {inf['niche']}")
            continue
        else:
            log("[PASSED] Match")

        # ---- AUDIENCE CHECK ----
        if input_data["audience"].lower() not in inf["audience"].lower():
            log(f"[REJECTED] Audience mismatch → {inf['audience']}")
            continue
        else:
            log("[PASSED] Audience")

        # ---- BUDGET CHECK ----
        if not within_budget(inf, input_data["budget"]):
            log(f"[REJECTED] Budget failed → cost: {inf['cost']}")
            continue
        else:
            log("[PASSED] Budget")

        # ---- REACH SCORE ----
        reach_score = compute_reach(inf)
        inf["reach_score"] = reach_score

        log(f"[PASSED] Reach score: {reach_score}")

        filtered.append(inf)

    log(f"Final selected: {len(filtered)}")
    log("----- SELECTOR END -----\n")

    return filtered