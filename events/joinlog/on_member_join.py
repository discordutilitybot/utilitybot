import discord
from discord.ext import commands
import datetime
from discord import Member

class Greetmsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.bot.db.execute("SELECT logging_join FROM guild_settings WHERE id = ?"):
            usedinvite = Noneg
            joinchan = self.bot.db.execute("SELECT logging_join FROM guild_settings WHERE id = ?")

            vars  = {
                '{user.mention}': member.mention,
                '{user}': str(member),
                '{user.name}': member.name,
            }   '{count}': str(member.guild.member_count)
        

        
            if joinchan:
                embed =  discord.Embed(title="Member Joined", url="https://tenor.com/view/penguin-hello-hi-hey-there-cutie-gif-3950966")

                embed.set_author(name=f"{member}", icon_url=str(
                    member.avatar_url_as(static_format='png', size=2048)))

                embed.add_field(name='Account Created', value=datetime.datetime.utcnow() - member.created_at) + 'ago', inline=False)
                if used invite:
                    embed.add_field(name="Invite used", value=used_invite, inline=False)

                
def setup(bot):
    bot.add_cog(Greetmsg(bot))
    bot.logger.info("Event Loaded Greetmsg!")