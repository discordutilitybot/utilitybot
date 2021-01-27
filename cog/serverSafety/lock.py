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
import re 
from discord.ext import commands
import load_moderation


class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.states = {}
    @commands.has_permissions(manage_channels=True)
    @commands.command(pass_context=True, name="lockdown")
    async def lockdown(self, ctx):
        """Lock message sending in the channel."""
        try:
            try:
                mod_strings = load_moderation()
                mod_role_strings = mod_strings[ctx.message.guild.name]
                mod_roles = []
                for m in mod_role_strings:
                    mod_roles.append(discord.utils.get(ctx.message.guild.roles, name=m))
            except:
                mod_roles = []
            server = ctx.message.guild
            overwrites_everyone = ctx.message.channel.overwrites_for(server.default_role)
            overwrites_owner = ctx.message.channel.overwrites_for(server.role_hierarchy[0])
            if ctx.message.channel.id in self.states:
                await ctx.send("🔒 Channel is already locked down. Use `unlock` to unlock.")
                return
            states = []
            for a in ctx.message.guild.role_hierarchy:
                states.append([a, ctx.message.channel.overwrites_for(a).send_messages])
            self.states[ctx.message.channel.id] = states
            overwrites_owner.send_messages = True
            overwrites_everyone.send_messages = False
            await ctx.message.channel.set_permissions(server.default_role, overwrite=overwrites_everyone)
            for modrole in mod_roles:
                await ctx.message.channel.set_permissions(modrole, overwrite=overwrites_owner)
            await ctx.send(
                "🔒 Channel locked down. Only roles with permissions specified in `moderation.json` can speak.")
        except discord.errors.Forbidden:
            await ctx.send(self.bot.bot_prefix + "Missing permissions.")

    @commands.has_permissions(manage_channels=True)
    @commands.command(pass_context=True, name="unlock")
    async def unlock(self, ctx):
        """Unlock message sending in the channel."""
        try:
            if not ctx.message.channel.id in self.states:
                await ctx.send("🔓 Channel is already unlocked.")
                return
            for a in self.states[ctx.message.channel.id]:
                overwrites_a = ctx.message.channel.overwrites_for(a[0])
                overwrites_a.send_messages = a[1]
                await ctx.message.channel.set_permissions(a[0], overwrite=overwrites_a)
            self.states.pop(ctx.message.channel.id)
            await ctx.send("🔓 Channel unlocked.")
        except discord.errors.Forbidden:
            await ctx.send(self.bot.bot_prefix + "Missing permissions.")


def setup(bot):
    bot.add_cog(Lock(bot))
    bot.logging.info("Loaded lock command!")