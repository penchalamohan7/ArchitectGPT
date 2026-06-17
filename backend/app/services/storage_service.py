import json
import os

STORAGE_FOLDER = "storage"

os.makedirs(STORAGE_FOLDER, exist_ok=True)


def save_api(name, data):

    filename = name.replace(".yaml", ".json")

    filepath = os.path.join(STORAGE_FOLDER, filename)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

    return filepath

def load_api(name):

    filename = name.replace(".yaml", ".json")

    filepath = os.path.join(STORAGE_FOLDER, filename)

    with open(filepath, "r") as f:
        return json.load(f)

def set_current_api(name):

    with open(os.path.join(STORAGE_FOLDER, "current_api.txt"), "w") as f:
        f.write(name)

def get_current_api():

    with open(os.path.join(STORAGE_FOLDER, "current_api.txt"), "r") as f:
        return f.read().strip()