import unittest
import unittest.mock
import discord
from discord.ext import commands
import .command 
from .command import github

class TestGithub(unittest.TestCase):
    
    async def setUp(self):
        self.app = github.app.setup()
        self.app.testing = True

    async def test_github(self):
        logmsg = "Testing github"
        self.assertEqual(self.app.github(), logmsg)
      
if __name__ == "__main__":
    unittest.main()