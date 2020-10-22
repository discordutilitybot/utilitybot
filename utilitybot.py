import discord
from discord.ext import commands
import asyncio
import asyncpg
import datetime
import aiohttp
from datetime import datetime
import json
from plugins.database import Database
import logging
from logging import logging

"""Local modules"""

class Utilitybot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launchtime = datetime.datime.utcnow(datetime.timezone.utc)
        self.db = asyncpg.pool.Pool = None
        """Common attributes"""

        logging.basicConfig()

    
        
