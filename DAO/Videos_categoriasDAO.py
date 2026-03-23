import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion_bd.conexionBD import obtener_conexion


def vincularVideoCategoria(id_video, id_categoria):
    conn = obtener_conexion()
    c = conn.cursor()

    try:
        # Validar máximo 3 categorías por video
        c.execute("""
            SELECT COUNT(*) 
            FROM VIDEOS_CATEGORIAS 
            WHERE id_video = %s
        """, (id_video,))
        
        total = c.fetchone()[0]

        if total >= 3:
            print("❌ Este video ya tiene 3 categorías (máximo permitido)")
            return

        # Validar que no esté repetida
        c.execute("""
            SELECT * 
            FROM VIDEOS_CATEGORIAS 
            WHERE id_video = %s AND id_categoria = %s
        """, (id_video, id_categoria))

        if c.fetchone():
            print("❌ Esta categoría ya está asignada a este video")
            return

        # Insertar
        query = """
            INSERT INTO VIDEOS_CATEGORIAS (id_video, id_categoria)
            VALUES (%s, %s)
        """
        c.execute(query, (id_video, id_categoria))
        conn.commit()

        print(f"✅ Video con ISAN '{id_video}' vinculado a categoría ID '{id_categoria}' correctamente")

    except Exception as e:
        print("❌ Error al vincular video a categoría:", e)

    finally:
        conn.close()


def editarVinculacionVideoCategoria(id_video, id_categoria, nuevo_id_categoria):
    conn = obtener_conexion()
    c = conn.cursor()

    try:
        # 🔹 Validar que no exista ya esa nueva relación
        c.execute("""
            SELECT * 
            FROM VIDEOS_CATEGORIAS 
            WHERE id_video = %s AND id_categoria = %s
        """, (id_video, nuevo_id_categoria))

        if c.fetchone():
            print("❌ Esa categoría ya está asignada al video")
            return

        query = """
            UPDATE VIDEOS_CATEGORIAS
            SET id_categoria = %s
            WHERE id_video = %s AND id_categoria = %s
        """
        c.execute(query, (nuevo_id_categoria, id_video, id_categoria))
        conn.commit()

        print(f"✅ Video con ISAN '{id_video}' actualizado a categoría ID '{nuevo_id_categoria}' correctamente")

    except Exception as e:
        print("❌ Error al actualizar vinculación video-categoría:", e)

    finally:
        conn.close()


def desvincularVideoCategoria(id_video, id_categoria):
    conn = obtener_conexion()
    c = conn.cursor()

    try:
        query = """
            DELETE FROM VIDEOS_CATEGORIAS 
            WHERE id_video = %s AND id_categoria = %s
        """
        c.execute(query, (id_video, id_categoria))
        conn.commit()

        print(f"✅ Video con ISAN '{id_video}' desvinculado de categoría ID '{id_categoria}' correctamente")

    except Exception as e:
        print("❌ Error al desvincular video de categoría:", e)

    finally:
        conn.close()


def obtenerVideosPorCategoria(id_categoria):
    conn = obtener_conexion()
    c = conn.cursor()

    query = """
        SELECT v.ISAN, v.titulo_original, v.anio_produccion, v.duracion_min, v.id_clasificacion, v.id_serie
        FROM VIDEOS v
        JOIN VIDEOS_CATEGORIAS vc ON v.ISAN = vc.id_video
        WHERE vc.id_categoria = %s
    """
    c.execute(query, (id_categoria,))
    videos = c.fetchall()

    print(f"\n=== VIDEOS DE LA CATEGORIA {id_categoria} ===")
    for video in videos:
        print(video)

    conn.close()