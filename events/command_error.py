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
            """Check if the user has the right permissions if they dont return the error if they do then return true"""
            for roles in ctx.guild.permissions:
                if roles == False:
                    await ctx.send("You dont have the permissions to perform this command")
                else:
                    return True
            
        if isinstance(error, commands.BotMissingPermissions):
           for roles in ctx.bot.permissions:
               

        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("You need to run this command in a server for it to work")

        if isinstance(error, commands.CommandOnCooldown):
            td = datetime.timedelta(seconds=error.retry_after)
            await ctx.send(f"This command is on cooldown please wait {td.format_timespan(td)}", delete_after=5)

        """Probably wont need this since the commands wont be NSFW. yuck."""
        if isinstance(error, commands.NSFWChannelRequired):
                await ctx.send("You need to have a NSFW channel to use this command")
            
        
        


"""Add the cog"""
def setup(bot):
    bot.add_cog(Commanderror(bot))
    