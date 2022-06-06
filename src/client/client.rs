use crate::client::serenity_handler::SerenityHandler;
use serenity::prelude::GatewayIntents;
use std::{env, error::Error};

pub struct Client {
    client: serenity::Client,
}

impl Client {
    pub async fn new() -> Result<Client, Box<dyn Error>> {
        let discord_token = match env::var("DISCORD_TOKEN") {
            Ok(token) => token,
            Err(error) => {
                log::error!("An error occurred while sending the message: {}", error);
                std::process::exit(1);
            }
        };

        let channel_id: u64 = match env::var("DISCORD_APP_ID") {
            Ok(channel_id) => match channel_id.parse::<u64>() {
                Ok(channel_id) => channel_id,
                Err(error) => {
                    log::error!("An error occurred while parsing the Discord app ID: {}", error);
                    std::process::exit(1);
                }
            },
            Err(error) => {
                log::error!("An error occurred while parsing the channel Discord app ID: {}", error);
                std::process::exit(1);
            }
        };

        let intents: GatewayIntents = GatewayIntents::GUILD_MEMBERS | GatewayIntents::GUILD_MESSAGES;
        let client: serenity::Client = serenity::Client::builder(discord_token, intents)
            .event_handler(SerenityHandler)
            .application_id(channel_id)
            .await?;
        Ok(Client { client })
    }

    pub async fn start(&mut self) -> Result<(), serenity::Error> {
        self.client.start().await
    }
}