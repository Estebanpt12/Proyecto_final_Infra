from pymongo import MongoClient
import sys
sys.path.append('/home/esteban/Documents/U/Infra/Proyecto_final_Infra/Server_Python/src')
from db.model.user_db import user_db

from db.model.user import User

MONGO_URI = 'mongodb://root:password@localhost/admin'

client = MongoClient(MONGO_URI)

db = client['uq']
collection = db['users']

def find_user_by_documento(documento: int):
    user = collection.find_one({ "documento": documento })
    if user is not None:
      return(User(**user_db(user)))
    else:
       return user
    
def find_user_by_documento_contrasenia(documento: int, contrasenia: str):
    user = collection.find_one({ "documento": documento, "contrasenia" : contrasenia })
    if user is not None:
      return(User(**user_db(user)))
    else:
       return user
    
def replace_user(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    user_replaced = collection.find_one_and_replace(
        {"_id": user.id}, user_dict)
    return user_replaced

def insert_many(users):
  return collection.insert_many(users)

