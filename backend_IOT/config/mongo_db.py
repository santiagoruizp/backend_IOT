# librerias
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# URI de la base de datos MongoDB
uri = "mongodb+srv://santiagoruizp:NkDzXa3vfCoZjMSW@cluster0.kcsmfwl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Crear un nuevo cliente y conectarse al servidor
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Database_PF_IOT"]
collection = db["Collection_PF_IOT"]