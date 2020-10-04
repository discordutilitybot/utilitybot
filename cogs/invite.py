"""Invite Link for the bot"""
import discord
from discord.ext import commands
from utilitybot import db 

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    


    @commands.command()
    async def invite(self, *, bot):
        await ctx.send("Here is the invite link for utilitybot:")