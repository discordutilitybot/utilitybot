import discord
from discord.ext import commands

class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def server_info(self, ctx):
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                                                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					                                len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					                                len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))] 
