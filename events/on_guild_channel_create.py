import discord
from discord.ext import commands

class ChannelCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        actionlogch = self.bot.db.execute(f"SELECT logging_action FROM guild_settings WHERE id = {ctx.guild.id}")

        if actionlogch:
            createdby =  None
            if channel.guild.me.guild_permissions.view_audit_log:
                async for e in channel.guild.audit_logs(action=discord.AuditLogAction.channel_create, limit=3):
                    if e.target.id == channel.id:
                        createdby = e.user
                        break


        
def setup(bot):
    bot.add_cog(ChannelCreate(bot))