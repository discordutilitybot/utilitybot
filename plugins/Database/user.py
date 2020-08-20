from discord import Member, User

from .database import Database
import datetime
from datetime import datetime


class User:
    def __init__(self, bot, id: int, *, messages: List[Message], messages_sent: int = 0, commands_sent: int = 0, joined_at: datetime = datetime.utcnow()):
        self.bot = bot
        self.id = id
        self.messages = messages
        self.joined_at = joined_at
        # This means everytime it joins the database not the server's.
    
    # Make a function to return the user id and the userid by a string


    # A function to check the amount of commands a user has used

    @classmethod
    async def on_command(cls, bot, user: Union[Member, Discord_User]):
        await bot.db.get_user(user.id)


