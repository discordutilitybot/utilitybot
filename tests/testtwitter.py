import unittest
import unittest.mock
import discord
from discord.ext import commands

#import .command
#from .command import twitter

class TestTwitter(unittest.TestCase):

    async def setUp(self):
        self.app = twitter.app.set()
        self.app.testing = True
    

    async def test_twitter(self):
        logmsg = "Testing twitter"
        self.assertEqual(self.app.twitter(), logmsg)

if __name__ == "__main__":
    unittest.main()