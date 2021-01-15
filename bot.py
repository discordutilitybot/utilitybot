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

dotenv_path = join(dirname(__file__), 'config.env')
load_dotenv(dotenv_path)

POSTGRES_PASSWORD = os.environ.get("database_password")
DATABASE = os.environ.get('database')
token = os.environ.get('discord_token')

bot = Utilitybot(
    command_prefix='u!',
    status=discord.Status.online,
    activity= discord.Game(name="utilitybot.co | u!help", type=3),
    case_insensitive=False,
    chunk_guilds_at_startup=False,
    
)

bot.load_extension("cog.serverSafety.lock")
async def start_db():
    try:
        login_data = {
            "user": "postgres",
            "password": POSTGRES_PASSWORD,
            "database": DATABASE,
            "host": '127.0.0.1'
        }

        bot.db = asyncpg.create_pool(**login_data)
    except KeyboardInterrupt:
        pass
        
for files in os.listdir('./command'):
     if files.endswith('.py'):
        bot.load_extension(f'command.{files[:-3]}')
        bot.load_extension

bot.run(f"{token}")
