import discord
from discord.ext import commands


class Ready(commands.Cog):
    def __init__(self, bot, id, guild_name, joined_at):
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
        
        query = """INSERT INTO guilds ( id, guild_name)
                VALUES ($1, $2, $3 )
                ON CONFLICT DO NOTHING"""
        await self.bot.db.execute(query, self.guild_id, self.ctx.guild.name)
def setup(bot):
    bot.add_cog(Ready(bot))
    bot.logging.info(f"Loaded event Ready!")
  