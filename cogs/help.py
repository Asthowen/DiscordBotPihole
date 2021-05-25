from discord.ext import commands
from utils import utils
import discord
import time


def setup(bot):
    bot.add_cog(Help(bot))


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        prefix = utils.get_property('prefix')

        embed = discord.Embed(color=utils.embed_color())
        embed.set_author(name='Commandes de DiscordBotPihole :')
        embed.add_field(name='Prefix', value=f'`{prefix}set prefix <prefix>`', inline=False)
        embed.add_field(name='PiHole url', value=f'`{prefix}set url <PiHole url>`', inline=False)
        embed.add_field(name='Channel', value=f'`{prefix}set channel <channel>`', inline=False)
        embed.set_footer(
            icon_url=ctx.guild.icon_url,
            text=f"Demandé par {ctx.author.display_name} • Le {time.strftime('%d/%m/%Y à %H:%M:%S', time.localtime())}"
        )
        await ctx.send(embed=embed)
