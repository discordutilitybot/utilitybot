from discord.ext import commands
import asyncio

def to_emoji(c):
    base = 0x1f1e6
    return chr(base + c)

class Polls(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def poll(self, ctx, *, question):

        messages = [ctx.message]
        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and len(m.content) <= 100

        for i in range(50):
            messages.append(await ctx.send(f"Say poll option or {ctx.prefix}cancel to publish poll."))

            try:
                entry = await self.bot.wait_for("message", check=check, timeout=90.0)
            except asyncio.TimeoutError:
                break

            messages.append(entry)

            if entry.clean_content.startswith(f"{ctx.prefix}cancel"):
                break

            answers.append((to_emoji(i), entry.clean_content))

        try:
            await ctx.channel.delete_messages(messages)
        except:
            pass 

        answer = "\n".join(f"{keycap}: {content}" for keycap, content in answers)
        actual_poll = await ctx.send(f"{ctx.author} asks: {question}\n\n{answer}")
        for emoji, _ in answers:
            await actual_poll.add_reaction(emoji)

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send("Missing the question.")

    @commands.command()
    @commands.guild_only()
    async def quickpoll(self, ctx, *questions_and_choices: str):

        if len(questions_and_choices) < 3:
            return await ctx.send("Need at least 1 question with 2 choices.")
        elif len(questions_and_choices) > 21:
            return await ctx.send("You can only have up to 20 choices.")

        perms = ctx.channel.permissions_for(ctx.me)
        if not (perms.read_message_history or perms.add_reactions):
            return await ctx.send("Need Read Message History and Add Reactions permissions.")

        question = questions_and_choices[0]
        choices = [(to_emoji(e), v) for e, v in enumerate(questions_and_choices[1:])]

        try:
            await ctx.message.delete()
        except discord.HTTPException:
            pass

        body = "\n".join(f"{key}: {c}" for key, c in choices)
        poll = await ctx.send(f"{ctx.author} asks: {question}\n\n{body}")
        for emoji, _ in choices:
            await poll.add_reaction(emoji)

def setup(bot):
    bot.add_cog(Polls(bot))
    bot.logging.info("Loaded poll system!")