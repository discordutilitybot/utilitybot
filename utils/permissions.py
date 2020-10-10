import discord
from discord.ext import commands
from discord.utils import get

"""Simple function to check whether the bot has permissions to perform events or actions."""
def has_permission(permission : str, **kwargs):
    def predicate(ctx):
        if ctx.bot.has_permission(ctx.author, permission):
            return True
        else:
            return commands.has_permissions(**kwargs)

        return commands.check(predicate)