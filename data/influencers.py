# data/influencers.py

from data.influencer_generator import generate_influencers


def get_influencers(count=50, niche=None, audience=None):
    return generate_influencers(count, niche=niche, audience=audience)