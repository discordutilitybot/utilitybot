import discord
from discord.ext import commands

class ChannelCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        actionlogch = self.bot.db.execute(f"SELECT logging_action FROM guild_settings WHERE id = {ctx.guild.id}")

        if actionlogch:
            pass


def setup(bot):
    bot.add_cog(ChannelCreate(bot))