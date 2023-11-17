from utilities.qr import generar_codigo_qr
from utilities.encription import encrypt_text
from db.init import *
from exceptions.ResponseException import ResponseException


def generate_qr_user(documento: str, contrasenia: str):
  try:
    encrypted_contrasenia = encrypt_text(contrasenia)
    encrypted_documento = encrypt_text(documento)
    user = find_user_by_documento_contrasenia(int(documento), encrypted_contrasenia)
  except Exception as e:
    raise ("QR invalido")
  
  if user is None:
    raise ResponseException("Usuario no encontrado")
  
  ruta = (f"images/codigo_qr_{documento}.png")
  generar_codigo_qr(encrypted_documento, ruta)
  
  return ruta

try:
  response = generate_qr_user("143229910", "DEL371")
except ResponseException as r:
  print(r)