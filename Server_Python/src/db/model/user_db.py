def user_db(user) -> dict:
  return {
        "id": user["_id"],
        "nombre": user["nombre"],
        "documento": user["documento"],
        "contrasenia": user["contrasenia"],
        "email": user["email"],
        "telefono": user["telefono"],
        "esta_logueado": user["estaLogueado"]
    }

def user_db_list(users):
  lista_usuarios=[]
  for u in users:
    lista_usuarios.append(user_db(u))
  return lista_usuarios

# usuario = User(
#     id=1,
#     nombre="Ejemplo",
#     documento=12345,
#     contrasenia="password123",
#     email="ejemplo@example.com",
#     telefono=123456789,
#     esta_logueado=True
# )

# print(user_db(usuario))