import discord
from discord.ext import commands
from discord.utils import get

class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botinfo(self, ctx)    

def setup(bot):
    bot.add_cog(Botinfo(bot))