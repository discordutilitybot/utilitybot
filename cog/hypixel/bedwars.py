import discord
from discord.ext import commands
import datetime
import aiohttp


class Bedwars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['bw', 'bws'])
    async def bedwars(self, ctx, user):
        channel = ctx.message.channel
        async with channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.slothpixel.me/api/players/{user}') as resp:
                    player = await resp.json()

            color = ctx.author.color
            embed = discord.Embed(title=f'{user} Bedwars stats', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Stars:", value=player["stats"]["BedWars"]["level"], inline=False)
            embed.add_field(name="Wins:", value=player["stats"]["BedWars"]["wins"], inline=False)
            embed.add_field(name="Games played:", value=player["stats"]["BedWars"]["games_played"], inline=False)
            embed.add_field(name="W/l ratio:", value=player["stats"]["BedWars"]["w_l"], inline=False)
            embed.add_field(name="Final Kills:", value=player["stats"]["BedWars"]["final_kills"], inline=False)
            embed.add_field(name="Final Deaths:", value=player["stats"]["BedWars"]["final_deaths"], inline=False)
            embed.add_field(name="Normal Kills:", value=player["stats"]["BedWars"]["kills"], inline=False)
            embed.add_field(name="Normal Deaths:", value=player["stats"]["BedWars"]["deaths"], inline=False)
            embed.add_field(name="FKDR:", value=player["stats"]["BedWars"]["final_k_d"], inline=False)
            embed.add_field(name="Current Winstreak:", value=player["stats"]["BedWars"]["winstreak"], inline=False)
            await ctx.send(embed=embed)
            return

def setup(bot):
    bot.add_cog(Bedwars(bot))
    bot.logging.info("Loaded bedwars command!")