from actions.outreach import generate_outreach_message, simulate_outreach

inf = {
    "name": "TechGuru",
    "platform": "Instagram"
}

msg = generate_outreach_message(inf, "Mass Awareness", "tech")
print(msg)

result = simulate_outreach(inf)
print(result)