import discord
from discord.ext import commands


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self, guild, channel):
        try:
            self.bot.load_extension("events.ready")
        except Exception:
            pass

        self.bot.logging(f"Bot:{self.bot.user}")
        self.bot.logging.info(f"D: {self.bot.user.id}")
        self.bot.logging.info(f"Guilds: {len(self.bot.guilds)}")
        self.bot.logging.info(f"Users: {len(self.bot.users)}")
        
        # Im not sure why but dpy discards member updates (e.g if they update nickname etc etc) Ffrom memebers that arent cached so i need them to be cached for updates and features
        # note: Features like logging will continue to work as normal when members are cached.
        [await self.chunk(g) for g in sorted(self.bot.guilds, key=lambda g: g.member_count, reverse=True) if self.bot.should_chunk(g)]
        async def chunk(self, guild):
            try:
                guild.chunk()
            except Exception:
                self.bot.logging.error(
                    f"Failed to chunk guilds {guild}"
                )
        
        
def setup(bot):
    bot.add_cog(Ready(bot))
    bot.logging.info(f"$REENLoaded event $CYANReady!")
  