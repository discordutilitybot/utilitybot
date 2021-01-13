import discord
import re 
from discord.ext import commands



class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'lock', usage="<#channel/ID>",description="Lock the channel.")
    @commands.has_permissions()
    @commands.guild_only()
    async def lock(self, ctx, channel: discord.TextChannel=None):

        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("Channel successfully locked.")

   


def setup(bot):
    bot.add_cog(Lock(bot))
    bot.logging.info("Loaded lock command!")