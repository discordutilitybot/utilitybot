import asyncio
import asyncpg
import json
import discord

from discord import Message, User
from discord import Guild
from discord import Message

class Database:
    def __init__(self, bot, pool, loop=None, timeout: float = 60.0):
        self.bot = bot
        self.pool = pool
        self._loop = loop or asyncio
        self.timeout = timeout
        self._rate_limit = asyncio.Semaphore(value=self._pool._maxsize, loop=self._loop)

    @classmethod
    async def create_pool(cls, bot, uri=None, *, min_connections=10, max_connections=10,
        timeout=60.0, loop=None, **kwargs):
        pool = await asyncpg.create_pool(uri, min_size=min_connections, max_size=max_connections, **kwargs)
        self = cls(bot=bot, pool=pool, loop=loop, timeout=timeout)
        print('Established DataBase pool with {} - {} connections\n'.format(min_connections, max_connections))
        return self 
        
    async def fetch(self, query, *args):
        async with self._rate_limit:
            async with self._pool.acquire() as con:
                return await con.fetch(query, *args, timeout=self.timeout)

    async def fetchrow(self, query, *args):
        async with self._rate_limit:
            async with self._pool.acquire() as con:
                return await con.fetch(query, *args)
    
    async def execute(self, query, *args):
        async with self._rate_limit:
            async with self._pool.acquire() as con:
                return await con.execute(query *args)

    async def get