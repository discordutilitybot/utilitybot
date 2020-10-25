import discord
from discord.ext import commands

class MemberRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    # For kick, ban it will be more specific in the log this is just a global event for kick ban etc
    async def on_member_remove(self, member):
        pass



def setup(bot):
    bot.add_cog(MemberRemove(bot))