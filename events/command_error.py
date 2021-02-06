"""MIT License

Copyright (c) 2020 utilitybot.co

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import discord
from discord.ext import commands
from discord import Guild

import datetime
import logging
from logging import log

import aiohttp
import random
import os


class Commanderror(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
            
        """checks the discord errors vs the python exceptions/errors and returns true if there is none"""
        if hasattr(ctx.command, "on_error"):
            return

        if isinstance(error, commands.CommandNotFound):
            return await ctx.send('Command not found, there may be a typo in the command.')
       
        if isinstance(error, commands.NoPrivateMessage):
            return await ctx.send("You cannot use commands in a private message please go to a server to run commands.")
        
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send("You dont have the permissions to perform this command")
            
        if isinstance(error, commands.BotMissingPermissions):
            return await ctx.send("You dont have the permissions to perform this command")

        if isinstance(error, commands.NoPrivateMessage):
            return await ctx.send("You can't run this command here!")

        if isinstance(error, commands.CommandNotFound):
            return await ctx.send(f"Command not found! :( Please try again")
def setup(bot):

    bot.add_cog(Commanderror(bot))
    bot.logging.info("Loaded event CommandError")

    