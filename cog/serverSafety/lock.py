import discord
import re 
from discord.ext import commands



class LockCog(commands.Cog, name="serverChannelsLock"):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(name = 'lock',
                        usage="<#channel/ID>",
                        description="Lock the channel.")
    @commands.guild_only()
    async def lock (self, ctx, channel):

        
        channel = re.findall(r'\d+', channel) # 
        channel = self.bot.get_channel(int(channel[0]))

        if channel is None:
            await channel.edit(name=f"Locked-{channel.name}")
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            embed = discord.Embed(title = f"#{channel.name} channel(s) locked with success!", description = f"", color = 0x2fa737) 
            await ctx.channel.send(embed = embed)
        else:
            await ctx.channel.send("Channel not found!")


def setup(bot):
    bot.add_cog(LockCog(bot))
    bot.logging.info("Loaded locking command!")