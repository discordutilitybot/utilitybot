import unittest
import unittest.mock
import discord
from discord.ext import commands
import .command 
from .command import botinfo

class TestBotInfo(unittest.TestCase):

    async def setUp(self):
        self.app = botinfo.app.setup()
        self.app.testing = True
    
    async def test_bot_info(self):
        logmsg = "Testing bot info."
        self.assertEqual(self.app.botinfo(), logmsg)
 

if __name__ == "__main__":
    unittest.main()
