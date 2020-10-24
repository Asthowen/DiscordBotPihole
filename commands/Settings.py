import discord
from discord.ext import commands

import Utils


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set(self, ctx, *args):
        if len(args) == 2:
            if args[0] == "prefix":
                actual_prefix = Utils.get_property_in_json_file("config/config.json", "prefix")
                Utils.write_property_in_json_file("config/config.json", "prefix", args[1])
                await ctx.send(
                    f":white_check_mark: Vous avez correctement modifié le prefix : {actual_prefix} par {args[1]} !")
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=args[1]))
            elif args[0] == "url":
                Utils.write_property_in_json_file("config/config.json", "pi_hole_web_address", args[1])
                await ctx.send(
                    f":white_check_mark: Vous avez correctement définis l'adresse de votre Pi-Hole sur : {args[1]} !")
            elif args[0] == "channel":
                channel = args[1].replace("<", "").replace(">", "").replace("#", "")
                Utils.write_property_in_json_file("config/config.json", "channel", channel)
                await ctx.send(
                    f":white_check_mark: Vous avez correctement définis le channel des stats de Pi-Hole dans : {args[1]} !")
        else:
            await ctx.send(f":x: Cette commande n'existe pas, faite : `{Utils.get_property_in_json_file('config/config.json', 'prefix')}help`")




def setup(bot):
    bot.add_cog(Settings(bot))
