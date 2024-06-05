# librerias
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from typing import List
from bson.objectid import ObjectId
from config.mongo_db import collection
from models.sensordata_model import SensorData
from utils.database_utils import filter_db_ordered
from utils.commons_parameters import CommonsFilterParams

router = APIRouter()  # Inicializar el enrutador

@router.get("/", tags=["Sensor Data"])
def get_all_sensor_data(kargs: CommonsFilterParams) -> List[SensorData]:
    """
    Obtener todos los datos del sensor filtrados según los parámetros comunes.

    Args:
        kargs (CommonsFilterParams): Parámetros comunes de filtrado.

    Returns:
        List[SensorData]: Lista de datos del sensor.
    """
    cursor = collection.find({})
    data = list(filter_db_ordered(cursor, **kargs))
    for d in data:
        d["_id"] = str(d["_id"])

    return data

@router.get("/lastest", tags=["Sensor Data"])
def get_latest_sensor_data() -> List[SensorData]:
    """
    Obtener los datos del sensor más recientes.

    Returns:
        List[SensorData]: Lista de datos del sensor más recientes.
    """
    latest_data = collection.find_one({}, sort=[("date", -1)])
    return [latest_data]  

@router.get("/measurement", tags=["Sensor Data"])
def get_sensor_data_by_measurement(measurement_name: str) -> List[SensorData]:
    """
    Obtener los datos del sensor por nombre de medición.

    Args:
        measurement_name (str): Nombre de la medición.

    Returns:
        List[SensorData]: Lista de datos del sensor filtrados por nombre de medición.
    """
    cursor = collection.find({"measurement_name": measurement_name})
    data = list(filter_db_ordered(cursor))
    for d in data:
        d["_id"] = str(d["_id"])

    return data

@router.get("/{id}", tags=["Sensor Data"])
def get_sensordata(_id: str) -> SensorData:
    """
    Obtener los datos del sensor por ID.

    Args:
        _id (str): Identificador único del documento en la base de datos.

    Returns:
        SensorData: Datos del sensor.
    """
    data = list(collection.find({"_id": ObjectId(_id)}))[0]
    data["_id"] = str(data["_id"])
    return data

