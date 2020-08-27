import discord
from discord.ext import commands
from discord.ext.commands import errors



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Global help command (there will be help commands for each module)"""

    async def help(self, ctx):
        embed = discord.Embed(
            title = "Command list"
            description = "List of commands and modules!"
            colour = discord.Colour.dark_grey()
        )
        
        embed.add_field(name=":tada: Fun Commands" value="coinflip, multiply, add, divide, subtract, blackjack, guess, say, roast, slap, punch, kick,", inline=False)
        embed.add_field(name=":frame_photo: Images", value="meme, cat, dog, slap, smile", inline=False) # Probably will add more pictures considering i find a api for it :/ 
        embed.add_field(name=":wrench:, Utility", value="poll, suggest, botlist, tag", inline=False)
        embed.add_field(name=":information_source:Info", value="avatar, help, invite, serverinfo, userinfo")
        embed.add_field(name=":hammer_pick Mod" value="kick, ban, mute, purge, unmute, unban," inline=False)
	
  

def setup(bot):
    bot.add_cog(bot(Help))
