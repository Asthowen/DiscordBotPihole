from urllib import request
import discord
import json


def get_response(key: str):
    url = get_property_in_json_file("config/config.json", "pi_hole_web_address")
    open_url = request.urlopen(url + "admin/api.php" if url[-1] == "/" else url + "/admin/api.php")
    json_data = ""

    if open_url.getcode() == 200:
        data = open_url.read()
        json_data = json.loads(data)

    else:
        print("Error : ", open_url.getcode())
    return None if json_data is None else json_data[key]


def get_property_in_json_file(file: str, value: str):
    with open(file, 'r') as f:
        info1 = json.load(f)
    return info1[str(value)]


def write_property_in_json_file(file: str, data_category: str, data_for_write: str):
    with open(file, 'r') as f:
        value = json.load(f)
    value[str(data_category)] = str(data_for_write)
    with open(file, 'w') as f:
        json.dump(value, f, indent=4)


def embed_color():
    return discord.Colour.from_rgb(255, 223, 0)
