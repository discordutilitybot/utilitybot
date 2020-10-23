import discord
from discord.ext import commands
from utilitybot import Utilitybot
from discord import Status, Playing
import asyncio
import asyncpg
import dotenv

bot = Utilitybot(
    command_prefix="u!",
    status=discord.Status.dnd,
    activity=(name=Playing("Among us")),
)