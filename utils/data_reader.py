import json

def load_users():
    with open("data/users.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)