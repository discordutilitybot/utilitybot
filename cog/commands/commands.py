import discord
import discord.ext 
from discord.ext import commands
import datetime

# This class represents all the different categorys of commands
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commands.moderation(self, ctx):
        
def setup(bot):
    bot.add_cog(Commands(bot))
    bot.logging.info("Loaded cog Commands")