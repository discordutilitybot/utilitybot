from .user import User
from .database import Database
from .message import Message
from discord import User, Guild 

class Server(object):
    def __init__(self, id: int, server_messages: int, server_name: str, server_joined_at: datetime = datetime.utcnow()):
        self.id = id
        self.server_messages = server_messages
        self.server_name = server_name
        self.server_joined_at = server_joined_at # When the server has joined the database not when the bot has joined the server
   
    """Query/Function to check if a server is in the db if not then we add it manually.."""
    async def post(self):
        query = "SELECT * from servers WHERE id = $1"

        assure_server = await self.bot.db.fetch(query, self.server_id)
        # Creates a new server row if the server already doesnt have one..
        if assure_server == 0:
            query = "INSERT INTO servers (guild_id, server_messages, server_name, server_joined_at) VALUES ( $1, $2, $3, $4 )"

    async def get_all_servers(self, id: int, server_messages: int):
        pass
