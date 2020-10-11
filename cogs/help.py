import discord
from discord.ext import commands
from discord.ext.commands import errors


class Help(commands.Cog):

    """Custom help command for Utility Bot rather than auto generated one by discord.py"""

    def __init__(self, bot):
        self.bot = bot

    """Global help command (there will be help commands for each module)"""

    async def help(self, ctx):
         prefix = ctx.prefix.replace(
            '<@444871677176709141> ', '@Fire ').replace('<@!444871677176709141>', '@Fire ')
        embed = discord.Embed(colour=ctx.author.color, description=f'''Here\'s some helpful links
[Commands](websiteredirecthere)
[Support Server](sereverlinkhere)
[Invite Me](invitelinkhere)
''')

            

        

def setup(bot):
    bot.add_help = bot.remove_command("help")
    bot.add_cog(Help(bot))

