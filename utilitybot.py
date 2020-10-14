"""Main file with all attributes and extensions"""

import discord
from discord.ext import commands
import asyncio
import asyncpg
import datetime
import aiohttp
from datetime import datetime
import json
from secrets import *
from plugins.database import Database


"""Local modules"""

class Utilitybot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launchtime = datetime.datime.utcnow(datetime.timezone.utc)
        self.db = None
        """Common attributes"""

        """Logging (log files levels etc..)"""

        """Other"""

    async def connect(self):
        """Initialize asyncpg Pool"""
        self.db = await asyncpg.create_pool()
        