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

class Admin(commands.Cog, name="Moderation"):

    def __init__(self, bot):
        self.bot = bot
        self.ban_list = []
        self.day_list = []
        self.server_list = []

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
                await ctx.send('\n-Failed to DM user, user most likely has DMs off.')
            try:
                await ctx.send(embed=embed)
                await target.kick(reason = arg2)
            except:
                await ctx.send('diff\n-Failed to kick member, check for the following:\n\nUtility Bot requires kick permissions\nNot high enough on role hiearchy\n-Member is an admin/mod')
                

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
            await ctx.send('diff\n-Failed to kick member, check for the following:\n\nUtility Bot requires kick permissions\nNot high enough on role hiearchy\n-Member is an admin/mod```')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(ban_members=True)
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
    async def purge(self, ctx, arg: str=None):
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
            title = str(target) +' Has been warned by ' + str(ctx.author),
            description = 'Reason: ' + arg2,
            colour = discord.Colour.orange(),
            timestamp=datetime.datetime.utcnow()
        )
        if target == None:
            await ctx.send('u!warn [member] [reason] (Optional)]')
            pass
        else:
            try:
                await target.send('You were warned in ' + ctx.guild.name),
                await ctx.send(embed=embed)
            except:
                await ctx.send('Failed to DM user :(.')
            
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(mute_members=True)
    async def mute(self, ctx, member: discord.Member = None, length: int = None, *, reason=None):
       guild = ctx.guild
       mutedRole = discord.utils.get(guild.roles, name="Muted")
       if member == None or reason == None:
          await ctx.send('```All parameters required | c!mute [member] [time in seconds)] [reason]```')
          pass
       else:
          if not mutedRole:
            await ctx.send('```Create a muted role named `Muted`!```')
            pass
          else:
            try:  
              await member.add_roles(mutedRole, reason=reason)
              await ctx.send(f"```Muted {member} for reason: {reason}\nMute Length: {length} seconds\nMute Command executed by: {ctx.author}```")
              try:
                await member.send(f"```You were muted in the server {guild.name} for {reason}\nMute Command executed by: {ctx.author}\nMute Length: {length} seconds```")
              except:
                await ctx.send('```diff\n-Failed to dm user```')  
            except:
              await ctx.send('```diff\n- Failed to mute member, check for the following:\n\n- Mute role not created\n- Member is a moderator/administrator\n- I do not have manage roles permissions```')
            
          
            if ctx.guild.id == 751476973477560412:
              updates = ctx.guild.get_channel(785572711300464691)
              updates2 = ctx.guild.get_channel(797220475071496192)
              await updates.send(f'{member.mention} got sent to the **Shadow Realm**. ')
              await updates2.send(f'-------------------------------------------------------------------------------------------------------\nOh hi {member.mention}, looks like you got muted and sent to the shadow realm.... Sucks doesnt it?\n\nMaybe next time you should learn to behave and not act like a :clown:\n\nAnyway, enjoy your time in this dark place, and make sure react to your reason in #mute-reason')
            try:
              await asyncio.sleep(length)
              await member.remove_roles(mutedRole)
              await ctx.send(f'```{member} has been unmuted.\nMute command executed by: {ctx.author}\nMute Length: {length} seconds```')
              if ctx.guild.id == 751476973477560412:
                 updates = ctx.guild.get_channel(756608398501347434)
                 await updates.send(f'{member} got released from the **Shadow Realm**')
            except:
              await ctx.send('```diff\n- Failed to unmute member, check for the following:\n\n- Mute role not created\n- Member is a moderator/administrator\n- I do not have manage roles permissions```')
    
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, member: discord.Member=None):
        if member == None:
          await ctx.send('```All parameters required | c!unmute [member]```')
        else:
          try:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.remove_roles(mutedRole)
            await ctx.send(f"Unmuted {member.mention}")
          except:
            await ctx.send('')  
          try:
            await member.send(f"You were unmuted in the server {ctx.guild.name}")
          except:
            await ctx.send('Failed to DM user :(.')

    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(manage_nicknames = True)
    async def nick(self, ctx, user: [Member], * , name: str = None):
        if name == None:
          await ctx.send('Specify a name to change! | Example: u!nick [Member (optional)] [name]')
        else:
          try:
            user == user or ctx.author
            await user.edit(nick = name)
            await ctx.send('Nickname changed for ' + str(user) + '.\nCurrent Name: ' + name + '')
          except:
            await ctx.send('\n-Failed to change users nickname.\nCheck if I have manage nicknames permissions or if the user is a higher rank than me.')

def setup(bot):
    bot.add_cog(Admin(bot))
    bot.logging.info('Loaded Admin cog!')