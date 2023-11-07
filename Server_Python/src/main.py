import sys
sys.path.append('/home/esteban/Documents/U/Infra/Proyecto_final_Infra/Server_Python/src')
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import FileResponse
from services.qr_service import generate_qr_user
from exceptions.ResponseException import ResponseException
import os

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload

app = FastAPI()
security = HTTPBasic()

# Ruta para el endpoint que recibe usuario y contraseña
@app.get("/get_image/")
async def get_image(credentials: HTTPBasicCredentials = Depends(security)):
    try:
        response = generate_qr_user(credentials.username, credentials.password)
        if os.path.isfile(response):
            return FileResponse(response)
    except ResponseException as r:
        raise HTTPException(status_code=403, detail=r.args[0])
