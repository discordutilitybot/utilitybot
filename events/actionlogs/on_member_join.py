import discord
from discord.ext import commands
import datetime
from discord import Member

class Greetmsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.bot.db.execute("SELECT greet_message FROM guild_settings WHERE id = ?"):
            joinchan = self.bot.db("")
            joinlog = self.bot.db


def setup(bot):
    bot.add_cog(Greetmsg(bot))
    bot.logger.info("Event Loaded Greetmsg!")