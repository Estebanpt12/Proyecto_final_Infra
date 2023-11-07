from pydantic import BaseModel

class User(BaseModel):
    id: int
    nombre: str
    documento: int
    contrasenia: str
    email: str
    telefono: float
    esta_logueado:bool