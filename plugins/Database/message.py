from .user import User
from .database import Database

class Message(object):

    def __init__(self, bot, message_id: int, channel_id: int, guild_id: int, author_id: int):
        self.bot = bot
        self.message_id = message_id
        self.channel_id = channel_id
        self.guild_id = guild_id
        self.author_id = author_id



    async def post(self):
        query = """INSERT INTO Messages ( message_id, guild_id, author_id, channel_id )
                VALUES ($1 $2 $3 $4)
                """

        await bot.db.execute(query, self.message_id, self.guild_id, self.author_id, self.channel_id)

        