from discord.ext import commands
import discord
import Utils


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('-------------------------------------------------------')
        print('|               DiscordBotPihole is on                |')
        print('-------------------------------------------------------')
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(
            name=f"Prefix : {Utils.get_property_in_json_file('config/config.json', 'prefix')}"))


def setup(bot):
    bot.add_cog(OnReady(bot))
