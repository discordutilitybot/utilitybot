import discord
from discord.ext import commands
import asyncio
import os
from config import TOKEN

"""Local modules"""

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