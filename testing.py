import json
with open('system/database/client.json', 'r') as f:
    data = json.load(f)
    for i in data:
        d = i["time"]
        users = [str(e["user"]) for e in data]
        seats = [str(i["seat"])for i in data]
        g = (", ".join(users))
        j = (", ".join(seats))
        print(j)