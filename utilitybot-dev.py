import discord
import os
from discord.ext import commands

import secrets
from secrets import *

bot = commands.Bot(command_prefix="u!")

bot.remove_cog('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")



bot.run(token)
