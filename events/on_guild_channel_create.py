import discord
from discord.ext import commands

class ChannelCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, bot):
        pass

def setup(bot):
    bot.add_cog(ChannelCreate(bot))