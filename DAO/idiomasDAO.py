import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion_bd.conexionBD import obtener_conexion

def findAllIdioma():
    conn = obtener_conexion()
    c = conn.cursor()
    query = """SELECT * FROM IDIOMAS"""
    c.execute(query)
    idiomas = c.fetchall()
    for idioma in idiomas:
        print(idioma)
    conn.close()

def crearIdioma(id_idioma, nombre):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = """
            INSERT INTO IDIOMAS (id_idioma, nombre)
            VALUES (%s, %s)
        """
        c.execute(query, (id_idioma, nombre))
        conn.commit()
        print(f"✅ Idioma '{nombre}' creado correctamente")
    except Exception as e:
        print("❌ Error al crear idioma:", e)
    finally:
        conn.close()

def editarIdioma(id_idioma, nombre):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = """
            UPDATE IDIOMAS
            SET nombre = %s
            WHERE id_idioma = %s
        """
        c.execute(query, (nombre, id_idioma))
        conn.commit()
        print(f"✅ Idioma '{nombre}' actualizado correctamente")
    except Exception as e:
        print("❌ Error al actualizar idioma:", e)
    finally:
        conn.close()
def eliminarIdioma(id_idioma):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "DELETE FROM IDIOMAS WHERE id_idioma = %s"
        c.execute(query, (id_idioma,))
        conn.commit()
        print(f"✅ Idioma con ID '{id_idioma}' eliminado correctamente")
    except Exception as e:
        print("❌ Error al eliminar idioma:", e)
    finally:
        conn.close()

