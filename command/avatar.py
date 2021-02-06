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

import typing

import discord
from discord.ext import commands


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar", aliases=["av", "pfp"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def avatar(self, ctx, target: typing.Union[discord.Member, discord.User, str, None]):
        # why....??????????
        if isinstance(target, str):
            return await ctx.send(embed=discord.Embed(
                description=f"User \"{target}\" not found",
                color=ctx.author.color,
                timestamp=ctx.message.created_at
            ))
        if not target:
            target = ctx.author
        await ctx.send(embed=discord.Embed(
            color=target.color,
            timestamp=ctx.message.created_at,
            description=target.mention
        ).set_image(
            url=str(target.avatar_url_as(static_format="png", size=2048))
        ).set_author(
            name=f"{target}'s Avatar"
        ))


def setup(bot):
    bot.add_cog(Avatar(bot))
    bot.logging.info('Loaded avatar command')