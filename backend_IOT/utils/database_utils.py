#librerias
from pymongo import ASCENDING, DESCENDING

def filter_db_ordered(db_cursor, sortby=None, lastest1st=True, skip=0, limit=0):
    """
    Filtra y ordena un cursor de base de datos MongoDB según los parámetros especificados.

    Args:
        db_cursor: Cursor de base de datos MongoDB.
        sortby (str, opcional): Campo por el cual ordenar los resultados. Por defecto, None.
        lastest1st (bool, opcional): Booleano que indica si los resultados más recientes deben ir primero. Por defecto, True.
        skip (int, opcional): Número de documentos para omitir al consultar la base de datos. Por defecto, 0.
        limit (int, opcional): Número máximo de documentos a devolver. Por defecto, 0 (sin límite).

    Returns:
        pymongo.cursor.Cursor: Cursor de base de datos MongoDB filtrado y ordenado.
    """
    valid_sort_fields = ["Temperatura 1 (°C)", "Temperatura 2 (°C)", "Temperatura 3 (°C)", 
                         "Voltaje 1 (V)", "Voltaje 2 (V)", "measurement_name", "device", "date"]
    if sortby in valid_sort_fields:
        db_cursor = db_cursor.sort(sortby, DESCENDING if lastest1st else ASCENDING)
    if skip:
        db_cursor = db_cursor.skip(skip)
    if limit:
        db_cursor = db_cursor.limit(limit)

    return db_cursor

