import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot_check

    

    @commands.command(alias=["av"])
    async def avatar(self, ctx, *, user: discord.Member):
        
        if not user:
            user = ctx.author
            
        member = None
        if ctx.guild:
            member = ctx.guild.get_member(user.id)
        await ctx.send(embed=discord.Embed(
            color=member.color if member else ctx.author.color
        ).set_image(
            url=str(user.avatar_url_as(static_format='png', size=2048))
        ))

       

def setup(bot):
    bot.add_cog(Avatar(bot))
    bot.logger.info(f'$GREENLoaded $BLUE"avatar $GREENcommand!')
