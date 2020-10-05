import discord
from discord.ext import commands

"""Link to the github repo."""   
class GuildInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    


def setup(bot):
    bot.add_cog(GuildInfo(bot))