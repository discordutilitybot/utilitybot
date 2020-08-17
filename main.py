import discord
from discord.ext import commands

import asyncio
import asyncpg
import os

bot = commands.Bot(command_prefix="-u")

bot.run("token")