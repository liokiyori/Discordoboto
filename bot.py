import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv('Discord_token')
client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot is ready.')
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')    

client.run(discord_token)