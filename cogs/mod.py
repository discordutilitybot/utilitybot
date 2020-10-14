import discord
from discord.ext import commands
from discord import utils
import asyncpg
import asyncio
import re


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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

    @commands.command(aliases=["silence, stfu"])
    async def mute(self, ctx, member: discord.Member, reason=None):
        pass

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        pass

    """Set the muted default muted role by utility bot to a custom one."""
    @commands.command()
    async def mutedrole(self, ctx, role_id: int):
        pass
    
    
    @commands.command()
    async def warn(self, ctx, member: discord.Member, reason=None):
        await ctx.send(f"{member.mention} was warned for {reason}")

        for reasons in reason:
            if not reasons:

                await ctx.send(f"Please provide a reason to warn a {member}")

            else:
                return True
        
        for members in member:
            if not members:
                await ctx.send(f"Please specify a member to warn {member.mention}")
            else:
                return Truediscor

def setup(bot):
    bot.add_cog(Moderation(bot))