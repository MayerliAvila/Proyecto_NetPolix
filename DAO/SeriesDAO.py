import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion_bd.conexionBD import obtener_conexion

def findAllSeries():
    conn = obtener_conexion()
    c = conn.cursor()

    query = """
        SELECT s.id_serie, s.titulo, s.sinopsis, s.temporada,
               GROUP_CONCAT(v.titulo_original SEPARATOR ', ')
        FROM SERIES s
        LEFT JOIN VIDEOS v ON s.id_serie = v.id_serie
        GROUP BY s.id_serie, s.titulo, s.sinopsis, s.temporada
    """

    c.execute(query)
    resultados = c.fetchall()

    print("\nid_serie | titulo | sinopsis | temporada | videos")
    print("-" * 90)

    for fila in resultados:
        id_serie, titulo, sinopsis, temporada, videos = fila
        print(f"{id_serie} | {titulo} | {sinopsis} | {temporada} | {videos}")

    conn.close()
def crearSerie(id_serie, titulo, sinopsis, temporada):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = """
            INSERT INTO SERIES (id_serie, titulo, sinopsis, temporada)
            VALUES (%s, %s, %s, %s)
        """
        c.execute(query, (id_serie, titulo, sinopsis, temporada))
        conn.commit()
        print(f"✅ Serie '{titulo}' creada correctamente")
    except Exception as e:
        print("❌ Error al crear serie:", e)
    finally:
        conn.close()
def editarSerie(id_serie, titulo, sinopsis, temporada):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = """
            UPDATE SERIES
            SET titulo = %s, sinopsis = %s, temporada = %s
            WHERE id_serie = %s
        """
        c.execute(query, (titulo, sinopsis, temporada, id_serie))
        conn.commit()
        print(f"✅ Serie '{titulo}' actualizada correctamente")
    except Exception as e:
        print("❌ Error al actualizar serie:", e)
    finally:
        conn.close()
def eliminarSerie(id_serie):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "DELETE FROM SERIES WHERE id_serie = %s"
        c.execute(query, (id_serie,))
        conn.commit()
        print(f"✅ Serie con ID '{id_serie}' eliminada correctamente")
    except Exception as e:
        print("❌ Error al eliminar serie:", e)
    finally:
        conn.close()
