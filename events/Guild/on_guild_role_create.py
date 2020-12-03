# When adding new events or enhancing them ALWAYS import datetime for time functions. This applys to everything in /events (Basically)
import discord
from discord.ext import commands
import datetime

class RoleCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        logch = self.bot.db.execute("SELECT logging_action FROM guild_settings WHERE id = ?")
        if logch:
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(
                datetime.timezone.utc), description=f'**A new role was created**\n{role.mention}')
            embed.set_author(name=role.guild.name,
                             icon_url=str(role.guild.icon_url))
            embed.set_footer(text=f"Role ID: {role.id}")
            try:
                await logch.send(embed=embed)
            except Exception:
                pass
        
def setup(bot):
    bot.add_cog(RoleCreate(bot))
    bot.logging.info("Loaded event RoleCreate")