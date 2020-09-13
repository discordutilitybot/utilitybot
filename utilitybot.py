import discord
from discord.ext import commands
import asyncio
import os
from config import TOKEN

"""Local modules"""
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
    "events.command_error"
    "events.command_error"
]

for cog in cogs:
    bot.load_extension(cog)


bot.run(TOKEN)