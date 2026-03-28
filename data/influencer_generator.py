import random

first_names = [
"Aarav","Vihaan","Arjun","Krishna","Aditya","Rohan","Karan","Rahul","Ishaan","Yash",
"Ananya","Riya","Priya","Sneha","Kavya","Pooja","Meera","Diya","Aisha","Neha",
"Alex","Chris","Jordan","Taylor","Sam","Ryan","Emma","Olivia","Liam","Noah",
"Zara","Ayaan","Reyansh","Tanvi","Ira","Nikhil","Siddharth","Varun","Manav","Dev"
]

tech_suffix = ["Tech","Coder","Dev","AI","Labs","Digital","Byte","X","Hub","Guru"]
fashion_suffix = ["Style","Vibes","Looks","Trend","Closet","Wear","Aura","Fit","Mode","Chic"]
fitness_suffix = ["Fit","Strong","Beast","Flex","Muscle","Train","Power","Core","Gym","Lift"]
food_suffix = ["Eats","Bites","Kitchen","Foodie","Flavours","Tadka","Cravings","Cook","Spice","Meal"]
edu_suffix = ["Study","Academy","Mentor","Learn","Focus","Prep","Notes","Brain","Scholar","Mind"]

def generate_name(niche):
    suffix_map = {
        "tech": tech_suffix,
        "fashion": fashion_suffix,
        "fitness": fitness_suffix,
        "food": food_suffix,
        "education": edu_suffix
    }
    return random.choice(first_names) + random.choice(suffix_map[niche])

def generate_influencer(niche=None):
    niches = ["tech","fashion","fitness","food","education"]
    
    if niche is None:
        niche = random.choice(niches)

    followers = random.randint(1000, 500000)
    engagement = round(random.uniform(1,10),2)

    return {
        "name": generate_name(niche),
        "platform": random.choice(["Instagram","YouTube","Twitter"]),
        "niche": niche,
        "followers": followers,
        "engagement": engagement,
        "audience": random.choice(["students","professionals","general"]),
        "cost": random.randint(500,10000),
        "email": f"{random.randint(1000,9999)}user@gmail.com",
        "reach_score": round(followers * (engagement / 100), 2)  # 🔥 important fix
    }

def generate_influencers(count=200):
    return [generate_influencer() for _ in range(count)]