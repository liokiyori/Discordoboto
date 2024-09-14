import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
from cogs.minigames import minigames


load_dotenv()

discord_token = os.getenv('Discord_token')
client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

async def change_status():
    await client.change_presence(activity=discord.Game(name="!help"))

@client.event
async def on_ready():
    print('Bot is ready.')
    await change_status()
    await client.load_extension('cogs.minigames')

@client.command(aliases=["pang","pung"])
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')    

@client.command(aliases=["nique", "nique ta mère"])
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


client.run(discord_token)