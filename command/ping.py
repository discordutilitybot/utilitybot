import discord
from discord.ext import commands

class Latency(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  
  @commands.command(name="ping", aliases=['pong, latency'])
  async def ping(self, ctx):
    pong = round(self.bot.latency * 1000)
    await ctx.send(f":white_check_mark: Pong in {pong}ms")


def setup(bot):
  bot.add_cog(Latency(bot))
  bot.logging.info('Loaded ping command')