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

        embed = discord.Embed(color=discord.Color.green(

        ), timestamp=channel.created_at, description=f"**New Channell created #{channel.name}**")

        if createdby:
            embed.add_field(
                name='Created by', value=f'{createdby} ({createdby.id})', inline=False
            )
        embed.set_author(name=channel.guild.name,
                         icon_url=str(channel.guild.icon_url)
        )
        embed.set_footer(
            text=f"Channel ID: {channel.id} | Guild ID: {channel.guild.id}")
        
        try:
            await actionlogch.send(embed=embed)
        except Exception:
            pass

def setup(bot):
    try:
        bot.add_cog(ChannelCreate(bot))
        bot.logging.info("$GREENLoaded event $CYANChannelCreate")
    except Exception:
        pass
