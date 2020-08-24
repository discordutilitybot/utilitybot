import discord
from discord.ext import commands

import asyncio
import asyncpg
import os

from logging import log


class UtilityBot(commands.Bot):
    """"This is the main class which subclasses 
    from commands.Bot so we can load all the modules/cogs"""

    def __init__(self, token, command_prefix):
        self.token = token
        self.command_prefix = command_prefix