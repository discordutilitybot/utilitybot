import discord
from discord.ext import commands
from discord.ext.commands import errors



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Global help command (there will be help commands for each module)"""

    async def help(self, ctx):
        
        

        
def setup(bot):
    bot.remove_cog('help')
    bot.add_cog(Help(bot))