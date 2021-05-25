from discord.ext import commands
from utils import utils
import discord
import os

print("Start DiscordBotPiHole...")

bot = commands.Bot(
    command_prefix=utils.get_property('prefix'),
    intents=discord.Intents.all()
)
bot.remove_command('help')

for filename in os.listdir('cogs'):
    if filename[-3:] == '.py':
        bot.load_extension('cogs.' + filename[:-3])

bot.run(utils.get_property('token'))
