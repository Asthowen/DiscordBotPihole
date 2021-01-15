from discord.ext import commands
import discord
import Utils


bot = commands.Bot(command_prefix=Utils.get_property_in_json_file("config/config.json", "prefix"), intents=discord.Intents.all())
bot.remove_command('help')

module_to_load = ['commands.Help', 'commands.Settings', 'events.OnReady', 'events.Stats']

for module in module_to_load:
    bot.load_extension(module)


bot.run(Utils.get_property_in_json_file("config/config.json", "token"))
