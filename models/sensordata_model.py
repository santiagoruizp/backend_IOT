# librerias
from pydantic import BaseModel, Field

# Definir una clase SensorData para representar los datos del sensor
class SensorData(BaseModel):
    _id: str  # Identificador único del documento en la base de datos
    temperatura_1: float = Field(alias="Temperatura 1 (°C)")  # Temperatura registrada por el sensor 1 en grados Celsius
    temperatura_2: float = Field(alias="Temperatura 2 (°C)")  # Temperatura registrada por el sensor 2 en grados Celsius
    temperatura_3: float = Field(alias="Temperatura 3 (°C)")  # Temperatura registrada por el sensor 3 en grados Celsius
    voltaje_1: float = Field(alias="Voltaje 1 (V)")  # Voltaje medido por el sensor 1 en voltios
    voltaje_2: float = Field(alias="Voltaje 2 (V)")  # Voltaje medido por el sensor 2 en voltios
    measurement_name: str  # Nombre de la medición realizada
    device: str  # Dispositivo que realizó la medición
    date: str  # Fecha de la medición en formato de cadena de texto