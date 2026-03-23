import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion_bd.conexionBD import obtener_conexion

# ==============================
# DAO de Detalles de Clientes
# ==============================

def findAllClientesDetalles():
    """
    Obtiene todos los detalles de clientes (saldo, puntos, fecha_creacion)
    junto con la información básica del usuario.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    query = """
        SELECT u.cedula, u.nombre, dc.saldo, dc.puntos, dc.fecha_creacion
        FROM DETALLES_CLIENTES dc
        JOIN USUARIOS u ON dc.cedula_usuario = u.cedula
    """
    c.execute(query)
    clientes = c.fetchall()
    for cliente in clientes:
        print(cliente)
    conn.close()


def crearClienteDetalle(cedula_usuario, puntos=0, saldo=0, fecha_creacion=None):
    """
    Inserta un registro en DETALLES_CLIENTES para un usuario cliente.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    fecha_creacion = fecha_creacion or datetime.now()
    try:
        query = """
            INSERT INTO DETALLES_CLIENTES (cedula_usuario, puntos, saldo, fecha_creacion)
            VALUES (%s, %s, %s, %s)
        """
        c.execute(query, (cedula_usuario, puntos, saldo, fecha_creacion))
        conn.commit()
        print(f"✅ Detalles del cliente {cedula_usuario} creados correctamente")
    except Exception as e:
        print("❌ Error al crear detalles del cliente:", e)
    finally:
        conn.close()


def actualizarPuntos(cedula_usuario, puntos):
    """
    Suma puntos al cliente.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "UPDATE DETALLES_CLIENTES SET puntos = puntos + %s WHERE cedula_usuario = %s"
        c.execute(query, (puntos, cedula_usuario))
        conn.commit()
        print(f"✅ Puntos actualizados para {cedula_usuario}.")
    except Exception as e:
        print("❌ Error al actualizar puntos:", e)
    finally:
        conn.close()


def actualizarSaldo(cedula_usuario, saldo):
    """
    Actualiza el saldo del cliente.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "UPDATE DETALLES_CLIENTES SET saldo = %s WHERE cedula_usuario = %s"
        c.execute(query, (saldo, cedula_usuario))
        conn.commit()
        print(f"✅ Saldo actualizado para {cedula_usuario}.")
    except Exception as e:
        print("❌ Error al actualizar saldo:", e)
    finally:
        conn.close()


def eliminarClienteDetalle(cedula_usuario):
    """
    Elimina los detalles de un cliente.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "DELETE FROM DETALLES_CLIENTES WHERE cedula_usuario = %s"
        c.execute(query, (cedula_usuario,))
        conn.commit()
        print(f"✅ Detalles del cliente {cedula_usuario} eliminados correctamente")
    except Exception as e:
        print("❌ Error al eliminar detalles del cliente:", e)
    finally:
        conn.close()


def obtenerPuntos(cedula_usuario):
    """
    Retorna los puntos de un cliente, o None si no existe.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    query = "SELECT puntos FROM DETALLES_CLIENTES WHERE cedula_usuario = %s"
    c.execute(query, (cedula_usuario,))
    resultado = c.fetchone()
    conn.close()
    return resultado[0] if resultado else None


def obtenerSaldo(cedula_usuario):
    """
    Retorna el saldo de un cliente, o None si no existe.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    query = "SELECT saldo FROM DETALLES_CLIENTES WHERE cedula_usuario = %s"
    c.execute(query, (cedula_usuario,))
    resultado = c.fetchone()
    conn.close()
    return resultado[0] if resultado else None