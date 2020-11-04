import discord
from discord.ext import commands
import datetime
import humanfriendly

class MemberRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    # For kick, ban it will be more specific in the log this is just a global event for kick ban etc
    async def on_member_remove(self, member):
        query = f"""SELECT logging_leave FROM guild_settings WHERE id = {self.bot} """
        leavech = self.bot.db.execute(query)
        if leavech:
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
            member.avatar_url_as(static_format='png', size=2048)))

        delta = humanfriendly.format_timespan(
            datetime.datetime.utcnow() - member.joined_at,
            max_units=2
            )

        embed.add_field(name="Stayed for", value=delta, inline=False)

        if member.nick:
            embed.add_field(name="Nickname", value=member.nick)
        roles = [role.mention for role in member.roles if role != 
                member.guild.default_role]

        if roles:
            embed.add_field(
                name='Roles', value=', '.join(roles), inline=False)    
     
        try:
            await leavech.send(embed=embed)
        except Exception:
            pass
     

def setup(bot):
    try:
        bot.add_cog(MemberRemove(bot))
        bot.logging.info(f'$GREENLoaded event $CYANMemberRemove')
    except Exception:
        bot.logging.error(
            f'$REDError while loading event $CYAN"MemberRemove"'
        )