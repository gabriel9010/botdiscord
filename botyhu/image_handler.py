import discord

async def get_profile_image(user):
    profile_image = user.avatar_url
    return profile_image