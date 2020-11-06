import discord
from discord.ext import commands

class GuildVoice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(GuildVoice(bot))
    bot.logging.info("$GREENLoaded event $CYANGuildVoice")