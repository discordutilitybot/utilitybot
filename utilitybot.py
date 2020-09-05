import discord
from discord.ext import commands

import asyncio
import asyncpg
import os

"""Local modules"""
from .plugins.commands import Commands
from .plugins.help import Help
from .plugins.utility import Utility
from .plugins.stats import Stats
from .plugins.mod import Mod

from .plugins.database.database import Database
from .plugins.database.message import Message
from .plugins.database.server import Server
from .plugins.database.user import User


class UtilityBot(commands.Bot):
    """Main file to load all modules"""

    def __init__(self, token, command_prefix):
        pass