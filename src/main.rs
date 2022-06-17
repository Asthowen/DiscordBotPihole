use discord_bot_pihole::utils::exit_if_keys_not_exist;
use discord_bot_pihole::client::discord_client::Client;
use simple_logger::SimpleLogger;
use std::error::Error;
use log::LevelFilter;


#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let logger = SimpleLogger::new()
        .with_level(LevelFilter::Off)
        .with_module_level("discord_bot_pihole", LevelFilter::Info)
        .with_colors(true).with_utc_timestamps().init();
    if let Err(error) = logger {
        log::error!("An error occurred during the initialization of the logger: {}", error);
        std::process::exit(1);
    }

    if !std::path::Path::new(".env").exists() {
        log::error!("The .env file does not exist.");
        std::process::exit(1);
    }
    dotenv::dotenv().ok();
    exit_if_keys_not_exist(&["DISCORD_TOKEN", "DISCORD_APP_ID", "PI_HOLE_URL", "CHANNEL_ID"]);

    log::info!("Start DiscordBotPiHole...");

    let mut bot_client: Client = Client::new().await?;
    let bot_task = tokio::spawn(async move {
        if let Err(error) = bot_client.start().await {
            log::error!("An error occurred during the initialization of the bot: {}", error);
            std::process::exit(1);
        }
    });

    if let Ok(()) = tokio::signal::ctrl_c().await {}
    bot_task.abort();
    log::warn!("Program stopped by the user.");

    Ok(())
}