from utils.logger import log

def budget_agent(influencer, budget):
    """
    Returns True if influencer cost <= budget
    """

    cost = influencer.get("cost", 0)

    if cost <= budget:
        return True

    return False

def within_budget(influencer, budget):
    result = influencer["cost"] <= budget

    log(f"[BudgetAgent] {influencer['name']} → {'OK' if result else 'TOO EXPENSIVE'}")

    return result