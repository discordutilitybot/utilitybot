import discord
from discord.ext import commands
import asyncio
import asyncpg
import datetime
import aiohttp
from datetime import datetime
import json
#from plugins.database import Database
import logging



"""Local modules"""

class Utilitybot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launchtime = datetime.dateime.utcnow(datetime.timezone.utc)
        self.db = asyncpg.pool.Pool = None
        self.started = False
        """Common attributes"""

        logging.basicConfig(filename="utility.log", level=logging.INFO)
        self.logger = logging.getLogger('Utility')
        

    
        
