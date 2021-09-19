import json


def addUser(new_user):
    f = open("config.json", "r")
    config = json.load(f)
    f.close()
    config["inbounds"][0]["settings"]["clients"] += [new_user.__dict__]
    f = open("config.json", "w")
    json.dump(config, f, indent = 2)
    f.close()