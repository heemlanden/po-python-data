import json
with open('bestand.json', 'r') as f:
    data = json.load(f)
print(type(data))
