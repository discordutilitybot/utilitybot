import discord
from discord.ext import commands
import aiohttp
import datetime
class Duels(commands.Cog):
    def __init__(self, bot):
        self.bot  = bot

    @commands.command()
    async def duels(self, ctx, user: str):
        channel = ctx.message.channel
        async with channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.slothpixel.me/api/guilds/{user}') as resp:
                    user = await resp.json()
                    color = ctx.author.color

                if 'error' in user:
                    embed = discord.Embed(title=f"{user} is not a player", colour=color,
                                                  timestamp=datetime.datetime.utcnow())
                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Duels(bot))
    bot.logging.info("Loaded duels command")


