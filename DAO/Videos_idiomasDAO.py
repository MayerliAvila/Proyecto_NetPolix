import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion_bd.conexionBD import obtener_conexion

def findAllVideos_idioma():
    conn = obtener_conexion()
    c = conn.cursor()

    query = """
        SELECT v.titulo_original, i.nombre, vi.tipo
        FROM VIDEOS_IDIOMAS vi
        JOIN VIDEOS v ON vi.id_video = v.ISAN
        JOIN IDIOMAS i ON vi.id_idioma = i.id_idioma
    """

    c.execute(query)
    videos_idiomas = c.fetchall()

    print("\n=== LISTA DE VIDEOS E IDIOMAS ===")
    print("Titulo Video | Idioma | Tipo")

    for vi in videos_idiomas:
        print(f"{vi[0]} | {vi[1]} | {vi[2]}")

    conn.close()

def vincularVideoIdioma(id_video, id_idioma, tipo):
    conn = obtener_conexion()
    c = conn.cursor(buffered=True)  # 🔥 evita error unread

    try:
        tipo = tipo.lower()

        # 🔹 1. Validar tipo permitido
        if tipo not in ["original", "subtitulos", "doblaje"]:
            print("❌ Tipo inválido. Use: original, subtitulos o doblaje")
            return

        # 🔹 2. Validar que no se repita (idioma + tipo)
        c.execute("""
            SELECT * 
            FROM VIDEOS_IDIOMAS 
            WHERE id_video = %s AND id_idioma = %s AND tipo = %s
        """, (id_video, id_idioma, tipo))

        if c.fetchone():
            print("❌ Este idioma ya está asignado a este video con ese tipo")
            return

        # 🔹 3. Validar ORIGINAL (solo uno)
        if tipo == "original":
            c.execute("""
                SELECT * 
                FROM VIDEOS_IDIOMAS 
                WHERE id_video = %s AND tipo = 'original'
            """, (id_video,))

            if c.fetchone():
                print("❌ Este video ya tiene un idioma original")
                return

        # 🔹 4. Insertar
        query = """
            INSERT INTO VIDEOS_IDIOMAS (id_video, id_idioma, tipo)
            VALUES (%s, %s, %s)
        """
        c.execute(query, (id_video, id_idioma, tipo))
        conn.commit()

        print(f"✅ Video '{id_video}' vinculado con idioma '{id_idioma}' como '{tipo}'")

    except Exception as e:
        print(f"❌ Error al vincular video con idioma: {e}")

    finally:
        conn.close()

def editarVinculacionVideoIdioma(id_video, id_idioma, nuevo_id_idioma, tipo):
    conn = obtener_conexion()
    c = conn.cursor(buffered=True)  # 🔥 evita errores

    try:
        tipo = tipo.lower()

        # 🔹 1. Validar tipo válido
        if tipo not in ["original", "subtitulos", "doblaje"]:
            print("❌ Tipo inválido. Use: original, subtitulos o doblaje")
            return

        # 🔹 2. Validar que exista la vinculación actual
        c.execute("""
            SELECT * 
            FROM VIDEOS_IDIOMAS 
            WHERE id_video = %s AND id_idioma = %s
        """, (id_video, id_idioma))

        if not c.fetchone():
            print("❌ No existe esta vinculación entre video e idioma")
            return

        # 🔹 3. Validar que no exista ya la nueva combinación
        c.execute("""
            SELECT * 
            FROM VIDEOS_IDIOMAS 
            WHERE id_video = %s AND id_idioma = %s AND tipo = %s
        """, (id_video, nuevo_id_idioma, tipo))

        if c.fetchone():
            print("❌ Este nuevo idioma ya está asignado con ese tipo")
            return

        # 🔹 4. Validar ORIGINAL (solo uno)
        if tipo == "original":
            c.execute("""
                SELECT * 
                FROM VIDEOS_IDIOMAS 
                WHERE id_video = %s AND tipo = 'original' AND id_idioma != %s
            """, (id_video, id_idioma))

            if c.fetchone():
                print("❌ Este video ya tiene un idioma original")
                return

        # 🔹 5. Actualizar idioma y tipo
        query = """
            UPDATE VIDEOS_IDIOMAS 
            SET id_idioma = %s, tipo = %s
            WHERE id_video = %s AND id_idioma = %s
        """
        c.execute(query, (nuevo_id_idioma, tipo, id_video, id_idioma))
        conn.commit()

        print(f"✅ Vinculación actualizada: Video '{id_video}' → Idioma '{nuevo_id_idioma}' ({tipo})")

    except Exception as e:
        print(f"❌ Error al editar vinculación video-idioma: {e}")

    finally:
        conn.close()
def desvincularVideoIdioma(id_video, id_idioma):
    conn = obtener_conexion()
    c = conn.cursor()

    try:
        # Validar que la vinculación exista
        c.execute("""
            SELECT * 
            FROM VIDEOS_IDIOMAS 
            WHERE id_video = %s AND id_idioma = %s
        """, (id_video, id_idioma))

        if not c.fetchone():
            print("❌ No existe esta vinculación entre video e idioma")
            return

        # Eliminar
        query = """
            DELETE FROM VIDEOS_IDIOMAS 
            WHERE id_video = %s AND id_idioma = %s
        """
        c.execute(query, (id_video, id_idioma))
        conn.commit()

        print(f"✅ Vinculación de video con ISAN '{id_video}' e idioma ID '{id_idioma}' eliminada correctamente")

    except Exception as e:
        print(f"❌ Error al eliminar vinculación video-idioma: {e}")
    finally:
        conn.close()

def mostrarVinculosPorVideo(id_video):
    conn = obtener_conexion()
    c = conn.cursor()

    try:
        query = """
            SELECT i.id_idioma, i.nombre 
            FROM VIDEOS_IDIOMAS vi
            JOIN IDIOMAS i ON vi.id_idioma = i.id_idioma
            WHERE vi.id_video = %s
        """
        c.execute(query, (id_video,))
        idiomas_vinculados = c.fetchall()

        print(f"\n=== Idiomas vinculados al video con ISAN '{id_video}' ===")
        for idioma in idiomas_vinculados:
            print(f"ID: {idioma[0]}, Nombre: {idioma[1]}")

    except Exception as e:
        print(f"❌ Error al mostrar vínculos por video: {e}")
    finally:
        conn.close()