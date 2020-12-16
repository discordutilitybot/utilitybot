import discord
from discord.ext import commands


class Hooks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Hooks(bot))
    bot.logging.info("Loaded util hooks")