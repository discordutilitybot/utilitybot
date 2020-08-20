from discord import Member, User

from .database import Database
import datetime
from datetime import datetime


class User:
    def __init__(self, bot, id: int, *, messages: List[Message], messages_sent: int = 0, commands_sent: int = 0, joined_at: datetime:= datetime.utcnow()):
        self.bot = bot
        self.id = id
        self.messages = messages
        self.joined_at = joined_at
        # This means everytime it joins the database not the server's.

    