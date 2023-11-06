from init import *
import json

with open('Server_Python\data-y1HuOVowWE7MQHE5Xeau-.json', 'r') as json_file:
    data_to_insert = json.load(json_file)

insert_many(data_to_insert)