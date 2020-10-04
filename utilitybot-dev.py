import discord

from discord.ext import commands

import secrets
from secrets import *

bot = commands.Bot(command_prefix="u!")

extensions = ('cogs.github', 'cogs.help')


for ext in extensions:
    bot.load_extension(extensions)

bot.run(token)
