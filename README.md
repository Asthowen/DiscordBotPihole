# DiscordBotPihole
A discord bot for get Pi-hole stats.

## Made with
* [**discord.py**](https://pypi.org/project/discord.py/)
* [**psutil**](https://pypi.org/project/psutil/)
* [**aiohttp**](https://pypi.org/project/aiohttp/)

## Use
### Create a discord application
* Go to https://discord.com/developers/applications
* Click on "New Application"
* Enter AppName and then click on "Create"

### Create Bot and enable intents
* Click on "Bot", then click on "Add Bot", then "Yes, do it"
* Copy the bot token

### Install prerequisites
* Execute command : ``pip3 install discord.py psutil``
* Download project : ``git clone https://github.com/Asthowen/DiscordBotPihole.git`` or [zip](https://github.com/Asthowen/DiscordBotPihole/archive/master.zip). 

### Add token to bot
* Go to bot folder (DiscordBotPihole)
* Open file config.json in config/config.json
* On token key paste the token

Ex : 
```json
{
    "token": "theToken",
    "prefix": "&",
    "pi_hole_web_address": "",
    "channel": "",
    "message": ""
}
```

### Launch
* Execute command : ``python3 Main.py``

## Author
[<img width="64" src="https://avatars3.githubusercontent.com/u/59535754?s=400&u=48aecdd175dd2dd8867ae063f1973b64d298220b&v=4" alt="Asthowen">](https://github.com/Asthowen)

## License
**[DiscordBotPihole](https://github.com/Asthowen/DiscordBotPihole) | [Mozilla Public License 2.0](https://github.com/Asthowen/DiscordBotPihole/blob/master/LICENSE)**