import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion_bd.conexionBD import obtener_conexion

def findAllCategorias():
    conn = obtener_conexion()
    c = conn.cursor()
    query = """SELECT * FROM CATEGORIAS"""
    c.execute(query)
    categorias = c.fetchall()
    for categoria in categorias:
        print(categoria)
    conn.close()

def crearCategoria(id_categoria, nombre):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = """
            INSERT INTO CATEGORIAS (id_categoria, nombre)
            VALUES (%s, %s)
        """
        c.execute(query, (id_categoria, nombre))
        conn.commit()
        print(f"✅ Categoría '{nombre}' creada correctamente")
    except Exception as e:
        print("❌ Error al crear categoría:", e)
    finally:
        conn.close()
def editarCategoria(id_categoria, nombre):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = """
            UPDATE CATEGORIAS
            SET nombre = %s
            WHERE id_categoria = %s
        """
        c.execute(query, (nombre, id_categoria))
        conn.commit()
        print(f"✅ Categoría '{nombre}' actualizada correctamente")
    except Exception as e:
        print("❌ Error al actualizar categoría:", e)
    finally:
        conn.close()
def eliminarCategoria(id_categoria):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "DELETE FROM CATEGORIAS WHERE id_categoria = %s"
        c.execute(query, (id_categoria,))
        conn.commit()
        print(f"✅ Categoría con ID '{id_categoria}' eliminada correctamente")
    except Exception as e:
        print("❌ Error al eliminar categoría:", e)
    finally:
        conn.close()
    
def mostrarSoloID_Categoria():
    conn = obtener_conexion()
    c = conn.cursor()
    query = "SELECT id_categoria, nombre FROM CATEGORIAS"
    c.execute(query)
    categorias = c.fetchall()
    for categoria in categorias:
        print(categoria)
    conn.close()