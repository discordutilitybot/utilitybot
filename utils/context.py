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


class Context(commands.Context):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = [
            discord.Color.blue(),
            discord.Color.blurple(),
            discord.Color.dark_blue(),
            discord.Color.dark_gold(),
            discord.Color.dark_green(),
            discord.Color.dark_magenta(),
            discord.Color.dark_orange(),
            discord.Color.dark_purple(),
            discord.Color.dark_red(),
            discord.Color.dark_teal(),
            discord.Color.gold(),
            discord.Color.green(),
            discord.Color.magenta(),
            discord.Color.orange(),
            discord.Color.purple(),
            discord.Color.red(),
            discord.Color.teal()
        ]

    async def modlog(self, embed: discord.Embed):
        pass

    async def actionlog(self, embed: discord.Embed):
        # wow you screwed that up
        pass
