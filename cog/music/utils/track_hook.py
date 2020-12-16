import discord
from discord.ext import commands
import lavalink

class Hooks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def track_hook(self, event):
        if isinstance(event, lavalink.event.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)
            

def setup(bot):
    bot.add_cog(Hooks(bot))
    bot.logging.info("Loaded util hooks")