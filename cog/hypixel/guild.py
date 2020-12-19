import discord
from discord.ext import commands
import datetime
import aiohttp

class Guild(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="guild", aliases=['g'])
  async def guild(self, ctx, user: str = None):
    channel = ctx.author.channel
    color = ctx.author.color
    async with channel.typing():
      async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.slothpixel.me/api/guilds/{user}') as resp:
          user == await resp.json()

        if "error" in user:
          embed = discord.Embed(title=f"{user} is not in a Guild", colour=color, timestamp=datetime.datetime.utcnow())
          await ctx.send(embed=embed)
        else:
          embed = discord.Embed(title=f"{user} Guild", colour=color, timestamp=datetime.datetime.utcnow())
          embed.add_field(name="Guild name:", value=user["name"], inline=False)
          embed.add_field(name="Guild tag:", value=user["tag"], inline=False)
          embed.add_field(name="Guild level:", value=user["level"], inline=False)
          embed.add_field(name="Guild legacy ranking:", value=user["legacy_ranking"], inline=False)
          embed.add_field(name="Guild description:", value=user["description"], inline=False)
          await ctx.send(embed=embed)

def setup(bot):     
    bot.add_cog(Guild(bot))
    bot.logging.info('Loaded cog Guild')