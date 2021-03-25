from discord.ext import commands, tasks
from utils import utils
import discord
import psutil
import time


def setup(bot):
    bot.add_cog(Stats(bot))


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('DiscordBotPi-hole is on')

        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(
            name=f"Prefix : {utils.get_property('prefix')}"))

        self.pi_hole_stats.start()

    @tasks.loop(seconds=5)
    async def pi_hole_stats(self):
        channel_id = utils.get_property('channel')
        pi_hole_web_address = utils.get_property('pi_hole_web_address')

        if channel_id == '' or pi_hole_web_address == '':
            return
        else:
            channel = self.bot.get_channel(id=int(channel_id))

        embed = discord.Embed(
            colour=utils.embed_color(),
            title='Stats :'
        )
        embed.add_field(name="Requetes Aujourd'hui :", value=f"`{str(utils.get_response('dns_queries_today'))}`",
                        inline=True)
        embed.add_field(name='Nombre de domaines bloqués :',
                        value=f"`{str(utils.get_response('domains_being_blocked'))}`", inline=True)
        embed.add_field(name='** **', value='** **', inline=False)
        embed.add_field(name='Pub bloquées :', value=f"`{str(utils.get_response('ads_blocked_today'))}`",
                        inline=True)
        embed.add_field(name='Pourcentage de pub :',
                        value=f"`{str(round(int(utils.get_response('ads_percentage_today'))))}%`", inline=True)
        embed.add_field(name='** **', value='** **', inline=False)
        embed.add_field(name='Nombre de clients :', value=f"`{str(utils.get_response('unique_clients'))}`",
                        inline=True)
        embed.add_field(name='Total nombre de clients :',
                        value=f"`{str(utils.get_response('clients_ever_seen'))}`", inline=True)
        embed.add_field(name='** **', value='** **', inline=False)
        embed.add_field(name='PC Stats :', value='** **', inline=False)
        embed.add_field(name='** **', value='** **', inline=False)
        embed.add_field(name='CPU Usage : ', value=f'`{psutil.cpu_percent()} %`', inline=True)
        embed.add_field(name='Ping : ', value=f'`%i ms`' % round(self.bot.latency * 1000), inline=True)
        embed.add_field(name='RAM :',
                        value=f'`{round(psutil.virtual_memory().used / 1000000)}/{round(psutil.virtual_memory().total / 1000000)}mo`',
                        inline=True)
        embed.set_footer(text='Dernière update : ' + time.strftime('%d/%m/%y - %H:%M:%S', time.localtime()))

        message = utils.get_property('message')

        if message == '':
            message = await channel.send(embed=embed)
            utils.write_property('message', message.id)
        else:
            message = await channel.fetch_message(id=int(message))
            await message.edit(embed=embed)
