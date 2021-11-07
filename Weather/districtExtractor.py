import json

# read json file
with open('files/bd_districts.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(data['districts'][2]['name'])