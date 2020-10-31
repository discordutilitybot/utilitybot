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
    activity= discord.Game(name="utilitybot.co | u!help", type=3),
    case_insensitive=True,
    owner_id=388788632686690305
)

# Remove default help command in discord.py
bot.remove_command('help')

bot.load_extension("commands.invite.py")

logger = logging.basicConfig(filename='utilitybot.log', level=logging.INFO)

bot.run("token")
logger.info("Yes")