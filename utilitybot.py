import discord
from discord.ext import commands

import asyncio
import asyncpg
import os

from .plugins.commands import Commands
from .plugins.help import Help
from .plugins.utility import Utility
from .plugins.stats import Stats
from .plugins.mod import Mod


class UtilityBot(commands.Bot):
    """Main file to load all modules"""

    def __init__(self, token, command_prefix):
        self.token = token
        self.command_prefix = command_prefix