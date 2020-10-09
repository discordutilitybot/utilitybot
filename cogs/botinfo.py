import discord
from discord.ext import commands
from discord.utils import get

class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['infobot, info'])
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title = "All about utility bot",
            description = "Something here",
            color = discord.Colour.grey()
        )   

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Botinfo(bot))