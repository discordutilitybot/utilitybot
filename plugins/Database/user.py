from discord import Member, User
from .database import Database
import datetime
from datetime import datetime


class User:
    def __init__(self, bot, id: int, *,  messages_sent: int = 0, commands_sent: int = 0, joined_at: datetime = datetime.utcnow()):
        self.bot = bot
        self.id = id
        self.messages_sent = messages_sent
        self.commands_sent = commands_sent
        self.joined_at = joined_at
        # This means everytime it joins the database not the server's.
    

    async def post(self):
        query = "SELECT * from users WHERE id = $1"
        assure_exclusive = await self.bot.db.fetch(query, self.id)
        if len(assure_exclusive) == 0:
            query = "INSERT INTO users ( id, commands_sent, joined_at, messages_sent ) VALUES ( $1, $2, $3, $4 )"
            await bot.db.execute(query, self.id, self.commands_sent, self.messages_sent, self.joined_at)

    # A function to check the amount of commands a user has used

    @classmethod
    async def on_command(cls, bot, user: Union[Member, Discord_User]):

        await bot.db.get_user(self.d) # Make sure a user object is in db
        query = "UPDATE users SET commands_sent = commands_sent +1 WHERE id = $1"
        await bot.db.execute(query, self.id)


