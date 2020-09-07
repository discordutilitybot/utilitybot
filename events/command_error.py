import discord
from discord.ext import commands
from discord import Guild
import datetime
import aiohttp
import logging
from logging import log
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
       
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("You cannot use commands in a private message please go to a server to run commands.")
        
        if isinstance(error, commands.MissingPermissions):
            for roles in ctx.guild.roles:
                if roles == True:
                    await ctx.send("You dont have the permissions to perform this command")
                else:
                    return False
            
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I am missing permissions to perform this command :(.")

        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("You need to run this command in a server for it to work")

        if isinstance(error, commands.CommandOnCooldown):
            td = datetime.timedelta(seconds=error.retry_after)
            await ctx.send(f"This command is on cooldown please wait {td.format_timespan(td)}", delete_after=5)

        """Probably wont need this since the commands wont be NSFW."""
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send("You need to use this command in a NSFW channel.")
        
        

    
"""Add the cog"""
def setup(bot):
    bot.add_cog(Commanderror(bot))
    