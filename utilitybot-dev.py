import discord
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="u!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")




bot.run("NzQyMTk2OTExNTIzNjI3MDY4.XzCmvQ.dYfTinQk5c5jFa5hkfbpYDmQqGk")
