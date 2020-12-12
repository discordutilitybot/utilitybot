import discord
from discord.ext import commands

class Servericon(commands.Cog):
    def __init__(self, bot) :
        self.bot = bot
    
def setup(bot):
    bot.add_cog(Servericon(bot))
    bot.logging.info("Loaded Servericon command")