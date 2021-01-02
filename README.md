# DiscordBotPihole
A discord bot for get Pi-hole stats.

## Made with

* [**discord.py**](https://pypi.org/project/discord.py/)
* [**psutil**](https://pypi.org/project/psutil/)

## Use

### Create an discord application

* Go to https://discord.com/developers/applications
* Click on "New Application"
* Enter AppName and then click on "Create"

### Create bot and enable intents

* Click on "Bot", then click on "Add Bot", then "Yes, do it"
* Copy the bot token

### Add token to bot

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

## Author

[<img width="64" src="https://avatars3.githubusercontent.com/u/59535754?s=400&u=48aecdd175dd2dd8867ae063f1973b64d298220b&v=4" alt="Asthowen">](https://github.com/Asthowen)