from discord.ext import commands, tasks
import discord
import psutil
import Utils
import time


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=5)
    async def pi_hole_stats(self):
        channel = self.bot.get_channel(
            id=int(Utils.get_property_in_json_file("config/config.json", "channel")))

        if channel == "" or Utils.get_property_in_json_file("config/config.json", "pi_hole_web_address") == "":
            return

        embed = discord.Embed(
            colour=Utils.embed_color(),
            title="Stats :"
        )
        embed.add_field(name="Requetes Aujourd'hui :", value="`" + str(Utils.get_response("dns_queries_today")) + "`",
                        inline=True)
        embed.add_field(name="Nombre de domaines bloqués :",
                        value="`" + str(Utils.get_response("domains_being_blocked")) + "`", inline=True)
        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name="Pub bloquées :", value="`" + str(Utils.get_response("ads_blocked_today")) + "`",
                        inline=True)
        embed.add_field(name="Pourcentage de pub :",
                        value="`" + str(round(int(Utils.get_response("ads_percentage_today")))) + "%`", inline=True)
        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name="Nombre de clients :", value="`" + str(Utils.get_response("unique_clients")) + "`",
                        inline=True)
        embed.add_field(name="Total nombre de clients :",
                        value="`" + str(Utils.get_response("clients_ever_seen")) + "`", inline=True)
        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name="PC Stats :", value="** **", inline=False)
        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name="CPU Usage : ", value=f"`{psutil.cpu_percent()} %`", inline=True)
        embed.add_field(name="Ping : ", value=f"`%i ms`" % round(self.bot.latency * 1000), inline=True)
        ram_used = round(psutil.virtual_memory().used / 1000000)
        ram_total = round(psutil.virtual_memory().total / 1000000)
        embed.add_field(name="RAM :", value=f"`{ram_used}/{ram_total}mo`", inline=True)
        embed.set_footer(text="Dernière update : " + time.strftime('%d/%m/%y - %H:%M:%S', time.localtime()))

        if Utils.get_property_in_json_file("config/config.json", "message") == "":
            message = await channel.send(embed=embed)
            Utils.write_property_in_json_file("config/config.json", "message", message.id)
        else:
            message = await channel.fetch_message(
                id=int(Utils.get_property_in_json_file("config/config.json", "message")))
            await message.edit(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        self.pi_hole_stats.start()


def setup(bot):
    bot.add_cog(Stats(bot))
