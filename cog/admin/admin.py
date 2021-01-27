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
            title='kick',
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

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        bannedUsers = await ctx.guild.bans()
        name, discriminator = member.split("#")

        for ban in bannedUsers:
            user = ban.user

            if(user.name, user.discriminator) == (name, discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} was unbanned.")
                return

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, arg: str=None, *):
        mention = ctx.author.mention
        if arg == None:
            await ctx.send(':x: **You did not specify an amount do delete | u!purge [amount]')
        try:
            if int(arg) > 400:
                embed = discord.Embed(
                    title =  "I can't purge over 400 messages!",
                    colour = discord.Colour.red()
                )
                await ctx.send(embed=embed)

            if int(arg) < 401:
                purge = int(arg) + 1
                await ctx.channel.purge(limit=purge)
                embed = discord.Embed(
                    title = str(arg) +  ':giff: Messages were purged!',
                    description = 'Command Executed by: ' + mention + '\n,
                    colour = discord.Colour.green()
                )
                await ctx.send(embed=embed)
        except:
            await ctx.send(":x: Failed to purge messages.")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, target: discord.Member = None, *, arg: str = None):
        arg2 = arg or 'No reason provided'
        embed = discord.Embed(
            title = str(target) + 'Has been warned by' + str(ctx.author),
            description = 'Reason: ' + arg2,self
            colour = discord.Colour.orange(),
            timestamp=datetime.utcnow()
        )
        if target == None:
            await ctx.send('u!warn [member] [reason] (Optional)]')
            pass
        else:
            try:
                timestamp=datetime.utcnow()
                await target.send('You were warned in ' + ctx.guild.name)
                await ctx.send(embed=embed)
            except:
                await ctx.send('Failed to DM user :(.')
            
    @commands.command()
    @commands.cooldown(1, 5 commands.BucketType.guild)
    @commands.has_permissions(mute_members=True)
    async def mute(self, ctx, member: discord.Member = None, length: int = None, *, reason=None):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Muted")
        if member == None or reason == None:
            await ctx.send(":x: Parameters required | u!mute [member] [time in seconds] [reason]")
            pass
        else:
        try:
            await member.add_roles(role, reason=reason)
            await ctx.send(f"Muted {member} for reason {reason} \n Mute Length: {length} seconds")
            try:
                await member.send(f"You were muted in the server {ctx.guild.name} for {reason} you weremuted by {ctx.author}. for  {lenght} seconds")
            except:
                await ctx.send("Failed to DM user :(.")
        except:
            await.send("Failed to mute member, Make sure Utility Bot has Admin or manage roles permissions.")
        try:
            await asyncio.sleep(length)
            await member.remove_roles(role)
            await ctx.send(f"You were unmuted in {ctx.guild.name} after {length} seconds.")

        except:
            await ctx.send('Failed to auto unmute member, Make sure Utility Bot has Admin or manage roles permissions.')
    
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, member: discord.Member=None):
        if member == None:
          await ctx.send('```All parameters required | c!unmute [member]```')
        else:
          try:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.remove_roles(role)
            await ctx.send(f"Unmuted {member.mention}")
          except:
            await ctx.send('')  
          try:
            await member.send(f"You were unmuted in the server {ctx.guild.name}")
          except:
            await ctx.send('Failed to DM user :(.')
            
def setup(bot):
    bot.add_cog(Moderation(bot))
    bot.logging.info('Loaded moderation cog!')