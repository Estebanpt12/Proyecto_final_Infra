from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import FileResponse
import os

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload

app = FastAPI()
security = HTTPBasic()

# Ruta para el endpoint que recibe usuario y contraseña
@app.get("/get_image/")
async def get_image(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == "usuario" and credentials.password == "contrasenia":
        # Si el usuario y la contraseña son válidos, secdrvir la imagen
        image_path = "images/codigo_qr.png"
        if os.path.isfile(image_path):
            return FileResponse(image_path)
        else:
            raise HTTPException(status_code=404, detail="Imagen no encontrada")
    else:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
