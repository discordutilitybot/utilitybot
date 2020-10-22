import discord
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="u!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")




bot.run("NzQyMTk2OTExNTIzNjI3MDY4.XzCmvQ.ihG05KN9rpzO_pTTIKeYP4dN6o4")