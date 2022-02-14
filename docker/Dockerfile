FROM rust:alpine

LABEL version="0.0.1" maintainer="Asthowen<contact@asthowen.fr>"

RUN apk update && apk upgrade && apk add build-base gcc perl

WORKDIR "/discordbotpihole"

COPY ./ /discordbotpihole

RUN cargo build --release

ENTRYPOINT ./target/release/discord_bot_pihole