import dbl
import discord
from discord.ext import commands

class TopGG(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.token =  ''
    
    self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)  # This posts guild every 30 minute intervalds

    async def on_guild_post():
        bot.logging.info("Server count posted!")

def setup(bot):
  bot.add_cog(TopGG(bot))
  bot.logging.info("Loaded TopGG cog")