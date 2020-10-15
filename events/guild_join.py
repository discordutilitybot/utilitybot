import discord
from discord.ext import commands
from discord import Guild, User
from discord.utils import get

import asyncpg
import logging



class GuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Make the default muted role Utility Bot uses before making calls to the db"""
        permissions = discord.Permissions(send_messages=False, speak=False, read_messages=True)
        await self.bot.create_role(name="Muted", permissions=permissions)

    
        
def setup(bot):
    bot.add_cog(GuildJoin(bot))
    """Ill add logging later so its alot easier to find bugs""" 