import discord
from discord.ext import commands
import datetime
class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['guildinfo, ginfo, serverinfo'])
    async def server_info(self, ctx):
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                                                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					                                len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					                                len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))] 
        
        embed = discord.Embed(
            title = 'Server Stats',
            description = f'Stats for Guild: {ctx.guild.name}',
            colour=discord.Colour.blue()
           
        )
        embed.add_field(name = 'Owner:', value = ctx.guild.owner)
        embed.add_field(name = 'Server ID:', value = ctx.guild.id)
        embed.add_field(name = 'Region:', value = ctx.guild.region)
        embed.add_field(name = 'Total Members:', value = len(ctx.guild.members))
        embed.add_field(name = 'Humans:', value = len(list(filter(lambda m: not m.bot, ctx.guild.members))))
        embed.add_field(name = 'Bots:', value = len(list(filter(lambda m: m.bot, ctx.guild.members))))
        embed.add_field(name = 'Banned Members:', value = len(await ctx.guild.bans()))
        embed.add_field(name = 'Statuses:', value =  f"🟢 {statuses[0]} :yellow_circle: {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}")
        embed.add_field(name = 'Categories:', value = len(ctx.guild.categories))
        embed.add_field(name = 'Channels:', value = len(ctx.guild.text_channels) + len(ctx.guild.voice_channels))
        embed.add_field(name = 'Text Channels:', value = len(ctx.guild.text_channels))
        embed.add_field(name = 'Voice Channels:', value = len(ctx.guild.voice_channels))
        embed.add_field(name = 'Roles:', value = len(ctx.guild.roles))
        embed.add_field(name = 'Invites:', value =  len(await ctx.guild.invites()))
        embed.add_field(name = 'Moderators', value = len([i for i in ctx.guild.members if i.guild_permissions.administrator]))
        embed.add_field(name = 'Server Created At:', value = ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"))
        embed.set_thumbnail(url= ctx.guild.icon_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Serverinfo(bot))
    bot.logging.info("Loaded serverinfo command")