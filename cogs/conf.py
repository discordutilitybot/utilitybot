"""This is used to check your guilds config settings these are not config commands."""
import discord
from discord.ext import commands
from discord.utils import get
class Conf(commands.Cog):
    def ___init__(self, bot):
    self.bot = bot



def setup(bot):
    bot.add_cog(Conf)