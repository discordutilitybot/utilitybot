"""Invite Link for the bot"""
import discord
from discord.ext import commands
import logging


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['inv, botinvite'])
    async def invite(self, ctx):
        await ctx.send("Here is the invite link for utilitybot: \n")

def setup(bot):
    bot.add_cog(Invite(bot))
    bot.logger.info(f'$GREENLoaded $BLUE"invite" $GREENcommand!')
