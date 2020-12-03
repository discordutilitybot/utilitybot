# When adding new events or enhancing them ALWAYS import datetime for time functions. This applys to everything in /events (Basically)
import discord
from discord.ext import commands
import datetime

class RoleCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    logch = self.bot.db.execute("SELECT logging_action FROM guild_settings WHERE id = ?")

    if logh:
        embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(
            datetime.utc), description=f'**A new role was create**\m{role.mention}')
        embed.set_author(name=role.guild.name,
                        icon_url=str(role.guild.icon_url))
        embed.set_footer(text=f"Role ID: {role.id}")
        ))

        try:
            await logch.send(embed=embed)
        except Exception:
            pass
        
def setup(bot):
    bot.add_cog(RoleCreate(bot))
    bot.logging.info("Loaded event RoleCreate")