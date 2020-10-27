import unittest
import unittest.mock
import discord
from discord.ext import commands

import commands
from .commands import botinfo

class TestBotInfo(unittest.TestCase):

    def setUp(self):
        self.app = bot_info.app.setup()
        self.app.testing = True
    
    # Tests main functionality of the command :)
    def test_bot_info(self):
        self.assertEqual(app.botinfo())