import asyncio
from discord.ext import commands
import discord
import youtube_dl
import os
from datetime import datetime

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
players = {}
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def play(self, ctx, *, url: str = None):
       
      if url == None:
        await ctx.send('```c!play [youtube title or URL]```')
      async with ctx.typing():
          player = await YTDLSource.from_url(url, stream=True)
          ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
          embed = discord.Embed(
            title = 'Song requested by: ' + str(ctx.author),
            description = '```Now playing: {}'.format(player.title) + '\n\nRequested by: ' + str(ctx.author) + '```',
            colour = discord.Colour.green(),
            timestamp=datetime.utcnow()
          )
          embed.set_thumbnail(url = 'https://images-ext-1.discordapp.net/external/jM4yYJy0MXntKVzqbDTLUi72OfQneGULXCMZoBbFwhw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/739305861951782985/407c829335208d72834df10e45721c5b.webp?width=701&height=701')
          await ctx.send(embed = embed)
          players[ctx.guild.id]=player
    @commands.command()
    async def pause(self, ctx):
        state = ctx.get_voice_state(ctx.message.guild)
        if state.is_playing():
          player = state.player
          player.pause()
    @commands.command()
    async def join(self, ctx):
      if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()
        embed = discord.Embed(
            title='I have joined the voice chat, say u!leave for me to leave the voice channel.',
            colour=discord.Colour.green()
        )
        await ctx.send(embed = embed)
      else:
        embed = discord.Embed(
            title = ':musical_note: You have to be in a voice channel for me to join!',
            colour = discord.Colour.red()
        )
        await ctx.send(embed = embed)
    @commands.command(pass_context = True)
    async def leave(self, ctx):

      if ctx.author.voice and ctx.author.voice.channel:
        await ctx.voice_client.disconnect()
        embed = discord.Embed(
            title='I have left the voice chat, say u!join for me to join again!',
            colour=discord.Colour.red()
        )
        await ctx.send(embed = embed)
      else:
        embed = discord.Embed(
            title = 'You have to be in a voice channel for me to leave!',
            colour = discord.Colour.red()
        )
        await ctx.send(embed = embed)
    @commands.command(pass_context=True)
    async def skip(self, ctx):
      channel = await ctx.voice_client.disconnect()
      if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()
        embed = discord.Embed(
          title = 'Skip requested by: ' + str(ctx.author),
          description = '```Previous song skipped```',
          colour = discord.Colour.green(),
          timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url = 'https://images-ext-1.discordapp.net/external/jM4yYJy0MXntKVzqbDTLUi72OfQneGULXCMZoBbFwhw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/739305861951782985/407c829335208d72834df10e45721c5b.webp?width=701&height=701')
        await ctx.send(embed = embed)
def setup(bot):
    bot.add_cog(Music(bot))