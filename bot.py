import discord
from discord.ext import commands
from utilitybot import Utilitybot
from discord.ext import *
import asyncio
import asyncpg
import dotenv

bot = Utilitybot(
    command_prefix="u!",
    status=discord.Status.dnd,
    activity= discord.Game(name="Vibing", type=3)
)