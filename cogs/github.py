import discord
from discord.ext import commands

"""Link to the github repo."""   
class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @command.commands(aliases=['code, src,'])
    async def github(self, *, ctx):
        await ctx.send("You can find Utility Bot's source code here: \n https://github.com/discordutilitybot/utilitybot.")