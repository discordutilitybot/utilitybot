import discord
from discord.ext import commands
import asyncio
import os
from config import TOKEN

"""Local modules"""

class Utilitybot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


    """Loading events"""
    async def load_events(self):
        pass

    """Loading utils"""
    async def load_utils(self):
        pass
    
    """Load commands."""
    async def load_cogs(self):
        pass
