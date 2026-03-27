# actions/outreach.py

def generate_outreach_message(influencer, campaign_goal, niche):
    """
    Input:
        influencer (dict)
        campaign_goal (str)
        niche (str)

    Output:
        str (personalized outreach message)
    """

    name = influencer.get("name", "Creator")
    platform = influencer.get("platform", "your platform")

    message = (
        f"Hi {name},\n\n"
        f"We love your content on {platform}, especially in the {niche} space.\n"
        f"We are planning a campaign focused on '{campaign_goal}' and believe you would be a great fit.\n\n"
        f"We'd love to collaborate with you for this campaign. Let us know if you're interested!\n\n"
        f"Best regards,\n"
        f"Brand Team"
    )

    return message


def simulate_outreach(influencer):
    """
    Input:
        influencer (dict)

    Output:
        dict with:
            - status (str)
            - response_time (int)
            - accepted (bool)
    """

    import random

    statuses = ["sent", "seen", "replied"]

    status = random.choice(statuses)
    response_time = random.randint(1, 24)  # hours
    accepted = random.choice([True, False])

    return {
        "status": status,
        "response_time": response_time,
        "accepted": accepted
    }