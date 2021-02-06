import discord
from discord.ext import commands

# extremely unnecessary
def unload_cog(cog_name):
    bot.unload_extension(cog_name)