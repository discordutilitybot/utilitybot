"""MIT License

Copyright (c) 2020 utilitybot.co

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import discord
from discord.ext import commands
import aiohttp
from aiohttp import ClientSession
import random

class Memecommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
    @commands.command(aliases=["dankmeme"])
    async def meme(self, ctx):
        embed = discord.Embed(title="Meme")


        async with aiohttp.ClientSession() as cs:
           async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
             res = r.json()
             embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
             await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Memecommand(bot))
  bot.logging.info("Loaded meme command")