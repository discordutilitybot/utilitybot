import discord
from discord.ext import commands
import datetime


class Bedwars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Bedwars(bot))
    bot.logging.info("Loaded bedwars command!")