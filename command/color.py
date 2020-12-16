import discord
from discord.ext import commands

class Color(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def random_color(self, ctx):
        color_number = 8

        color_picked = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
            for i in range(number_of_colors)]

        await ctx.send(embed=discord.Embed(color=color_picked, description="Random color: " + color_picked)

def setup(bot):
    bot.add_cog(Color(bot)
    bot.logging.info("Loaded color command!")