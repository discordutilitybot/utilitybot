import discord
from discord.ext import commands
from discord.ext.commands import errors



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Global help command (there will be help commands for each module)"""

    async def help(self, ctx, module_name: str):
        embed = discord.Embed(
            title = "Command's use the prefix u!",
            description = "List of commands and modules!",
            colour = discord.Colour.blue()
        )
        
        embed.add_field(name=":tada: Fun Commands", value="Fun commands", inline=False)
        embed.add_field(name=":frame_photo: Images", value="Image commands ", inline=False) # Probably will add more pictures considering i find a api for it :/ 
        embed.add_field(name=":wrench:, Utility", value="utility commands", inline=False)
        embed.add_field(name=":information_source :Info", value="u!info")


    if module_name == "utility":
        try:
            embed = discord.Embed(
                title = "Utility commands",
                description = "List of all the utility commands",
                color = discord.Colour.dark_grey()

            )

            embed.add_field(name="Utility", value="..", inline=False)

            await ctx.send(embed)

        except "Forbidden":
            await ctx.send("The bot is not allowed to perform this command.")

        except "HTTPException":
            await ctx.send("Operation failed HTTP error.")

        else:
            return
        
    if module_name == "info":
        try:
            embed = discord.Embed(
                title = "Info commands",
                description = "List of all the information commands of the server and the bot.",
                color = discord.Color.dark_grey()
            )

            embed.add_field(name="Info", value="..", inline=False)

            await ctx.send(embed)

        except "Forbidden":
            await ctx.send("The bot is not allowed to perform this command.")

        except "HTTPException":
            await ctx.send("Operation failed HTTP error.")

        else:
            return

    if module_name == "fun":
        try:
            embed = discord.Embed(
                title = "Fun commands",
                description = "List of all fun commands."
                color = discord.Color.dark_grey()

            )

            embed.add_field(name="Fun", value="..", inline=False)

            await ctx.send(embed)
    
        except "Forbidden":
            await ctx.send("The bot is not allowed to perform this command.")


        except "HTTPException":
            await ctx.send("Operation failed HTTP error.")


        else:
            return

def setup(bot):
    bot.add_cog(bot(Help))