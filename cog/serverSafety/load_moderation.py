import json

def load_moderation():
    with open('settings/moderation.json', 'r') as f:
        return json.load(f)