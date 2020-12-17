import asyncio
import discord
from discord.ext import commands
from operator import itemgetter
import base64
import binascii
import re
from Cogs import Nullify


class Morse(commands.Cog):

	def __init__(self, bot, settings):
		self.bot = bot
		self.settings = settings
		self.to_morse = { 
			"a" : ".-",
			"b" : "-...",
			"c" : "-.-.",
			"d" : "-..",
			"e" : ".",
			"f" : "..-.",
			"g" : "--.",
			"h" : "....",
			"i" : "..",
			"j" : ".---",
			"k" : "-.-",
			"l" : ".-..",
			"m" : "--",
			"n" : "-.",
			"o" : "---",
			"p" : ".--.",
			"q" : "--.-",
			"r" : ".-.",
			"s" : "...",
			"t" : "-",
			"u" : "..-",
			"v" : "...-",
			"w" : ".--",
			"x" : "-..-",
			"y" : "-.--",
			"z" : "--..",
			"1" : ".----",
			"2" : "..---",
			"3" : "...--",
			"4" : "....-",
			"5" : ".....",
			"6" : "-....",
			"7" : "--...",
			"8" : "---..",
			"9" : "----.",
			"0" : "-----"
			}


	def suppressed(self, guild, msg):
		if self.settings.getServerStat(guild, "SuppressMentions"):
			return Nullify.clean(msg)
		else:
			return msg
		
		
	@commands.command(pass_context=True)
	async def morse(self, ctx, *, content = None):
		"""ascii to morse code"""

		if content == None:
			await ctx.send("Usage `{}morse [content]`".format(ctx.prefix))
			return

		word_list = content.split()
		morse_list = []
		for word in word_list:
			letter_list = []
			for letter in word:
				if letter.lower() in self.to_morse:
					letter_list.append(self.to_morse[letter.lower()])
			if len(letter_list):
				morse_list.append(" ".join(letter_list))
			
		if not len(morse_list):
			await ctx.send("There were no valid a-z/0-9 characters in the passed content.")
			return

		msg = "    ".join(morse_list)
		msg = "```\n" + msg + "```"
		await ctx.send(self.suppressed(ctx.guild, msg))


	@commands.command(pass_context=True)
	async def unmorse(self, ctx, *, content = None):
		"""morse code to ascii"""

		if content == None:
			await ctx.send("Usage `{}unmorse [content]`".format(ctx.prefix))
			return

		word_list = content.split("    ")
		ascii_list = []
		for word in word_list:
			letter_list = word.split()
			letter_ascii = []
			for letter in letter_list:
				for key in self.to_morse:
					if self.to_morse[key] == letter:
						letter_ascii.append(key.upper())
			if len(letter_ascii):
				ascii_list.append("".join(letter_ascii))
			
		if not len(ascii_list):
			await ctx.send("There were no valid morse characters in the passed content.")
			return

		msg = " ".join(ascii_list)
		msg = "```\n" + msg + "```"
		await ctx.send(self.suppressed(ctx.guild, msg))

def setup(bot):
    bot.add_cog(Morse(bot))
    bot.logging.info("Loaded cog!")