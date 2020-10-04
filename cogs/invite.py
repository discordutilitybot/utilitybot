"""Invite Link for the bot"""
import discord
from discord.ext import commands


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['inv, botinvite'])
    async def invite(self, *, ctx, bot):
        await ctx.send("Here is the invite link for utilitybot: ")