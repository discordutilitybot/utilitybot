import discord
from discord.ext import commands
from discord.utils import get
import datetime
from discord import Member

class Joinlog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
       
        usedinvite = Noneg
        logch = self.bot.db.execute("SELECT logging_join FROM guild_settings WHERE id = ?")
        channel = discord.utils.get(guild.text_channels, name="logs")

        vars  = {
            '{user.mention}': member.mention,
            '{user}': str(member),
            '{user.name}': member.name,
        }   
        
        if logch:
            embed =  discord.Embed(title="Member Joined", url="https://tenor.com/view/penguin-hello-hi-hey-there-cutie-gif-3950966")

            embed.set_author(name=f"{member}", icon_url=str(
                member.avatar_url_as(static_format='png', size=2048)))

            embed.add_field(name='Account Created', value=datetime.datetime.utcnow() - member.created_at), + 'ago', inline=False)
            if used invite:
                embed.add_field(name="Invite used:", value=used_invite, inline=False)

            embed.add_footer(name="Member Count:", value=f"{guild.members}")

            try:
                await logch.send(embed)
                except Exception:
                    pass


def setup(bot):
    bot.add_cog(Greetmsg(bot))
    bot.logging.info("Event Loaded Joinlog!")