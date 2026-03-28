import os
import json
from openai import OpenAI


def get_client():
    api_key = os.getenv("FEATHERLESS_API_KEY")

    if not api_key:
        return None

    return OpenAI(
        api_key=api_key,
        base_url="https://api.featherless.ai/v1"
    )


def generate_influencers(niche, audience):
    """
    Generates influencer dataset using Featherless API
    """

    client = get_client()

    if client is None:
        print("⚠️ FEATHERLESS_API_KEY not set. Using fallback data.")
        return []

    prompt = f"""
    Generate a list of 6 influencers for a {niche} campaign targeting {audience}.

    Return ONLY valid JSON array with this structure:
    [
      {{
        "name": "string",
        "platform": "Instagram or YouTube",
        "niche": "{niche}",
        "followers": number,
        "engagement": number (5 to 15),
        "audience": "{audience}",
        "cost": number
      }}
    ]
    """

    try:
        response = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct",
            messages=[
                {"role": "system", "content": "You generate realistic influencer datasets."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        content = response.choices[0].message.content.strip()

        # Parse JSON safely
        influencers = json.loads(content)

        return influencers

    except Exception as e:
        print(f"❌ LLM generation failed: {e}")
        return []