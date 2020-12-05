"""MIT License

Copyright (c) 2020 utilitybot.co

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import discord
from discord.ext import commands
from discord.utils import get

class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['infobot, info'])
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title = "All about Utility Bot!",
            description = "Hello! I am Utility Bot I'm here to help you manage and moderate your server with a touch of fun! I was written in Python by Flop#7234 using discord.py and python3.6! Type u!help to get a link to our website for a list of commands!",
            color = discord.Color.orange()
        )   
        
        embed.set_image(url="https://cdn.discordapp.com/avatars/742196911523627068/e53fa8ac8c8492ea6d67e7e217520e26.png?size=2048")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/742196911523627068/e53fa8ac8c8492ea6d67e7e217520e26.png?size=2048")
        embed.set_footer(text=f"Guilds: {len(self.bot.guilds)}. Utility Bot The Server Management Bot.")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Botinfo(bot))
    bot.logging.info(f'Loaded botinfo command')