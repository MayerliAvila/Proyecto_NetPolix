import sys
import os
from datetime import datetime

# Agregar la carpeta raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion_bd.conexionBD import obtener_conexion


# DAO de Usuarios

def findAllClasificacion():
   conn = obtener_conexion()
   c = conn.cursor()
   query= """SELECT * FROM CLASIFICACIONES"""
   c.execute(query)
   clasificaciones = c.fetchall()
   for clasificacion in clasificaciones:
      print(clasificacion)
   conn.close()

def crearClasificacion(tipo, descripcion):
   conn = obtener_conexion()
   c = conn.cursor()
   try:
      query ="INSERT INTO CLASIFICACIONES (tipo, descripcion) VALUES (%s, %s)"
      c.execute(query, (tipo, descripcion))
      conn.commit()
      print(f"✅ Clasificación '{tipo}' creada correctamente")
   except Exception as e:
        print("❌ Error al crear clasificación:", e)
   finally:
        conn.close()
def editarClasificacion(tipo, descripcion):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "UPDATE CLASIFICACIONES SET descripcion = %s WHERE tipo = %s"
        c.execute(query, (descripcion, tipo))
        conn.commit()
        print(f"✅ Clasificación '{tipo}' actualizada correctamente")
    except Exception as e:
        print("❌ Error al actualizar clasificación:", e)
    finally:       
        conn.close()
def eliminarClasificacion(tipo):
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "DELETE FROM CLASIFICACIONES WHERE tipo = %s"
        c.execute(query, (tipo,))
        conn.commit()
        print(f"✅ Clasificación '{tipo}' eliminada correctamente")
    except Exception as e:
        print("❌ Error al eliminar clasificación:", e)
    finally:
        conn.close()