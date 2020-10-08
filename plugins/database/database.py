import asyncio
import asyncpg
import json
import discord

from discord import User
from discord import Guild
from discord import Message


class Database(object):
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
        return self 
        
    async def fetch(self, query, *args):
        async with self._rate_limit:
            async with self._pool.acquire() as con:
                return await con.fetch(query, *args, timeout=self.timeout)
    """Fetch a row"""
    async def fetchrow(self, query, *args):
        async with self._rate_limit:
            async with self._pool.acquire() as con:
                return await con.fetch(query, *args)
    """"Execute querys"""
    async def execute(self, query, *args):
        async with self._rate_limit:
            async with self._pool.acquire() as con:
                return await con.execute(query *args)

    async def get_user(self, user_id: int, get_messages: bool = False):
        query = "SELECT * users WHERE id = $1"

        record = await self.fetchrow(query, user_id)
        if record is None:
            # If there a user doesnt have its own row then we add one:
            user = User(bot=self.bot, id=user_id, messages=[])
            await user.post()
            return user
    """Get all users in the db **not** a the servers"""

    async def get_all_users(self, user_id: int, get_messages: bool = False):
        query = "SELECT * users WHERE id = $1"
        await self.fetchrow(query, user_id)


        