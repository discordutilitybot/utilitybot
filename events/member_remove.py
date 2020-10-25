import discord
from discord.ext import commands

class MemberRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(MemberRemove(bot))