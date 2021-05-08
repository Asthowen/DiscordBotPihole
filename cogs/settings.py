from discord.ext import commands
from utils import utils
import discord


def setup(bot):
    bot.add_cog(Settings(bot))


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set(self, ctx, *args):
        if len(args) == 2:
            if args[0] == 'prefix':
                actual_prefix = utils.get_property('prefix')
                utils.write_property('prefix', args[1])
                await ctx.send(
                    f':white_check_mark: Vous avez correctement modifié le prefix : {actual_prefix} par {args[1]} !')
                await self.bot.change_presence(
                    status=discord.Status.online,
                    activity=discord.Game(
                        name=f'Prefix : {args[1]}'
                    )
                )
            elif args[0] == 'url':
                utils.write_property('pi_hole_web_address', args[1])
                await ctx.send(
                    f":white_check_mark: Vous avez correctement définis l'adresse de votre Pi-Hole sur : {args[1]} !")
            elif args[0] == "channel":
                try:
                    channel = int(args[1].replace("<", "").replace(">", "").replace("#", ""))
                    channel = discord.utils.get(ctx.guild.text_channels, id=channel)
                except ValueError:
                    return await ctx.send(":x: Ce channel n'existe pas !")
                else:
                    if channel is None:
                        return await ctx.send(":x: Ce channel n'existe pas !")

                    utils.write_property('channel', channel.id)
                    await ctx.send(
                        f':white_check_mark: Vous avez correctement définis le channel des stats de Pi-Hole dans : {args[1]} !')
        else:
            await ctx.send(
                f":x: Cette commande n'existe pas, faites : `{utils.get_property('prefix')}help`")
