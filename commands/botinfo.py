import discord
from discord.ext import commands
from discord.utils import get

class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['infobot, info'])
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title = "All about utility bot",
            description = "Something here",
            color = discord.Color.blue()
        )   
        
        embed.set_thumbnail(url="https://discord.com/channels/@me/700807345630085201/767113082446807070")
        embed.set_footer(text=f"Guilds: {len(self.bot.guilds)}")


def setup(bot):
    bot.add_cog(Botinfo(bot))