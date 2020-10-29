import discord
from discord.ext import commands

 
class GuildInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    """Simple guildinfo command to check amount of roles, server_id and more."""
    @commands.command()
    async def guildinfo(self, ctx):
        pass

    


def setup(bot):
    bot.add_cog(GuildInfo(bot))