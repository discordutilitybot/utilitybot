import discord
import discord.ext 
from discord.ext import commands
import datetime

# This class represents all the different categorys of commands
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commands(self, ctx, category):


        if 'error' in category:
            await ctx.send(":x:That category isn't availaible")
        

        if category == "moderation":
            color = ctx.author.color
            embed = discord.Embed(
                title="Moderation commands",
                description="Here is a list of all the moderation commands!",
                color = color

            )

            embed.add_field(name="u!ban [member] (optional reason)", value="Bans a user with an optional reason.", inline=False)
            embed.add_field(name="u!kick [member] (optional reason)", value="Kicks a user with an optional reason.", inline=False)
            embed.add_field(name="u!mute [member] (optional reason)", value="Mutes a user with a specified amount of time,", inline=False)
            # Note: if you dont specify a user it deletes all messages no matter what user it is and the default count is 10 messages.
            embed.add_field(name="u!purge (optional member) (optional count)", value="Purges message either from a specific user and or a specific amount.", inline=False)
            
def setup(bot):
    bot.add_cog(Commands(bot))
    bot.logging.info("Loaded cog Commands")