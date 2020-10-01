import json

with open('src/data/players.json') as file_data:
    data = json.loads(str(file_data))

print(data)