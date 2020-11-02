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

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

POSTGRES_PASSWORD = os.environ.get("database_password")
DATABASE = os.environ.get('database')

bot = Utilitybot(
    command_prefix="u!",
    status=discord.Status.dnd,
    activity= discord.Game(name="utilitybot.co | u!help", type=3),
    case_insensitive=True,
    owner_id=388788632686690305
)

# Remove default help command in discord.py
bot.remove_command('help')

async def start_db():
    try:
        login_data = {
            "user": "postgres",
            "password": POSTGRES_PASSWORD,
            "database": DATABASE
        }

        b
        

logger = logging.basicConfig(filename='utilitybot.log', level=logging.INFO)

bot.run("NzQyMTk2OTExNY4.XzCmvQ.uBrDt_ppK6p9m08ls68bnVR4Gn4")
logger.info("Yes")