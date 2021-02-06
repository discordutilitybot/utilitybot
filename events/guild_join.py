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
from discord import Guild, User
from discord.utils import get

import asyncpg
import logging


class GuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # A few problems here:
        #
        # await self.bot.create_role(``: bot doesn't have the create_role attr, changed that to ``guild``
        #
        # ``self.channel``: self.channel is undefined
        permissions = discord.Permissions(send_messages=False, speak=False, read_messages=True)
        await guild.create_role(
            name="Muted",
            reason="Utility bot's Default Muted Role on join.",
            permissions=permissions,
            color=discord.Color.orange())

        await self.channel.send(
            "**Thank you for adding me!** :white_check_mark:\n - My prefix is u! but you can change it using u!prefix [prefix]\n - You can see a list of commands by typing u!help\n - If you need help, feel free to join our support server https://utilitybot.co/suppor")


def setup(bot):
    bot.add_cog(GuildJoin(bot))
    bot.logging.info("Loaded event GuildJoin")
