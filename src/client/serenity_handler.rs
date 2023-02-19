use crate::commands::{infos::infos, message_updater::update_message};
use serenity::{
    async_trait,
    client::{Context, EventHandler},
    model::{
        application::command::Command,
        application::interaction::{
            application_command::ApplicationCommandInteraction, Interaction,
        },
        gateway::Ready,
        id::GuildId,
        prelude::Activity,
        Permissions,
    },
    prelude::SerenityError,
};

pub struct SerenityHandler;

#[async_trait]
impl EventHandler for SerenityHandler {
    async fn cache_ready(&self, ctx: Context, _guilds: Vec<GuildId>) {
        log::info!("DiscordBotPiHole cache built!");

        let mut pi_hole_url: String = std::env::var("PI_HOLE_URL").unwrap();
        let pi_hole_last_char: char = match pi_hole_url.chars().last() {
            None => {
                log::error!(
                    "An error occurred while parsing the Pi-Hole URL. You must enter a valid URL."
                );
                std::process::exit(1);
            }
            Some(last_char) => last_char,
        };
        pi_hole_url = if pi_hole_last_char.to_string() == "/" {
            pi_hole_url
        } else {
            pi_hole_url + "/"
        };
        pi_hole_url += "admin/api.php";

        let channel_id: u64 = match std::env::var("CHANNEL_ID") {
            Ok(channel_id) => match channel_id.parse::<u64>() {
                Ok(channel_id) => channel_id,
                Err(error) => {
                    log::error!("An error occurred while parsing the channel ID: {}", error);
                    std::process::exit(1);
                }
            },
            Err(error) => {
                log::error!(
                    "An error occurred while converting the channel ID: {}",
                    error
                );
                std::process::exit(1);
            }
        };

        tokio::spawn(async move {
            loop {
                update_message(&ctx, &pi_hole_url, &channel_id).await;

                tokio::time::sleep(std::time::Duration::from_secs(60)).await;
            }
        });
    }
    async fn ready(&self, ctx: Context, _ready: Ready) {
        log::info!("DiscordBotPiHole is connected!");

        ctx.set_activity(Activity::watching("pi-hole.net")).await;

        self.create_commands(&ctx).await;
    }
    async fn interaction_create(&self, ctx: Context, interaction: Interaction) {
        if let Interaction::ApplicationCommand(mut command) = interaction {
            self.run_command(&ctx, &mut command).await.unwrap();
        }
    }
}

impl SerenityHandler {
    async fn run_command(
        &self,
        ctx: &Context,
        command: &mut ApplicationCommandInteraction,
    ) -> Result<(), SerenityError> {
        match command.data.name.as_str() {
            "infos" => infos(ctx, command).await,
            _ => unreachable!(),
        }
        .unwrap();

        Ok(())
    }
    async fn create_commands(&self, ctx: &Context) -> Vec<Command> {
        Command::set_global_application_commands(&ctx.http, |commands| {
            commands.create_application_command(|command| {
                command
                    .name("infos")
                    .description("Display information about the bot.")
                    .default_member_permissions(Permissions::USE_SLASH_COMMANDS)
            })
        })
        .await
        .unwrap()
    }
}
