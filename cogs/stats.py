from discord.ext import commands, tasks
from utils import utils
import discord
import aiohttp
import psutil
import time


def setup(bot):
    bot.add_cog(Stats(bot))


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('DiscordBotPiHole is on!')

        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Game(
                name=f"Prefix : {utils.get_property('prefix')}"
            )
        )

        self.pi_hole_stats.start()

    @tasks.loop(seconds=25)
    async def pi_hole_stats(self):
        channel_id = utils.get_property('channel')
        pi_hole_web_address = utils.get_property('pi_hole_web_address')

        if not channel_id or not pi_hole_web_address:
            return
        else:
            channel = self.bot.get_channel(id=int(channel_id))

        url = utils.get_property('pi_hole_web_address')

        async with aiohttp.ClientSession() as s:
            async with s.get(url + 'admin/api.php' if url[-1] == '/' else url + '/admin/api.php') as r:
                if r.status == 200:
                    content = await r.json()
                else:
                    return

        embed = discord.Embed(
            colour=utils.embed_color(),
            title="Pi-Hole Stats :"
        )
        embed.add_field(
            name="Status :",
            value=f"`{content['status'].replace('enabled', 'Activé').replace('disabled', 'Désactivé')}`",
            inline=False
        )
        embed.add_field(
            name="Requêtes aujourd'hui :",
            value=f"`{content['dns_queries_today']}`",
            inline=False
        )
        embed.add_field(
            name="Pub bloquées aujourd'hui :",
            value=f"`{content['ads_blocked_today']}`",
            inline=False
        )
        embed.add_field(
            name="Pourcentage de pub bloquées aujourd'hui :",
            value=f"`{round(content['ads_percentage_today'])}%`",
            inline=False
        )
        embed.add_field(
            name='Nombre de domaines bloqués :',
            value=f"`{content['domains_being_blocked']}`",
            inline=False
        )
        embed.add_field(
            name='Nombre de clients :',
            value=f"`{content['unique_clients']}`",
            inline=True
        )
        embed.add_field(
            name='CPU : ',
            value=f'`{psutil.cpu_percent()}%`',
            inline=False
        )
        embed.add_field(
            name='RAM :',
            value=f'`{round(psutil.virtual_memory().used / 1000000000, 2)}/{round(psutil.virtual_memory().total / 1000000000)}Go`',
            inline=False
        )
        embed.add_field(
            name='Ping : ',
            value=f'`{round(self.bot.latency * 1000)}Ms`',
            inline=False
        )

        embed.set_footer(text=f"Dernière mise à jour • Le {time.strftime('%d/%m/%Y à %H:%M:%S', time.localtime())}")

        message = utils.get_property('message')

        if message == '':
            message = await channel.send(embed=embed)
            utils.write_property('message', message.id)
        else:
            message = await channel.fetch_message(id=int(message))
            await message.edit(embed=embed)
