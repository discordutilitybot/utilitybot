import discord
from discord.ext import commands
import datetime
import aiohttp
import random
import os
import re

# Local modules


class on_command_error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        # Make sure it doenst confuse local python errors/ handlers with discord errors
        if hasattr(ctx.command, "on_error"):
            return
        
        if isinstance(error, commands.CommandNotFound):
            await ctx.error('Command not found, there may be a typo in the command.')

        if isinstance(error, commands.NoPrivateMessage):
            await ctx.error("You cannot use commands in a dm.")
        
        if isinstance(error, commands.MissingPermissions):
            ctx.error("You are missing the permissions to use this command.")

        if isinstance(error, commands.BotMissingPermissions):
            await ctx.error("I am missing permissions to perform this command :(.")