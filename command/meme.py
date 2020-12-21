import discord
from discord.ext import commands


class Meme(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()