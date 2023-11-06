from init import *
import json

with open('Server_Python/src/db/data.json', 'r') as json_file:
    data_to_insert = json.load(json_file)

insert_many(data_to_insert)