import json

# read json file
with open('E:\\Pycharm\\FunWithAPIs\\res\\countries.json') as json_file:
    data = json.load(json_file)
    print(data['Canada'])