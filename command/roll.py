import discord
from discord.ext import commands

import random

class Rolldie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, num):
        final = random.randint(1, num)
        await ctx.send(num)
        
def setup(bot):
    bot.add_cog(Rolldie(bot))
    bot.logging.info('Loaded color command')
