from discord.ext import commands
import Utils, os


bot = commands.Bot(command_prefix=Utils.get_property_in_json_file("config/config.json", "prefix"))

for filename in os.listdir('commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')
for filename in os.listdir('events'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.{filename[:-3]}')

bot.run(Utils.get_property_in_json_file("config/config.json", "token"))
