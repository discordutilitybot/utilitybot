"""Used to check the ping of the bot"""  
import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {bot.latency}')
        
def setup(bot):
    bot.add_cog(Ping(bot))