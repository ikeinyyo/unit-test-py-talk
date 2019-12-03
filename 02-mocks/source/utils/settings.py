import json


def get_setting(key, default=None):
    try:
        with open("settings.json", "r") as f:
            settings = json.loads(f.read())
            return settings[key]
    except:
        return default
