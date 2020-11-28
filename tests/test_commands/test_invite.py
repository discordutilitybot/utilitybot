import unittest
import unittest.mock
import .command 
from .command import github

class Testinvite(unittest.TestCase):

    async def setUp(self):
        self.app = invite.app.setup()
        self.app.testing = True
    
    async def testinvite(self):
        logmsg = "Testing invite."
        self.assertTrue(self.app.invite(), logmsg)

if __name__ == "__main__":
    unittest.main()-
