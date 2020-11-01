import discord
from discord.ext import commands
from discord import utils
from discord import TextChannel, Member
from discord import Role
import asyncpg
import asyncio
import re
#from .utils import *
#from .utils.permissions import permissions

class Moderation(commands.Cog, name="Moderation"):

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.command(aliases=["banish," "begone", "perish"])
    async def ban(
    
    self, 
    ctx,   # Not sure if i should use discord.member or discord.User i believe discord.User is global and member is guild wise?
    member: discord.Member,
    reason=None,
    modlogs: TextChannel = None


    ):

        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned for {reason}.")

        if not member:
            await ctx.send("You must specify a user.")


    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(
        self, 
        ctx, 
        member: discord.Member, 
        reason=None, 
        modlogs: TextChannel = None
    ):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked for {reason}")

        for reasons in reason:
            if not reasons:
                await ctx.send(f"Please specify a reason to ban {member}.")

        for members in member:
            if not members:
                await ctx.send(f"Pleasy specify a member to ban {member.mention}")

    @commands.has_permissions(mute_members=True)
    @commands.command(aliases=["silence, stfu"])
    async def mute(self, ctx, member: discord.Member, reason=None, modlogs: TextChannel = None):

        if not member:
            await ctx.send(f"You need to specify a user to mute {member.mention}")

        if not reason:
            await ctx.send(f"You need to specify reason to mute {member.mention}")
        
        query = """SELECT muted_role FROM guild_settings WHERE id = ?"""
        muted = self.bot.db.execute(query, ctx.guild.id) or discord.utils.get(
            # Default muted role created by utiilitybot
            #ctx.guild.roles, name="Muted"
        )
        
    
    @commands.has_permissions(mute_members=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member, modlogs: TextChannel = None):
        pass

    """Set the muted default muted role by utility bot to a custom one."""
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mutedrole(self, ctx, role: discord.Role,):
        pass
        
    
    
    @commands.command()
    async def warn(
        self, 
        ctx,
        member: discord.Member,
        reason="No reason specified", 
        modlogs: TextChannel = None
    ):
        
        await ctx.send(f"{member.mention} was warned for {reason}")

        """Error Handlers"""
        if not member:
            await ctx.send("You have specify a member to warn")
            
        if len(reason) > 250:
            await ctx.send("Reason's have to be less than 250 characters.")

        if ctx.author.id != ctx.guild.owner.id:
            await ctx.send("You can't warn the Owner of the Server!")

        if ctx.author == member:
            await ctx.send("You can't wwarn your self.")
            
        
        # Update warnings for the user in db

def setup(bot):
    bot.add_cog(Moderation(bot))
    bot.logger.info('$GREENLoaded $BLUE"moderation" $GREENcog!')