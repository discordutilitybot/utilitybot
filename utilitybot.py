import discord
from discord.ext import commands
import asyncio
import asyncpg
import datetime
import aiohttp
import json
#from plugins.database import Database
import logging



"""Local modules"""
class Utilitybot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launchtime = datetime.datetime.now(datetime.timezone.utc)
        self.db = asyncpg.pool.Pool = None
        self.started = False
        
        
    async def load_commands(self):
        pass

    async def load_cogs(self):
        pass

    async def load_utils(self):
        pass

    async def load_events(self):
        pass

    
        
