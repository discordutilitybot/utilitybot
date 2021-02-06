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
            await ctx.send(f" :x: Please specifiy a valid username or uuid.", delete_after=6)
            return

        if 'error' in player:
            await ctx.send(f":x:{user} Is not a valid username.")
            return

        async with channel.typing():
            async with aiohttp.ClientSession() as session:
                # second request here was redundant so i removed it
                async with session.get(f'https://api.slothpixel.me/api/guilds/{user}') as resp:
                        guild = await resp.json()

        color = ctx.author.color
        embed = discord.Embed(title=f'{user} Hypixel Stats', colour=color, timestamp=datetime.datetime.utcnow())

        if player['rank'] == 'MVP_PLUS_PLUS':
            embed.add_field(name="PlayerRank", value="MVP++")

        elif player['rank'] == 'MVP_PLUS':
            embed.add_field(name="PlayerRank", value="MVP+")

        elif player['rank'] == "VIP_PLUS":
            embed.add_field(name="PlayerRank", value="VIP+")

        else:
            embed.add_field(name="PlayerRank", value=player['rank'])
        embed.add_field(name="Level:", value=player["level"])
        if "error" in guild:
            embed.add_field(name="Guild:", value=f"{user} isn't in a guild")
        else:
            embed.add_field(name="Guild:", value=guild["name"])
        embed.add_field(name="Discord:", value=player["links"]["DISCORD"])
        embed.add_field(name="Online:", value=player['online'])
        embed.add_field(name="Minecraft version:", value=player['mc_version'])
        embed.add_field(name="Last game played:", value=player['last_game'])
        await ctx.send(embed=embed)
        await self.bot.logging.info({player})


def setup(bot):
    bot.add_cog(Hypixel(bot))
    bot.logging.info('Loaded cog Hypixel!')
   