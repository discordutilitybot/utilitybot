import discord
from discord.ext import commands

class Servericon(commands.Cog):
    def __init__(self, bot) :
        self.bot = bot

    @commands.command()
    async def servericon(self, ctx):
        member = ctx.author.color
        guild = ctx.message.author
        
        await ctx.send(embed=discord.Embed(
               color=member.color if member else ctx.author.color.set_image(
                   url=str(guild.avatar_url_as(static_format='png', size=2048))
               )
            ))
            
def setup(bot):
    bot.add_cog(Servericon(bot))
    bot.logging.info("Loaded Servericon command")