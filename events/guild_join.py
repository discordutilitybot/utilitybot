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
       
        permissions = discord.Permissions(send_messages=False, speak=False, read_messages=True)
        await self.bot.create_role(
            name="Muted", 
            reason="Utility bot's Default Muted Role on join. (used for muting)",
            permissions=permissions,
            color=discord.Color.orange())
            

        
    
        
def setp(bot):
    bot.add_cog(GuildJoin(bot))
    """Ill add logging later so its alot easier to find bugs""" 