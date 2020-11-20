import discord
from discord.ext import commands


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self, guild):
        try:
            self.bot.load_extension("events.ready")
        except Exception:
            pass

        self.bot.logging(f"Bot:{self.bot.user}")
        self.bot.logging.info(f"D: {self.bot.user.id}")
        self.bot.logging.info(f"Guilds: {len(self.bot.guilds)}")
        self.bot.logging.info(f"Users: {len(self.bot.users)}")
        

        embed = discord.Embed(
            title = "Server Rules",
            description = "List of important server rules",
            color = discord.Color.orange()
        )

        embed.add_field(name="Rule 1", value="Follow the Discord Terms of Service and the Community Guidelines \nYou can find the TOS here and the Community Guidelines here.")
def setup(bot):
    bot.add_cog(Ready(bot))
    bot.logging.info(f"$REENLoaded event $CYANReady!")
  