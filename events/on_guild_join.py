import discord
from discord.ext import commands
from discord import Guild, User

import asyncpg
import logging

class GuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Add muted role with its permissions and insert guild info into the db"""
        pass




def setup(bot):
    try:
        bot.add_cog(GuildJoin(bot))
        """Ill add logging later so its alot easier to find bugs"""
    
    """exception here (probably a discord exception)"""