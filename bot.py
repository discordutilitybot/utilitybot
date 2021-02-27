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

import utilitybot
from utilitybot import Utilitybot

import logging
import datetime
import asyncpg
import asyncio
import dotenv
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json
import datetime

dotenv_path = join(dirname(__file__), 'config.env')
load_dotenv(dotenv_path)

POSTGRES_PASSWORD = os.environ.get("database_password")
DATABASE = os.environ.get('database')
token = os.environ.get('discord_token')

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = Utilitybot(
    command_prefix='u!',
    status=discord.Status.online,
    activity= discord.Game(name="utilitybot.co | u!invite", type=3),
    case_insensitive=False,
)

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'u!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)

bot.remove_command("help")

bot.load_extension("cog.serverSafety.lock")
async def start_db():
    try:
        login_data = {
            "user": "postgres",
            "password": POSTGRES_PASSWORD,
            "database": DATABASE,
            "host": '172.105.104.44'
        }

        bot.db = asyncpg.create_pool(**login_data)
        bot.logging.info("Connected to database pool.")
    except KeyboardInterrupt:
        pass
        

bot.remove_command("help")
bot.load_extension("command.twitter")
bot.load_extension("command.avatar")
bot.load_extension("command.github")
bot.load_extension("cog.admin.admin")
bot.load_extension("cog.hypixel.guild")
bot.load_extension("cog.hypixel.hypixel")
bot.load_extension("cog.hypixel.bedwars")
bot.load_extension("cog.hypixel.duels")
bot.load_extension("command.botinfo")
bot.load_extension("command.server_info")
bot.load_extension("command.server_icon")
bot.load_extension("events.Guild.on_guild_channel_create")
bot.load_extension("events.command_error")
bot.load_extension("command.meme")
bot.load_extension("cog.misc.games")
bot.load_extension("command.invite")
bot.load_extension("command.talk")
bot.load_extension("command.ping")
bot.load_extension('command.about')
bot.load_extension("command.channelinfo")

@bot.command(aliases = ['commands'])
@commands.cooldown(1, 5, commands.BucketType.guild)
async def help(ctx):
    embed = discord.Embed(
        title = 'List of available Commands, all Commands are case insensitive',
        colour = discord.Colour.orange(),
        description = '`Important links `https://utilitybot.co, https://discord.gg/3fBcFFsm6U, https://twitter.com/utilitybot1, https://top.gg/bot/790399381840068619#/  ',
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name = 'Commands Categories 📖', value = '`Utility, Fun, Bot, Moderation`', inline = False)
    embed.add_field(name = 'Bot 🤖', value = '`help, botinfo, invite, ping`', inline = False)
    embed.add_field(name = 'Fun 🎉', value = '`eightball, coinflip`', inline = False)
    embed.add_field(name = 'Integrations 🎉', value = '`hypixel, bedwars, duels, guild, meme`', inline = False)
    embed.add_field(name = 'Utility ⚙️', value = '`servericon, avatar, channel_information`', inline = False)
    embed.add_field(name = 'Moderation ⚒️', value = '`poll, ban, unban, mute, unmute, warn, kick,purge, nick`', inline = False)
    embed.set_footer(text = 'Utility Bot, The ultimate server management bot')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790349906648498219/805846213475827722/Screen_Shot_2021-01-04_at_7.png?size=2048')
    await ctx.send(embed=embed)

bot.run('NzkwMzk5MzgxODQwMDY4NjE5.X-ACyQ.g9EGJ-VrLMbznPIH-WG2spJoDbI')
