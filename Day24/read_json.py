import json

data = {
    "president": {
        "name": "Zaphod",
        "species": "Betelguesian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)