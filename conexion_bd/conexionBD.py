import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="pwwc1p.h.filess.io",
        database="NetPolix_elephantso",
        user="NetPolix_elephantso",
        password="ea97d83cb2228d0d2d4977161b9171e8fdc73b31",
        port=3307
    )
def probar_conexion():
    try:
        conexion = obtener_conexion()
        if conexion.is_connected():
            print("✅ Conexión exitosa a la base de datos")
            print("Base de datos:", conexion.database)
    except Exception as e:
        print("❌ Error en conexión:", e)
    finally:
        if conexion.is_connected():
            conexion.close()