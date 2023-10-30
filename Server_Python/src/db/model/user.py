from pydantic import BaseModel

class User(BaseModel):
    _id: int
    nombre: str
    documento: int
    contrasenia: str
    email: str
    telefono: int
    esta_logueado:bool