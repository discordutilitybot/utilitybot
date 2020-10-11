import discord
from discord.ext import commands
from discord.ext.commands import errors



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Global help command (there will be help commands for each module)"""

    async def help(self, ctx):
        embed = discord.Embed(
            embed = discord.Embed(colour=ctx.author.color, description=f"Here\'s some helpful links [Commands](websiteredirecthere)      
[Suppport Server](supportserverhere)")

        

def setup(bot):
    bot.add_help = bot.remove_command("help")
    bot.add_cog(Help(bot))

