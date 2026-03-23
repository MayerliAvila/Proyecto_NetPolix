from conexion_bd.conexionBD import obtener_conexion

def crear_tablas():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        tablas = [

            # Tabla de usuarios general (para todos los roles)
            """CREATE TABLE IF NOT EXISTS USUARIOS (
                cedula VARCHAR(50) PRIMARY KEY,
                nombre VARCHAR(255),
                contraseña VARCHAR(100),
                rol_perfil VARCHAR(50)  -- Cliente, Admin, Gerente
            )""",

            # Tabla de detalles para clientes únicamente
            """CREATE TABLE IF NOT EXISTS DETALLES_CLIENTES (
                cedula_usuario VARCHAR(50) PRIMARY KEY,
                puntos INT DEFAULT 0,
                saldo INT DEFAULT 0,
                fecha_creacion DATETIME,
                FOREIGN KEY (cedula_usuario) REFERENCES USUARIOS(cedula) ON DELETE CASCADE
            )"""
        ]

        for tabla in tablas:
            cursor.execute(tabla)

        conexion.commit()
        print("✅ Tablas creadas correctamente")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()


if __name__ == "__main__":
    crear_tablas()