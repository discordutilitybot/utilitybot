import discord
from discord.ext import commands


class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name='join')
    

def setup(bot):
    bot.add_cog(Join(bot))
    bot.logging.info("Loaded join command")