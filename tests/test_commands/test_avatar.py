import unittest
import unittest.mock

from .command import avatar

class TestAvatar(unittest.TestCase):
    async def setUp(self):
        self.app = avatar.app.setup()
        self.app.testing = True
    
    async def testavatar(self):
        logmsg = "Testing avatae"
        self.assertTrue(self.app.avatar(), logmsg)

if __name__ == "__main__":
    unittest.main()