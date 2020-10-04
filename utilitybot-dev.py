import discord

from discord.ext.commands import commands
import secrets
from secrets import *
bot = commands.Bot(command_prefix="u!")
cogs = [
    'cogs.github',
    'cogs.help'
]

bot.run(token)