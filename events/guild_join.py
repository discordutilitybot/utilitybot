"""MIT License

Copyright (c) 2020 utilitybot.co

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

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
        
        # Insert global guild data
        self.bot.db.execute("INSERT INTO guilds (guild_id, guild_roles, guild_channels, guild_messages, guild_voice_channels, guild_categorys)")

        # Insert data for guild settings and prefix's..
        self.bot.db.execute(f"INSERT INTO guild_settings (guild_id, muted_role, guild_prefix,  logging_moderation, logging_action, logging_join, greet_message) VALUES ({guild.id}, Muted,")



        
def setup(bot):
    try:
        bot.add_cog(GuildJoin(bot)) 
        bot.logging.info("$GREENLoaded event $CYANGuildJoin")
    except Exception:
        bot.logging.error(
            f'$REDError while loading event $CYAN"GuildJoin"'
        )