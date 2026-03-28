# actions/outreach.py

import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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


def send_email_to_best(influencer, goal, niche):
    """
    Generates an AI email and sends it to the best influencer via Gmail SMTP.

    Requires these env vars:
        GMAIL_SENDER     — your Gmail address (e.g. you@gmail.com)
        GMAIL_APP_PASS   — Gmail App Password (NOT your normal password)

    The influencer dict must include an 'email' field.
    """

    # ── 1. Generate the email body with AI ──────────────────────────────────
    body = generate_email(influencer, goal, niche)

    if body.startswith("❌"):
        return {"success": False, "error": body}

    # ── 2. Read SMTP credentials from env ───────────────────────────────────
    sender     = os.getenv("GMAIL_SENDER")
    app_pass   = os.getenv("GMAIL_APP_PASS")
    recipient  = influencer.get("email")

    if not sender or not app_pass:
        return {"success": False, "error": "❌ GMAIL_SENDER or GMAIL_APP_PASS not set in env"}

    if not recipient:
        return {"success": False, "error": f"❌ No email address found for {influencer['name']}"}

    # ── 3. Build the MIME message ────────────────────────────────────────────
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Collaboration Opportunity with BrandFluence 🚀"
    msg["From"]    = sender
    msg["To"]      = recipient

    msg.attach(MIMEText(body, "plain"))

    # ── 4. Send via Gmail SMTP ───────────────────────────────────────────────
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, app_pass)
            server.sendmail(sender, recipient, msg.as_string())

        print(f"✅ Email sent to {influencer['name']} at {recipient}")
        return {
            "success": True,
            "recipient": recipient,
            "preview": body
        }

    except smtplib.SMTPAuthenticationError:
        return {"success": False, "error": "❌ Gmail auth failed — check GMAIL_SENDER and GMAIL_APP_PASS"}

    except Exception as e:
        return {"success": False, "error": f"❌ SMTP error: {e}"}


def simulate_outreach(influencer):
    """
    Simulates outreach for an influencer.

    Returns:
        dict with status, response_time, accepted
    """
    statuses = ["sent", "seen", "replied"]

    return {
        "status": random.choice(statuses),
        "response_time": random.randint(1, 24),
        "accepted": random.choice([True, False])
    }


if __name__ == "__main__":
    influencer = {
        "name": "PoojaFlex",
        "platform": "YouTube",
        "email": "pooja@example.com"   # ← replace with real email from your data
    }

    result = send_email_to_best(influencer, goal="Brand Awareness", niche="fitness")
    print(result)