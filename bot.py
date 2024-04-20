import discord
from discord.ext import commands
from review_handler import ReviewHandler

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
review_handler = ReviewHandler()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    with open('data/token.txt', 'r') as file:
        token = file.read().strip()
    bot.run(token)

@bot.command()
async def review(ctx, stars: int, *, text):
    review_handler.add_review(ctx.author.id, stars, text)
    await ctx.send('Review added successfully!')