import discord
from discord.ext import commands
import datetime
import aiohttp
import random
import os
import re

# Local modules


class Commanderror(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
            
        """checks the discord errors vs the python exceptions/errors and returns true if there is none"""
        if hasattr(ctx.command, "on_error"):
            return

        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found, there may be a typo in the command.')
        """Not sure if the bot can actually respond to commands in dm so this may not be needed"""
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("You cannot use commands in a dm.")
        
        if isinstance(error, commands.MissingPermissions):
            ctx.send("You are missing the permissions to use this command.")

        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I am missing permissions to perform this command :(.")

        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("You need to run this command in a server for it to work")

        if isinstance(error, commands.CommandOnCooldown):
            td = datetime.timedelta(seconds=error.retry_after)
            await ctx.send(f"This command is on cooldown please wait {humanfriendly.format_timespan(td)}"", delete_after=5)


    
def setup(bot):
    bot.add_cog(Commanderror(bot))
    