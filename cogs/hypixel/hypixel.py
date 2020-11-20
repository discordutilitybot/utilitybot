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
            return

        if 'error' in player:
            await ctx.send(f"{user} Is not a valid username.")
            return

        async with channel.typing():
            async with aiohttp.ClientSession() as session:

                async with session.get(f'https://api.slothpixel.me/api/players/{user}') as resp:
                    player = await resp.json()

                 async with session.get(f'https://api.slothpixel.me/api/guilds/{arg1}') as resp:
                        guild = await resp.json()

        color = ctx.author.color
        embed = discord.Embed(title=f'{user} Hypixel stats', colour=color, timestamp=datetime.datetime.utcnow())

        if player['rank'] == 'MVP_PLUS_PLUS':
            embed.add_field(name="PlayerRank", value="MVP++", inline=False)

        elif player['rank'] == 'MVP_PLUS':
            embed.add_field(name="PlayerRank", value="MVP+", inline=False)

        elif player['rank'] == "MVP":
            embed.add_field(name="PlayerRank", value="MVP", inline=False)
        

        elif player['rank'] == "VIP_PLUS":
            embed.add_field(name="PlayerRank", value="VIP+", inline=False)

        elif player['rank'] == "VIP":
            embed.add_field(name="PlayerRank", value="VIP", inline=False)
        

       
        


def setup(bot):
    bot.add_cog(Hypixel(bot))
    bot.logging.info('$GREENLoaded $BLUE"hypixel" $GREENcog!')
   