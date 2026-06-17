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