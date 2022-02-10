use crate::utils::current_version;
use serenity::{
    client::Context, prelude::SerenityError, builder::CreateEmbed, builder::CreateEmbedAuthor,
    model::interactions::{
        application_command::ApplicationCommandInteraction, InteractionResponseType,
    },
};

pub async fn infos(
    ctx: &Context, interaction: &mut ApplicationCommandInteraction
) -> Result<(), SerenityError> {
    let mut author = CreateEmbedAuthor::default();
    author.icon_url("https://wp-cdn.pi-hole.net/wp-content/uploads/2016/12/Vortex-R.webp");
    author.name("DiscordBotPiHole");
    let mut description: String = "**[DiscordBotPiHole](https://github.com/Asthowen/DiscordBotPiHole)** is a Discord bot that displays the stats of a Pi-Hole instance in a channel. It will allow other interactions with the API in the future.".to_string();
    description += &*format!("\n\nInstalled version: **{}**", current_version());
    description += "\n\n**Contact me**:\nWebsite: **[asthowen.fr](https://asthowen.fr)**\nEmail: **[contact@asthowen.fr](mailto:contact@asthowen.fr)**\nDiscord: **[Asthowen#9241](https://discord.bio/p/asthowen)**";

    let mut embed = CreateEmbed::default();
    embed.color(0xee171f);
    embed.set_author(author);
    embed.description(description);

    interaction.create_interaction_response(&ctx.http, |response| {
        response
            .kind(InteractionResponseType::ChannelMessageWithSource)
            .interaction_response_data(|message| message.add_embed(embed))
    }).await
}