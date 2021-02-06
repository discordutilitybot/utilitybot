import discord
from discord.ext import commands

import random

class RNG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, num):
        final = random.randint(1, num)
        await ctx.send(final)
    
    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx):
        """ Flips a coin. """
        choices = ["Heads","Tails"]
        result = random.choice(choices)
        await ctx.send(f"You got {result} \U0001fa99.")
    
    @commands.command(name="8ball", aliases=["8b"])
    async def _8ball(self, ctx, *, question):
        """asks the magic 8ball a question"""
        responses = [
  'It is certain', 'It is decidedly so', 'Without a doubt',
  'Yes – definitely', 'You may rely on it', 'As I see it, yes',
  'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 
  'Reply hazy, try again', 'Ask again later', 'Better not tell you now',
  'Better not tell you now', 'Concentrate and ask again', 'Very doubtful',
  "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
]
        answer = random.choice(responses)
        await ctx.send(f"\U0001f3b1 Question for the magic 8ball: {question}\nAnswer: {answer}")
        
def setup(bot):
    bot.add_cog(RNG(bot))
    bot.logging.info('Loaded RNG Commands')
