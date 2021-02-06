import discord
from discord.ext import commands


class Ready(commands.Cog):
    def __init__(self, ):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):  # on_ready doesn't take guild or channel args
        try:
            self.bot.load_extension("events.ready")
        except Exception:
            pass

        self.bot.logging(f"Bot:{self.bot.user}")
        self.bot.logging.info(f"ID: {self.bot.user.id}")
        self.bot.logging.info(f"Guilds: {len(self.bot.guilds)}")
        self.bot.logging.info(f"Users: {len(self.bot.users)}")


def setup(bot):
    bot.add_cog(Ready(bot))
    bot.logging.info(f"Loaded event Ready!")
