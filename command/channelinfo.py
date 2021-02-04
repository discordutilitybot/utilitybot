import discord
from discord.ext import commands
import datetime


class Channelinfo(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def channel_info(self, ctx, chan: [discord.TextChannel]):
        channel = chan
        if channel == None:
            channel = ctx.channel
        embed = discord.Embed(
            title = f'Stats for: {channel.name}',
            description = f'List of details about: {channel.name}',
            timestamp=datetime.datetime.utcnow(),
            colour = discord.Colour.blue()
        )
        embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=False)
        embed.add_field(name="Channel Id", value=channel.id, inline=False)
        embed.add_field(name="Channel Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=False)
        embed.add_field(name="Channel Position", value=channel.position, inline=False)
        embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=False)
        embed.add_field(name="Channel is NSFW?", value=channel.is_nsfw(), inline=False)
        embed.add_field(name="Channel is Announcement Channel?", value=channel.is_news(), inline=False)
        embed.add_field(name="Channel Creation Time", value=channel.created_at, inline=False)
        embed.add_field(name="Channel Permissions Synced", value=channel.permissions_synced, inline=False)
        embed.add_field(name = 'Channel ID', value = channel.id)
        embed.add_field(name="Channel Hash", value=hash(channel), inline=False)
        embed.set_thumbnail(url= ctx.guild.icon_url)
        await ctx.send(embed = embed)


def setup(bot):
  bot.add_cog(Channelinfo(bot))
  bot.logging.info("Loaded channelinfo command")
  