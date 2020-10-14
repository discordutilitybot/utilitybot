import discord
from discord.ext import commands
from discord import utils
import asyncpg



class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

def setup(bot):
    bot.add_cog(Utility(bot))