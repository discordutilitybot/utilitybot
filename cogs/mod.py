import discord
from discord.ext import commands
from discord.ext.errors import *
import asyncpg
import asyncio
import re


class Moderation(commands.Cog, name="Mod commands"):
    """commands used to moderatore your guild"""

    def __init__(self, bot):
        self.bot