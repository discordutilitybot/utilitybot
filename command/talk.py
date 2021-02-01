import discord
from discord.ext import commands

class Talk(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def talk(self, ctx, delete, *, text):
    if delete == 'y':
      await ctx.channel.purge(limit=1)
      await ctx.send(text)
    if delete == 'n':
      await ctx.send(text)

def setup(bot):
  bot.add_cog(Talk(bot))
  bot.logging.info("Loaded talk command")
    