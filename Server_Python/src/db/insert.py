import sys
sys.path.append('/home/esteban/Documents/U/Infra/Proyecto_final_Infra/Server_Python/src')
from init import *
import json
from utilities.encription import encrypt_text

with open('Server_Python/src/db/data.json', 'r') as json_file:
    data_to_insert = json.load(json_file)

for object in data_to_insert:
    object["contrasenia"] = encrypt_text(object["contrasenia"])

insert_many(data_to_insert)