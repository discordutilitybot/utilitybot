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
        """Make sure to add muted role before any calls are made to the DB."""

    
        

def setup(bot):
    bot.add_cog(GuildJoin(bot))
    """Ill add logging later so its alot easier to find bugs"""