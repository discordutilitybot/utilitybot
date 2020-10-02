import discord
from discord.ext import commands

"""Link to the github repo."""   
class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @command.commands()