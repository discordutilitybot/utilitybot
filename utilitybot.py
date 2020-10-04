import discord
from discord.ext import commands
import asyncio
import asyncpg
import datetime
import aiohttp
from datetime import datetime
import json
from secrets import *
from secrets import database_host


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
        self.db = await asyncpg.create_pool(user='postgres', host=database_host, max_size=None, min_size=None)
        

    """Loading cogs/events functions"""
    async def load_events(self):
        for ext in resolve_extensions(self, 'events.*'):
           self.load_extension(ext)

    
    async def load_utils(self):
        for ext in resolve_extensions(self, 'utils.*'):
            self.load_extension(ext)
          
                

    async def load_cogs(self):
        for ext in resolve_xtensions(self, 'cogs.*'):
            self.load_extension(ext)
            
    
    
    self.load_cogs()

    self.load_events()

    self.load_utils()


    