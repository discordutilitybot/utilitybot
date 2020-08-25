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

from .plugins.database.user import User
from .plugins.database.server import Server
from .plugins.database.message import message
from .plugins.database.bot import Bot

class UtilityBot(commands.Bot):
    """Main file to load all modules"""

    def __init__(self, token, command_prefix):
        self.token = token
        self.command_prefix = command_prefix
