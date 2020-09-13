import discord
from discord.ext import commands
import asyncio
import os
from config import TOKEN

"""Local modules"""
from plugins.commands import Commands
from plugins.help import Help
from plugins.utility import Utility
from plugins.stats import Stats
from plugins.mod import Mod

from plugins.database.database import Database
from plugins.database.message import Message
from plugins.database.server import Server
from plugins.database.user import User

bot = commands.Bot(command_prefix="u!")

cogs = [
    "cogs.avatar"
    "cogs.games"
    "cogs.guildinfo"
    "cogs.help"
    "cogs.mod"
    "cogs.utility"
]



bot.run(TOKEN)