import discord
from discord.ext import commands

"""Link to the github repo."""   
class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['code, src, oss, source'])
    async def github(self, *, ctx):
        await ctx.send("You can find Utility Bot's source code here: \n https://github.com/discordutilitybot/utilitybot.")