import discord
from discord.ext import commands
import aiohttp
from aiohttp import ClientSession
import random

class Meme(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
    @commands.command()
    async def meme(self, ctx):
        embed = discord.Embed(title="Meme")


        async with aiohttp.ClientSession() as cs:
           async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
             res = r.json()
             embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
             await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Meme(bot))
  bot.logging.info("Loaded meme command")