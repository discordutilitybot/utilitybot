import discord
from discord.ext import commands

class MemberRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    # For kick, ban it will be more specific in the log this is just a global event for kick ban etc
    async def on_member_remove(self, member):
        query = f"""SELECT logging_moderation FROM guild_settings WHERE id = {ctx.guild.id} """
        logch = self.bot.db.execute(query)
        if logch:
            moderator = None
            action = None
            reason = None
            if member.guild.me.guild_permissions.view_audit_log:
                async for e in member.guild.audit_logs(limit=5):
                    if e.action in [discord.AuditLogAction.kick, discord.AuditLogAction.ban] and e.target.id == member.id:
                        moderator = e.user
                        if moderator == member.guild.me:
                            moderator = None

                        break

                    if e.action == discord.AuditLogAction.kick:
                        action = 'kick'
                        reason = e.reason
                    break

                    if e.action == discord.AuditLogAction.ban:
                        action = 'ban'
                        reason = e.reason
                    break

        embed = discord.Embed(title="Member Left", url="https://tenor.com/view/bear-hug-wave-bye-gif-12388210")

        embed.set_author(name=f'{member}', icon_url=str(
            member.avatar_url_as(static_format='png', size-2048)))
        
     

def setup(bot):
    bot.add_cog(MemberRemove(bot))