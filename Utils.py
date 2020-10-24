import discord
import urllib, json


def get_response(key):
    url = get_property_in_json_file("config/config.json", "pi_hole_web_address")
    open_url = urllib.request.urlopen(url + "admin/api.php" if url[-1] == "/" else url + "/admin/api.php")
    if open_url.getcode() == 200:
        data = open_url.read()
        json_data = json.loads(data)
    else:
        print("UNE FUCKING ERREUR EST SURVENUE !", open_url.getcode())
    return json_data[key]


def get_property_in_json_file(file, value):
    with open(file, 'r') as f:
        info1 = json.load(f)
    return info1[str(value)]


def write_property_in_json_file(file, data_categorie, data_for_write):
    with open(file, 'r') as f:
        value = json.load(f)
    value[str(data_categorie)] = str(data_for_write)
    with open(file, 'w') as f:
        json.dump(value, f, indent=4)

def embedColor():
    return discord.Colour.from_rgb(255, 223, 0)