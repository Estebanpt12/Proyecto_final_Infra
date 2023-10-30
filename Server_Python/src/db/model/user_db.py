from user import User

def user_db(user : User) -> dict:
  return user.model_dump()

def user_db_list(users):
  lista_usuarios=[]
  for u in users:
    lista_usuarios.append(user_db(u))
  return lista_usuarios

usuario = User(
    _id=1,
    nombre="Ejemplo",
    documento=12345,
    contrasenia="password123",
    email="ejemplo@example.com",
    telefono=123456789,
    esta_logueado=True
)

print(user_db(usuario)["_id"])