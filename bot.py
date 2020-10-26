import discord
from discord.ext import commands
from utilitybot import Utilitybot
from discord.ext import *
import asyncio
import asyncpg
import dotenv
import utils
import datetime
from utils.permissions import has_permission

bot = Utilitybot(
    command_prefix="u!",
    status=discord.Status.dnd,
    activity= discord.Game(name="Vibing", type=3),
    case_insensitive=True,
    owner_id=388788632686690305
)

# Remove default help command in discord.py
bot.remove_command('help')
extensions = [
    "commands.avatar"
    "commands.botinfo"
    "commands.help"
    "commands.github"
    "commands.invite"
]
for e in extensions:
    bot.load_extension(e)

bot.run("w")