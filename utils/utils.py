import discord
import json


def get_property(value: str):
    with open('utils/config.json', 'r') as f:
        info1 = json.load(f)
    return info1[str(value)]


def write_property(data_category: str, data_to_write: str):
    with open('utils/config.json', 'r') as f:
        value = json.load(f)
    value[str(data_category)] = str(data_to_write)
    with open('utils/config.json', 'w') as f:
        json.dump(value, f, indent=4)


def embed_color():
    return discord.Colour.from_rgb(255, 223, 0)
