import discord
from discord.ext import commands
import aiohttp
import datetime
from aiohttp import ClientSession
class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="hypixel", aliases=['hy'])
    async def hypixel(self, ctx, user: str = None):
        channel = ctx.message.channel
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.slothpixel.me/api/players/{user}') as resp:
                player = await resp.json()

        if user is None:
            await ctx.send(f"Please specifiy a valid username or uuid.", delete_after=5)

        if 'error' in player:
            await ctx.send(f"{user} Is not a valid username.")


def setup(bot):
    bot.add_cog(Hypixel(bot))
    bot.logger.info('$GREENLoaded $BLUE"hypixel" $GREENcog!')