import discord
from discord.ext import commands
import random

class Color(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def Color(self, ctx):
        hexes = '0123456789ABCDEF'
        hexes_result = '#' + ''.join(random.choice(hexes) for _ in range(6))
        embed = discord.Embed(
            title = 'Random Color',
            description = "Random Hex color:" + hexes_result,
            colour=0x + hexes_result
        )
        await ctx.send(embed)


def setup(bot):
    bot.add_cog(Color(bot))
    bot.logging.info("Loaded color command")
