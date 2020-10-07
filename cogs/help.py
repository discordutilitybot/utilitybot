import discord
from discord.ext import commands
from discord.ext.commands import errors



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Global help command (there will be help commands for each module)"""

    async def help(self, ctx, module_name: str):
        if module_name is None:
            embed = discord.Embed(
                title = "Modules",
                description = "List of all the modules you can find!",
                colour = discord.Colour.blue()
            )
        
            embed.add_field(name=":tada: Fun Commands", value="Fun commands", inline=False)
            embed.add_field(name=":frame_photo: Images", value="Image commands ", inline=False) 
            embed.add_field(name=":wrench:, Utility", value="utility commands", inline=False)
            embed.add_field(name=":information_source :Info", value="u!info")

        
            await ctx.send(embed=embed)
        

        if module_name == "Mod" or "Moderation":
            pass
            
        if module_name == "Utility" or "Utilites":
            pass

        if
def setup(bot):
    bot.remove_cog('help')
    bot.add_cog(Help(bot))