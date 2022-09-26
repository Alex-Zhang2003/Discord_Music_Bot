import discord
from discord.ext import commands
import os

from music_cog import music_cog
from help_cog import help_cog

token = "MTAwODE0NTY0NjEyNzE2MTQ0NA.GLI3lR.ZoBOzK7CNDFpfBBPgavy1dsbd9cm3GvyXIzWn0"
bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

bot.run(token)


