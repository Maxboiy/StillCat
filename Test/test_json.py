import json

with open("config.json", "r") as f:
    data = json.load(f)

for config in data["config"]:
    print(config["max_deployed_cats"])
    print(config["stand_still"])
    
        