import discord
from discord.ext import commands
from discord.utils import get

class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['infobot, info'])
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title = "All about Utility Bot!",
            description = "Hello! I am Utility Bot I'm here to help you manage and moderate your server with a touch of fun! I was written in Python by Flop#7234 using discord.py! Type u!help to get a link to our website for a list of commands!",
            color = discord.Color.orange()
        )   
        
        
        embed.set_thumbnail(url="https://discord.com/channels/@me/700807345630085201/767113082446807070")
        embed.set_footer(text=f"Guilds: {len(self.bot.guilds)}. Utility Bot The Server Management Bot.")


def setup(bot):
    bot.add_cog(Botinfo(bot))