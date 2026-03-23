from conexion_bd.conexionBD import obtener_conexion

def crear_tablas():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        tablas = [

            # SERIES
            """CREATE TABLE IF NOT EXISTS SERIES (
                id_serie INT PRIMARY KEY,
                titulo VARCHAR(255),
                sinopsis TEXT,
                temporada INT
            )""",

            # USUARIOS
            """CREATE TABLE IF NOT EXISTS USUARIOS (
                cedula VARCHAR(50) PRIMARY KEY,
                nombre VARCHAR(255),
                `contraseña` VARCHAR(100),
                rol_perfil VARCHAR(50)
            )""",

            # DETALLES_CLIENTES
            """CREATE TABLE IF NOT EXISTS DETALLES_CLIENTES (
                cedula_usuario VARCHAR(50) PRIMARY KEY,
                fecha_creacion DATETIME NOT NULL,
                saldo INT DEFAULT 0,
                puntos INT DEFAULT 0,
                FOREIGN KEY (cedula_usuario) REFERENCES USUARIOS(cedula) ON DELETE CASCADE
            )""",

            # CLASIFICACIONES
            """CREATE TABLE IF NOT EXISTS CLASIFICACIONES (
                tipo VARCHAR(50) PRIMARY KEY,
                descripcion TEXT
            )""",

            # VIDEOS
            """CREATE TABLE IF NOT EXISTS VIDEOS (
                isan VARCHAR(50) PRIMARY KEY,
                titulo_original VARCHAR(255),
                anio_produccion INT,
                duracion_min INT,
                id_clasificacion VARCHAR(50),
                id_serie INT,
                FOREIGN KEY (id_clasificacion) REFERENCES CLASIFICACIONES(tipo),
                FOREIGN KEY (id_serie) REFERENCES SERIES(id_serie)
            )""",

            # ORDENES
            """CREATE TABLE IF NOT EXISTS ORDENES (
                id_orden INT PRIMARY KEY,
                id_usuario VARCHAR(50),
                fecha_creacion DATETIME,
                estado VARCHAR(50),
                total DECIMAL(10,2),
                FOREIGN KEY (id_usuario) REFERENCES USUARIOS(cedula)
            )""",

            # ORDENES_DETALLES
            """CREATE TABLE IF NOT EXISTS ORDENES_DETALLES (
                id_detalle INT PRIMARY KEY,
                id_orden INT,
                id_video VARCHAR(50),
                tipo_transaccion VARCHAR(50),
                precio_unitario DECIMAL(10,2),
                FOREIGN KEY (id_orden) REFERENCES ORDENES(id_orden),
                FOREIGN KEY (id_video) REFERENCES VIDEOS(isan)
            )""",

            # CALIFICACIONES_USUARIOS
            """CREATE TABLE IF NOT EXISTS CALIFICACIONES_USUARIOS (
                id_calificacion INT PRIMARY KEY,
                id_usuario VARCHAR(50),
                id_detalle_orden INT,
                puntuacion INT,
                comentario TEXT,
                fecha_creacion DATETIME,
                FOREIGN KEY (id_usuario) REFERENCES USUARIOS(cedula),
                FOREIGN KEY (id_detalle_orden) REFERENCES ORDENES_DETALLES(id_detalle)
            )""",

            # PARTICIPANTES
            """CREATE TABLE IF NOT EXISTS PARTICIPANTES (
                id_participante INT PRIMARY KEY,
                nombre VARCHAR(255),
                fecha_nacimiento DATE
            )""",

            # ROLES
            """CREATE TABLE IF NOT EXISTS ROLES (
                id_rol INT PRIMARY KEY,
                nombre VARCHAR(255)
            )""",

            # VIDEOS_PARTICIPANTES
            """CREATE TABLE IF NOT EXISTS VIDEOS_PARTICIPANTES (
                id_video VARCHAR(50),
                id_participante INT,
                id_rol INT,
                FOREIGN KEY (id_video) REFERENCES VIDEOS(isan),
                FOREIGN KEY (id_participante) REFERENCES PARTICIPANTES(id_participante),
                FOREIGN KEY (id_rol) REFERENCES ROLES(id_rol)
            )""",

            # CATEGORIAS
            """CREATE TABLE IF NOT EXISTS CATEGORIAS (
                id_categoria VARCHAR(10) PRIMARY KEY,
                nombre VARCHAR(255)
            )""",

            # VIDEOS_CATEGORIAS
            """CREATE TABLE IF NOT EXISTS VIDEOS_CATEGORIAS (
                id_video VARCHAR(50),
                id_categoria VARCHAR(10),
                FOREIGN KEY (id_video) REFERENCES VIDEOS(isan),
                FOREIGN KEY (id_categoria) REFERENCES CATEGORIAS(id_categoria)
            )""",

            # IDIOMAS
            """CREATE TABLE IF NOT EXISTS IDIOMAS (
                id_idioma INT PRIMARY KEY,
                nombre VARCHAR(255)
            )""",

            # VIDEOS_IDIOMAS
            """CREATE TABLE IF NOT EXISTS VIDEOS_IDIOMAS (
                id_video VARCHAR(50),
                id_idioma INT,
                tipo VARCHAR(50),
                FOREIGN KEY (id_video) REFERENCES VIDEOS(isan),
                FOREIGN KEY (id_idioma) REFERENCES IDIOMAS(id_idioma)
            )""",

            # COLECCIONES
            """CREATE TABLE IF NOT EXISTS COLECCIONES (
                isan VARCHAR(50) PRIMARY KEY,
                titulo VARCHAR(255),
                volumen INT
            )""",

            # COLECCIONES_VIDEOS
            """CREATE TABLE IF NOT EXISTS COLECCIONES_VIDEOS (
                id_coleccion VARCHAR(50),
                id_video VARCHAR(50),
                FOREIGN KEY (id_coleccion) REFERENCES COLECCIONES(isan),
                FOREIGN KEY (id_video) REFERENCES VIDEOS(isan)
            )"""
        ]

        # Ejecutar todas las tablas en orden
        for tabla in tablas:
            cursor.execute(tabla)

        conexion.commit()
        print("✅ Todas las tablas fueron creadas correctamente")

    except Exception as e:
        print("❌ Error al crear tablas:", e)

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()


if __name__ == "__main__":
    crear_tablas()