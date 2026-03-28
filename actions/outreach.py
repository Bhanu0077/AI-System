# actions/outreach.py

import os
import random
from openai import OpenAI


def get_client():
    api_key = os.getenv("FEATHERLESS_API_KEY")
    if not api_key:
        return None
    return OpenAI(
        api_key=api_key,
        base_url="https://api.featherless.ai/v1"
    )


def generate_email(influencer, goal, niche):
    client = get_client()
    if client is None:
        return "❌ API key not set"

    prompt = f"""
    Write a short professional collaboration email.

    Influencer Name: {influencer['name']}
    Platform: {influencer['platform']}
    Niche: {niche}
    Campaign Goal: {goal}

    Keep it under 80 words.
    """

    try:
        response = client.chat.completions.create(
            model="openchat-3.5",
            messages=[
                {"role": "system", "content": "You write short outreach emails."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Failed: {e}"


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
    statuses = ["sent", "seen", "replied"]

    return {
        "status": random.choice(statuses),
        "response_time": random.randint(1, 24),  # hours
        "accepted": random.choice([True, False])
    }


if __name__ == "__main__":
    influencer = {
        "name": "TechGuru",
        "platform": "Instagram"
    }
    result = generate_email(influencer, "Awareness", "tech")
    print("\n📧 EMAIL OUTPUT:\n")
    print(result)