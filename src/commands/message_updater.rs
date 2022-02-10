use serenity::{prelude::*, builder::CreateEmbed, model::{id::{ChannelId}}};
use serde_json::Value;

pub async fn update_message(ctx: &Context, pi_hole_url: &String, channel_id: &u64) {
    let response: reqwest::Response = match reqwest::Client::new().get(pi_hole_url).send().await {
        Ok(response) => response,
        Err(error) => {
            log::error!("An error occurred while interacting with the API: {}", error);
            std::process::exit(1);
        }
    };
    let json_value: Value = response.json().await.unwrap();

    let status: &String = &json_value["status"].as_str().unwrap().to_string();
    let status_to_print: String = status[0..1].to_uppercase().to_string() + &status[1..].to_string();

    let mut embed: CreateEmbed = CreateEmbed::default();
    embed.title("Pi-Hole stats:");
    embed.color(0xee171f);
    embed.field("Status:", format!("`{}`", status_to_print),true);
    embed.field("DNS queries today:", format!("`{}`", &json_value["dns_queries_today"]),true);
    embed.field("DNS queries all types:", format!("`{}`", &json_value["dns_queries_all_types"]),true);
    embed.field("Ads blocked today:", format!("`{}`", &json_value["ads_blocked_today"]),true);
    embed.field("Queries forwarded:", format!("`{}`", &json_value["queries_forwarded"]),true);
    embed.field("Queries cached:", format!("`{}`", &json_value["queries_cached"]),true);
    embed.field("Clients ever seen:", format!("`{}`", &json_value["clients_ever_seen"]),true);
    embed.field("Unique clients:", format!("`{}`", &json_value["unique_clients"]),true);
    embed.field("Domains being blocked:", format!("`{}`", &json_value["domains_being_blocked"]),true);
    embed.footer(|f| f.text(chrono::Local::now().format("Last edit the %d/%m/%Y at %H:%M").to_string()));

    if !std::path::Path::new("message-id.txt").exists() {
        log::warn!("The file containing the message ID does not exist. I will send it and save the ID.");

        let msg = ChannelId(*channel_id)
            .send_message(&ctx.http, |m| {
                m.embed(|e| { *e = embed; e } );
                m
            }).await;

        if let Err(error) = msg {
            log::error!("An error occurred while sending the message: {}", error);
        } else {
            let write = tokio::fs::write("message-id.txt", msg.unwrap().id.to_string()).await;
            if let Err(error) = write {
                log::error!("An error occurred while saving message ID in the file: {}", error);
            }
        }
    } else {
        let message_id_string: String = match tokio::fs::read_to_string("message-id.txt").await {
            Ok(message_id) => message_id,
            Err(error) => {
                log::error!("An error occurred while parsing the message ID: {}", error);
                std::process::exit(1);
            }
        };
        let message_id_u64: u64 = match message_id_string.parse::<u64>() {
            Ok(message_id) => message_id,
            Err(error) => {
                log::error!("An error occurred while converting the message ID: {}", error);
                std::process::exit(1);
            }
        };

        let msg = ChannelId(*channel_id)
            .edit_message(&ctx.http,message_id_u64, |m| {
                m.embed(|e| { *e = embed; e } );
                m
            }).await;

        if let Err(error) = msg {
            log::error!("An error occurred while editing the message: {}", error);
        }
    }
}