import discord
from discord.ext import commands


"""Get a link to utility bot's twitter"""
class Twitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def twitter(self, ctx):
        await ctx.send("Here's a link to utility bot's twitter \n [twitter]())


def setup(bot):
    bot.add_cog(Twitter(bot))
