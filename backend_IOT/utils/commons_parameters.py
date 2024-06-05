#librerias
from fastapi import Depends
from typing import Annotated

def commons_parameters(sortby: str = "None", lastest1st: bool = True, skip: int = 0, limit: int = 0):
    """
    Genera un diccionario de parámetros comunes para filtrar datos.

    Args:
        sortby (str, opcional): Campo por el cual ordenar los resultados. Por defecto, "None".
        lastest1st (bool, opcional): Booleano que indica si los resultados más recientes deben ir primero. Por defecto, True.
        skip (int, opcional): Número de documentos para omitir al consultar la base de datos. Por defecto, 0.
        limit (int, opcional): Número máximo de documentos a devolver. Por defecto, 0 (sin límite).

    Returns:
        dict: Diccionario de parámetros comunes.
    """
    return {"sortby": sortby, "lastest1st": lastest1st, "skip": skip, "limit": limit}

CommonsFilterParams = Annotated[dict, Depends(commons_parameters)]
