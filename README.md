<!--suppress HtmlDeprecatedAttribute -->
<div align="center">
    <h1>DiscordBotPihole</h1>
    <div>
        <a href="https://www.rust-lang.org/">
            <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" alt="Made with Rust">
        </a>
        <a href="https://github.com/Asthowen/DiscordBotPihole">
            <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Use git">
        </a>
        <a href="https://discord.com">
            <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" alt="Discord bot">
        </a>
    </div>
    <h3>
        <strong>A Discord bot for get Pi-Hole stats written in Rust.</strong>
    </h3>
</div>

## Usage
To use this bot you must create a Discord application.

Create a Discord application:

* Go to Discord Developers [Applications](https://discord.com/developers/applications) page.
* Click on "**New Application**".
* Enter a name for your application in the "**Name**" field.
* Click on "**Create**".

Create a bot user:
* On the page for your application, click on menu "**Bot**" and then click on button "**Add Bot**".
* Click "**Yes, do it!**" when popup appeared.
* Now that your bot is created, click on button "Copy" under token section to copy your bot's token, keep this token.

## Installation
### Manually
Start by cloning the repo:
```bash
git clone https://github.com/Asthowen/DiscordBotPihole.git
```
**For the next step you need to have Rust and cargo installed on your PC, for that follow the [official documentation](https://www.rust-lang.org/tools/install).**

Now switch to project folder and compile a release:
```bash
cd DiscordBotPihole && cargo build --release
```

Your executable will be in the `target/release/` folder, it is named `discord_bot_pihole`.

### Docker
Start by cloning the repo:
```bash
git clone https://github.com/Asthowen/DiscordBotPihole.git
```

Now switch to project folder and build the container with docker-compose:
```bash
cd DiscordBotPihole && docker-compose -f ./docker/docker-compose.yml up -d --build
```

### With release
This repo contains compiled bot executables for Windows and Linux, you can find them [here](https://github.com/Asthowen/DiscordBotPihole/releases/latest).
<br>
You just need to download and launch it according to your operating system.

## Configuration
To configure this bot, just use the example configuration: [`.env.example`](https://github.com/Asthowen/DiscordBotPihole/blob/main/.env.example), you just have to rename it to `.env` and complete it.

## Author
[<img width="45" src="https://avatars3.githubusercontent.com/u/59535754?s=400&u=48aecdd175dd2dd8867ae063f1973b64d298220b&v=4" alt="Asthowen">](https://github.com/Asthowen)

## License
**[DiscordBotPihole](https://github.com/Asthowen/DiscordBotPihole) | [Mozilla Public License 2.0](https://github.com/Asthowen/DiscordBotPihole/blob/main/LICENSE)**