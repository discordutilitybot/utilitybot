import discord
from discord.ext import commands
from discord import utils
import asyncpg
import asyncio
import re


class Moderation(commands.Cog, name="Mod commands"):

    def __init__(self, bot):
        self.bot = bot


    async def mute(self, ctx, member: discord.Member):
        pass
        
