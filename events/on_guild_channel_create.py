import discord
from discord.ext import commands

class ChannelCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

def setup(bot):
    bot.add_cog(ChannelCreate(bot))