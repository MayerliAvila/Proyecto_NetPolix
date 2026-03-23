import sys
import os
from datetime import datetime

# Agregar la carpeta raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion_bd.conexionBD import obtener_conexion

# ==============================
# DAO de Usuarios
# ==============================


def findAllUsuarios():
    """
    Muestra todos los usuarios registrados.
    Incluye información de clientes (saldo, puntos, fecha_creacion) si aplica.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    query = """
        SELECT *FROM USUARIOS
    """
    c.execute(query)
    usuarios = c.fetchall()
    for usuario in usuarios:
        print(usuario)
    conn.close()


def crearUsuario(cedula, nombre, contraseña, rol_perfil):
    """
    Inserta un usuario en la tabla USUARIOS.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        query = "INSERT INTO USUARIOS (cedula, nombre, contraseña, rol_perfil) VALUES (%s, %s, %s, %s)"
        c.execute(query, (cedula, nombre, contraseña, rol_perfil))
        conn.commit()
        print(f"✅ Usuario {cedula} creado correctamente")
    except Exception as e:
        print("❌ Error al crear usuario:", e)
    finally:
        conn.close()


def editarUsuario(nombre, saldo, cedula, contraseña, rol_perfil):
    """
    Actualiza los datos de un usuario.
    Si el usuario es Cliente, también actualiza su saldo en DETALLES_CLIENTES.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        # Actualizar tabla USUARIOS
        query = "UPDATE USUARIOS SET nombre = %s, contraseña = %s, rol_perfil = %s WHERE cedula = %s"
        c.execute(query, (nombre, contraseña, rol_perfil, cedula))
        
        # Si es Cliente, actualizar saldo
        if rol_perfil == "Cliente" and saldo is not None:
            query_detalle = "UPDATE DETALLES_CLIENTES SET saldo = %s WHERE cedula_usuario = %s"
            c.execute(query_detalle, (saldo, cedula))
        
        conn.commit()
        print(f"✅ Usuario {cedula} actualizado correctamente")
    except Exception as e:
        print("❌ Error al actualizar usuario:", e)
    finally:
        conn.close()


def eliminarUsuario(cedula):
    """
    Elimina un usuario.
    Si es Cliente, también elimina sus detalles.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    try:
        # Eliminar detalles de cliente
        query_detalles = "DELETE FROM DETALLES_CLIENTES WHERE cedula_usuario = %s"
        c.execute(query_detalles, (cedula,))

        # Eliminar usuario
        query_usuario = "DELETE FROM USUARIOS WHERE cedula = %s"
        c.execute(query_usuario, (cedula,))
        
        conn.commit()
        print(f"✅ Usuario {cedula} eliminado correctamente")
    except Exception as e:
        print("❌ Error al eliminar usuario:", e)
    finally:
        conn.close()


def loginUsuario(cedula, contraseña):
    """
    Retorna el usuario si la cédula y contraseña coinciden, None si no existe.
    """
    conn = obtener_conexion()
    c = conn.cursor()
    query = "SELECT * FROM USUARIOS WHERE cedula = %s AND contraseña = %s"
    c.execute(query, (cedula, contraseña))
    usuario = c.fetchone()
    conn.close()
    return usuario

