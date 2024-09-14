import random
import discord
from discord.ext import commands

class minigames(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
    
    @commands.command(aliases=["pierre","feuille","ciseaux"])
    async def pfc(self,ctx,choice):
        choices = ["pierre","feuille","ciseaux"]
        bot_choice = random.choice(choices)
        if choice == bot_choice:
            await ctx.send(f"J'ai choisi {bot_choice}, c'est un match nul!")
        elif choice == "pierre":
            if bot_choice == "feuille":
                await ctx.send(f"J'ai choisi {bot_choice}, j'ai gagné!")
            else:
                await ctx.send(f"J'ai choisi {bot_choice}, tu as gagné!")
        elif choice == "feuille":
            if bot_choice == "ciseaux":
                await ctx.send(f"J'ai choisi {bot_choice}, j'ai gagné!")
            else:
                await ctx.send(f"J'ai choisi {bot_choice}, tu as gagné!")
        elif choice == "ciseaux":
            if bot_choice == "pierre":
                await ctx.send(f"J'ai choisi {bot_choice}, j'ai gagné!")
            else:
                await ctx.send(f"J'ai choisi {bot_choice}, tu as gagné!")
        else:
            await ctx.send("Choisis entre pierre, feuille ou ciseaux!")

async def setup(bot):
    await bot.add_cog(minigames(bot))
    print("Minigames cog loaded.")