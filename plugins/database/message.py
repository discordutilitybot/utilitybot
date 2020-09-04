from .user import User
from .database import Database
import discord 
from discord import Guild, Message, User

class Message(object):

    def __init__(self, bot, message_id: int, channel_id: int, guild_id: int, author_id: int):
        self.bot = bot
        self.message_id = message_id
        self.channel_id = channel_id
        self.guild_id = guild_id
        self.author_id = author_id


    """Query to insert data into the messages table with its rows etc."""
    async def post(self):
        query = """INSERT INTO Messages ( message_id, guild_id, author_id, channel_id )
                VALUES ($1 $2 $3 $4)
                """

        await bot.db.execute(query, self.message_id, self.guild_id, self.author_id, self.channel_id)

    """Would have posted the real message content/object but currently i do not have the money to afford more database space.."""
    
    @classmethod
    async def on_message(cls, bot, message: Discord_Message) -> None:
        user = await bot.db.get_user(message.author.id)  # assure a user gets a row
        self = cls(bot=bot, message_id=message.id, guild_id=message.guild.id, channel_id=message.channel.id, author_id=message.author.id)

        """Use the post function above with the query to insert into the messages table.."""
        await self.post()
        """Update the amount of messages for a user in the message row for the user table"""
        await bot.db.execute('UPDATE users SET messages_sent = messages_sent + 1 WHERE id = $1', user.id)