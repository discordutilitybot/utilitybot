import discord
from discord.ext import commands


class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
      if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()
        embed = discord.Embed(
            title=':musical_note: I have joined the voice chat, say c!leave for me to leave the vc. :musical_note:',
            colour=discord.Colour.green()
        )
        await ctx.send(embed = embed)
      else:
        embed = discord.Embed(
            title = ':musical_note: You have to be in a voice channel for me to join! :musical_note:',
            colour = discord.Colour.red()
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Join(bot))
    bot.logging.info("Loaded join command")