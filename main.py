# librerias
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from routers import sensordata

app = FastAPI()  # Crear una instancia de la aplicación FastAPI

app.title = "UdeA - IOT API"  # Establecer el título de la aplicación
app.version = "1.0.0"  # Establecer la versión de la aplicación

@app.get("/", tags=["Home"])  # Definir una ruta para la página de inicio
def home():
    """
    Página de inicio de la API.
    """
    return PlainTextResponse("IOT API\nversion:1.0.0\nAuthor:Santiago Ruiz\nCopyright 2024")

app.include_router(prefix="/sensordata", router=sensordata.router)  # Incluir el enrutador sensordata con un prefijo "/sensordata"

