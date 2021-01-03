import discord
from discord.ext import commands


class Modlogcheck:
  pass

class Modlog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def modlog(self, ctx, channel: discord.TextChannel):
      await ctx.send(f"Configuring modlog channel to #{channel}", delete_after=3)

      await self.bot.db
def setup(bot):
  bot.add_cog(Modlog(bot))