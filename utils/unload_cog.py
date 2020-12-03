import discord
from discord.ext import commands


def unload_cog(cog_name):
    bot.unload_extension(cog_name)