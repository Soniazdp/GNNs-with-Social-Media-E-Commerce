import json

with open('test.json', "r") as f:
    data = json.load(f)

dic = {"nails":[] for h in data}

for post in data:
    dic["nails"].append(post["ownerId"])
print(dic)