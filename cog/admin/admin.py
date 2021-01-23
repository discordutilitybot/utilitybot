import discord
from discord.ext import commands
from discord import utils
from discord import TextChannel, Member
from discord import Role
from discord.ext import tasks
import asyncpg
import asyncio
import re
import datetime
from discord import Member, TextChannel, Role

class StaffCheck(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await Member().convert(ctx, argument)
        if type(argument) != discord.Member:
            return False
        if argument.top_role.position >= ctx.guild.me.top_role.position:
            try:
                await ctx.send(
                    "You cannot punish someone with a role higher than or equal to mine :("
                )
            except Exception:
                return False

# Check if a staff has a message (manage_message)      
class StaffCheckNoMessage(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await Member().convert(ctx, argument)
        permission = argument.guild_permissions.manage_nessages
        if ctx.author.id == ctx.author.id and argument.id == ctx.author.id:
            return argument
        if not permission: 
            return argument
        else: 
            return False

class Moderation(commands.Cog, name="Moderation"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target : discord.Member = None, *, arg: str = None):
        arg2 = arg or 'No reason provided'
        embed = discord.Embed(
            title = str(target) + ' was kicked from ' + ctx.guild.name,
            description = 'Reason: ' + arg2,
            colour = discord.Colour.orange(),
            timestamp=datetime.datetime.utcnow()
        )
        embed2 = discord.Embed(
            title = 'You were kicked from' + ctx.guild.name,
            description = 'Reason' + arg2,
            colour = discord.Colour.orange(),
            timestamp=datetime.datetime.utcnow()
        )

        if target == None:
            await ctx.send('u!kick [member] [reason (Optional)]')
        else:
            try:
                await target.send(embed=embed2)
            except:
                await ctx.send('diff\n-Failed to DM user, user most likely has DMs off.')
            try:
                await ctx.send(embed=embed)
                await target.kick(reason = arg2)
            except:
                await ctx.send('```diff\n-Failed to kick member, check for the following:\n\nUtility Bot requires kick permissions\nNot high enough on role hiearchy\n-Member is an admin/mod```')
                

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, target: discord.Member = None, *, arg: str = None):
        arg2 = arg or 'No reason provided'
        embed = discord.Embed(
            title = str(target)  ' was kicked from ' + ctx.guild.name,
            description='Reason: ' + arg2,
            colour = discord.Colour.orange(),
            timestamp=datetime.datetime.utcnow()
        ) 
        embed2 = discord.Embed(
            title= 'You wer kicked from ' + ctx.guild.name,
            description='Reason' + arg2,
            colour=discord.Colour.orange(),
            timestamp=datetime.datetime.utcnow()
        )

        if target == None:
            await ctx.send('u!kick [member] [reason (Optional)]')
        else:
            try:
                await target.send(embed=embed2)
        except:
            await ctx.send('diff\n-Failed to DM user, user most likely has DMs off.')
        try:
            await ctx.send(embed=embed)
            await target.kick(reason=arg2)
        except:
            await ctx.send('```diff\n-Failed to kick member, check for the following:\n\nUtility Bot requires kick permissions\nNot high enough on role hiearchy\n-Member is an admin/mod```')
            
def setup(bot):
    bot.add_cog(Moderation(bot))
    bot.logging.info('Loaded moderation cog!')