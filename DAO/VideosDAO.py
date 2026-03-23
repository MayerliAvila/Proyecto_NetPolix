import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion_bd.conexionBD import obtener_conexion

def findAllVideos():
    conn = obtener_conexion()
    c = conn.cursor()
    query = """SELECT * FROM VIDEOS"""
    c.execute(query)
    videos = c.fetchall()
    for video in videos:
        print(video)
    conn.close()

def crearVideo(isan, titulo_original, anio_produccion, duracion_min, id_clasificacion, id_serie):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = """
            INSERT INTO VIDEOS (isan, titulo_original, anio_produccion, duracion_min, id_clasificacion, id_serie)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        c.execute(query, (isan, titulo_original, anio_produccion, duracion_min, id_clasificacion, id_serie))
        conn.commit()
        print(f"✅ Video '{titulo_original}' creado correctamente")
    except Exception as e:
        print("❌ Error al crear video:", e)
    finally:
        conn.close()

def editarVideo(isan, titulo_original, anio_produccion, duracion_min, id_clasificacion, id_serie):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = """
            UPDATE VIDEOS
            SET titulo_original = %s, anio_produccion = %s, duracion_min = %s, id_clasificacion = %s, id_serie = %s
            WHERE isan = %s
        """
        c.execute(query, (titulo_original, anio_produccion, duracion_min, id_clasificacion, id_serie, isan))
        conn.commit()
        print(f"✅ Video '{titulo_original}' actualizado correctamente")
    except Exception as e:
        print("❌ Error al actualizar video:", e)
    finally:
        conn.close()
def eliminarVideo(isan):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "DELETE FROM VIDEOS WHERE isan = %s"
        c.execute(query, (isan,))
        conn.commit()
        print(f"✅ Video con ISAN '{isan}' eliminado correctamente")
    except Exception as e:
        print("❌ Error al eliminar video:", e)
    finally:
        conn.close()
def buscarVideoPorISAN(isan):
    conn = obtener_conexion()
    c = conn.cursor()
    query = "SELECT * FROM VIDEOS WHERE isan = %s"
    c.execute(query, (isan,))
    video = c.fetchone()
    conn.close()
    return video
def mostrarSoloISAN():
    conn = obtener_conexion()
    c = conn.cursor()
    query = "SELECT isan FROM VIDEOS"
    c.execute(query)
    videos = c.fetchall()
    for video in videos:
        print(video[0])  # Imprime solo el ISAN
    conn.close()
def mostrarViculacionCategoriasPorVideo(isan):
    conn = obtener_conexion()
    c = conn.cursor()
    query = """
        SELECT c.id_categoria, c.nombre
        FROM CATEGORIAS c
        JOIN VIDEOS_CATEGORIAS vc ON c.id_categoria = vc.id_categoria
        WHERE vc.id_video = %s
    """
    c.execute(query, (isan,))
    categorias = c.fetchall()
    print(f"Categorías vinculadas al video con ISAN '{isan}':")
    for categoria in categorias:
        print(categoria)
    conn.close()

def buscarVideoPorNombre(nombre):
    conn = obtener_conexion()
    c = conn.cursor()

    query = "SELECT * FROM VIDEOS WHERE LOWER(titulo_original) LIKE LOWER(%s)"
    c.execute(query, (f"%{nombre}%",))

    videos = c.fetchall()

    if videos:
        print("Videos encontrados:")
        for video in videos:
            print(video)
    else:
        print("No se encontraron videos con ese nombre.")

    conn.close()