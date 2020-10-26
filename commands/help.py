import discord
from discord.ext import commands
from discord.ext.commands import errors


class Help(commands.Cog):

    """Custom help command for Utility Bot rather than auto generated one by discord.py"""

    def __init__(self, bot):
        self.bot = bot

    """Global help command (there will be help commands for each module)"""

    async def commands(self, ctx):
        embed = discord.Embed(colour=ctx.author.color, description=f'''Here\'s some helpful links
    [Commands](https://utilitybot.co/commands)
    [Support Server](sereverlinkhere)
    [Invite Me](invitelinkhere)
        ''')

        await ctx.send(embed=embed)
            

            
def setup(bot):
    bot.add_cog(Help(bot))

