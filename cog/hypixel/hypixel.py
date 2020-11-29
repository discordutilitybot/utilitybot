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

                async with session.get(f'https://api.slothpixel.me/api/guilds/{user}') as resp:
                        guild = await resp.json()

        color = ctx.author.color
        embed = discord.Embed(title=f'{user} Hypixel stats', colour=color, timestamp=datetime.datetime.utcnow())

        if player['rank'] == 'MVP_PLUS_PLUS':
            embed.add_field(name="PlayerRank", value="MVP++", inline=False)

        elif player['rank'] == 'MVP_PLUS':
            embed.add_field(name="PlayerRank", value="MVP+", inline=False)

        elif player['rank'] == "VIP_PLUS":
            embed.add_field(name="PlayerRank", value="VIP+", inline=False)

        else:
            embed.add_field(name="PlayerRank", value=player['rank'], inline=False)
        embed.add_field(name="Level:", value=player["level"], inline=False)
        if "error" in guild:
            embed.add_field(name="Guild:", value=f"{user} isn't in a guild")
        else:
            embed.add_field(name="Guild:", value=guild["name"])
        embed.add_field(name="Discord:", value=player["links"]["DISCORD"], inline=False)
        embed.add_field(name="Online:", value=player['online'], inline=False)
        embed.add_field(name="Minecraft version:", value=player['mc_version'], inline=False)
        embed.add_field(name="Last game played:", value=player['last_game'], inline=False)
        await ctx.send(embed=embed)
        await bot.logging.info({player})


def setup(bot):
    bot.add_cog(Hypixel(bot))
    bot.logging.info('Loaded cog Hypixel!')
   