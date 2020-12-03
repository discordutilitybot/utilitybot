import discord
import discord.ext 
from discord.ext import commands
import datetime

class RoleDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        logch = self.bot.db.execute("SELECT logging_action FROM guild_settings WHERE id = ?")
        if logch:
            embed = discord.Embed(color=role.color, timestamp=datetime.datetime.now(
                datetime.timezone.utc), description=f'**The role** `{role.name}` **was deleted**')
            embed.set_author(name=role.guild.name,
                             icon_url=str(role.guild.icon_url))
            embed.set_footer(text=f"Role ID: {role.id}")
            try:
                await logch.send(embed=embed)
            except Exception:
                pass
    

def setup(bot):
    bot.add_cog(RoleDelete(bot))
    bot.logging.info("Loaded event RoleDelete")