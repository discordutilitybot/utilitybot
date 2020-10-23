import discord
from discord.ext import commands
from utilitybot import Utilitybot
from discord.ext import *
import asyncio
import asyncpg
import dotenv
import utils
from utils.permissions import has_permission

bot = Utilitybot(
    command_prefix="u!",
    status=discord.Status.dnd,
    activity= discord.Game(name="Vibing", type=3),
    case_insensitive=True,
    owner_id=388788632686690305
)

bot.remove_command('help')
extensions = [
    "cogs.help",
    "cogs.botinfo",
    "cogs.conf",
    "cogs.avatar",
    "cogs.github",
    "cogs.guildinfo",
    "cogs.hypixel",
    "cogs.moderation",
    "cogs.utilitys"
]