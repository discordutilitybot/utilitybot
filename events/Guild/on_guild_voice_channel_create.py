"""MIT License

Copyright (c) 2020 utilitybot.co

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import discord
from discord.ext import commands


class GuildVoice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_voice_channel_create(self, channel):
        actionlogch = self.bot.db.execute(f"SELECT logging_action FROM guild_settings WHERE id = ?")

        createdby = None
        if actionlogch:
            if channel.guild.me.guild_permissions.view_audit_log:
                async for e in channel.guild.audit_logs(action=discord.AuditLogAction.voice_channel_create, limit=5):
                    if e.target.id == channel.id:
                        createdby = e.user
                        break

        embed = discord.Embed(color=discord.Color.green(
        ), timestamp=voice_channel.created_at, description=f"**New voice channel created #{voice_channel.name}")

        if createdby:
            embed.add_field(
                name='Created by', value=f'{createdby} ({createdby.id})', inline=False
            )
        embed.set_footer(
            text=f"Channel ID: {voice_channel.id} | Guild ID: {voice_channel.guild.id}"
        )
        try:
            await actionlogch.send(embed=embed)
        except discord.HTTPException:
            pass


def setup(bot):
    bot.add_cog(GuildVoice(bot))
    bot.logging.info("Loaded event GuildVoice")
