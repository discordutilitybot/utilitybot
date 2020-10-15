import discord
from discord.ext import commands
from discord import utils
import asyncpg
import asyncio
import re


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(mute_members=True)
    @commands.command
    async def ban(self, ctx, member: discord.Member, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned for {reason}.")

        for reasons in reason:
            if reasons is None:
                await ctx.send(f"Please specify a reason to ban {member}.")

        for members in member:
            if members is None:
                await ctx.send(f"Pleasy specify a member to ban {member.mention}")

    @commands.has_permissions(mute_members=True)
    @commands.command(aliases=["silence, stfu"])
    async def mute(self, ctx, member: discord.Member, reason=None):
        pass
    
    @commands.has_permissions(mute_members=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        pass

    """Set the muted default muted role by utility bot to a custom one."""
    @commands.has_permissions(manage_server=True)
    @commands.command()
    async def mutedrole(self, ctx, role_id: int):
        pass
    
    
    @commands.command()
    async def warn(self, ctx, member: discord.Member, reason=None):
        
        await ctx.send(f"{member.mention} was warned for {reason}")

        if not member:
            await ctx.send("You have specify a member to warn")
            return

        if len(reason) > 250:
            await ctx.send("Reason's have to be less than 250 characters.")
            return

        if ctx.author.id != ctx.guild.owner.id:
            await ctx.send("You can't warn the Owner of the Server!")
            return

        if ctx.author == member:
            await ctx.send("You can't wwarn your self.")
            return

def setup(bot):
    bot.add_cog(Moderation(bot))