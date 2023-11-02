
import sys
sys.path.append('/home/esteban/Documents/U/Infra/Proyecto_final_Infra/Server_Python/src')

from utilities.encription import decrypt_text
from db.init import *

def enter_user_with_qr(document_encrypted: str):
  try:
    document = decrypt_text(document_encrypted)
  except Exception as e:
    return {"error": "QR invalido"}
  
  user = find_user_by_documento(int(document))

  if user is None:
    return {"error": "QR invalido"}
  
  if user.esta_logueado:
    return {"error": "El usuario ya se encuentra logueado"}
  
  user.esta_logueado = True
  replace_user(user)

def leave_user_with_qr(document_encrypted: str):
  try:
    document = decrypt_text(document_encrypted)
  except Exception as e:
    return {"error": "QR invalido"}
  
  user = find_user_by_documento(int(document))

  if user is None:
    return {"error": "QR invalido"}
  
  if not user.esta_logueado:
    return {"error": "El usuario se encuentra fuera de la institucion"}
  
  user.esta_logueado = True
  replace_user(user)

  return {"sucess" : "Sesion cerrada de usuario"}

qr = "gAAAAABlRANJSPuT78kSxvqgDlgXhglK_hDDuJtV2Ayq_WoTmLjtFIzmL4u1wN6thvLUczDfEp6lO_-LR9gA03OZrY-cUgQYcg=="
print(enter_user_with_qr(qr))
  
