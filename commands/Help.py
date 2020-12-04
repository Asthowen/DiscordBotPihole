from discord.ext import commands
import discord
import Utils
import time


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=Utils.embed_color())
        embed.set_author(name="Commandes de DiscordBotPihole :")
        embed.add_field(name="Prefix", value=f"`set prefix <prefix>`", inline=False)
        embed.add_field(name="PiHole url :", value=f"`set url <PiHole url>`", inline=False)
        embed.add_field(name="Channel :", value=f"`set channel <channel>`", inline=False)
        embed.set_footer(icon_url=ctx.guild.icon_url,
                         text=f"Demandé par {ctx.author.display_name} • Aujourd'hui à {time.strftime('%H:%M:%S', time.localtime())}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Settings(bot))
