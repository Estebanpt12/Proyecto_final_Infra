from exceptions.ResponseException import ResponseException
from utilities.encription import decrypt_text
from db.init import *

def enter_user_with_qr(document_encrypted: str):
  try:
    document = decrypt_text(document_encrypted)
  except Exception as e:
    raise ResponseException("QR invalido")
  
  user = find_user_by_documento(int(document))

  if user is None:
    raise ResponseException("Usuario no encontrado")
  
  if user.esta_logueado:
    raise ResponseException("El usuario ya se encuentra logueado")
  
  user.esta_logueado = True
  replace_user(user)

  return "Sesion iniciada de usuario"

def leave_user_with_qr(document_encrypted: str):
  try:
    document = decrypt_text(document_encrypted)
  except Exception as e:
    raise ResponseException("QR invalido")
  
  user = find_user_by_documento(int(document))

  if user is None:
    raise ResponseException("Usuario no encontrado")
  
  if not user.esta_logueado:
    raise ResponseException("El usuario no se encuentra logueado")
  
  user.esta_logueado = False
  replace_user(user)

  return "Sesion cerrada de usuario"
