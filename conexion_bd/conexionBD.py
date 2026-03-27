import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="o31fli.h.filess.io",
        database="Plataforma_NetPolix_twentythey",
        port=3307,
        user="Plataforma_NetPolix_twentythey",
        password="82432f03fff6540ac3fbb34b8bd09aadccaabfed"
    )

def probar_conexion():
    conexion = None
    try:
        conexion = obtener_conexion()
        if conexion.is_connected():
            print("✅ Conexión exitosa a la base de datos")
            print("Base de datos:", conexion.database)
    except Exception as e:
        print("❌ Error en conexión:", e)
    finally:
        if conexion and conexion.is_connected():
            conexion.close()