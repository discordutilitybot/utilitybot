import discord
from discord.ext import commands

# Check all the permissions of the botand return true if it has the permissimon (we can pass through as many arguments because **kwargs lets us pass through any number of arguments)
def has_permission(permission : str, **kwargs):
    def predicate(ctx):
        if ctx.bot.has_permission(ctx.author, permission):
            return True
        else:
            return commands.has_permissions(**kwargs)

        return commands.check(predicate)