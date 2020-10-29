import discord
from discord.ext import commands

import utilitybot
from utilitybot import Utilitybot

import logging
import datetime
import asyncpg
import asyncio

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

for ext in extensions:
    bot.load_extension(ext)

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='utilitybot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
bot.run("NzQyMTk2OTExNTIzNjI3MDY4.XzCmvQ.S5f")