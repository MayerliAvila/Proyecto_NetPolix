import sys
import os
from datetime import datetime

# Agregar la carpeta DAO al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DAO')))

import VideosDAO as v
import ClasificacionesDAO as c

def menu_videos():
    
    while True:
        print("\n====MENÚ VIDEOS ===")
        print("1. Mostrar Catalogo de videos")
        print("2. Crear video")
        print("3. Editar video")
        print("4. Eliminar video")
        print("5. Buscar por nombre el video")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print("\nListas de videos")
            print("ISAN | Titulo_original | año_produccion | duracion_min | tipo_clasificacion | serie")
            v.findAllVideos()
        elif opcion == "2":
            ISAN = input("Digite ISAN del video: ").strip()

            # Verificar si ya existe
            if v.buscarVideoPorISAN(ISAN):
                print("❌ Ya existe un video con ese ISAN")
                continue  

            titulo_original = input("Digite el titulo original del video: ").strip()
            anio_produccion = input("Digite el año de producción del video: ").strip()
            duracion_min = input("Digite la duración en minutos del video: ").strip()

            # Mostrar clasificaciones
            print("\nClasificaciones disponibles:")
            c.findAllClasificacion()

            tipo_clasificacion = input("Seleccione el tipo de clasificacion: ").strip()

            # Preguntar si es serie
            serie_opcion = input("¿Pertenece a una serie? (Si/No): ").strip().lower()

            if serie_opcion == "si":
                id_serie = input("Digite el ID de la serie: ").strip()
            else:
                id_serie = None  # Película
            v.crearVideo(ISAN, titulo_original, anio_produccion, duracion_min, tipo_clasificacion, id_serie)
        elif opcion == "3":
            ISAN = input("Digite el ISAN del video a editar: ").strip()
            titulo_originalU = input("Digite el titulo original de video: "). strip()
            anio_produccionU = input("Digite el año de producción del video: ").strip()
            duracion_minU = input("Digite la duración en minutos del video: ").strip()
            print("\n📋 Clasificaciones disponibles:")
            c.findAllClasificacion()
            tipo_clasificacionU = input("Seleccione el tipo de clasificacion: ").strip()
            serie_opcionU = input("¿Pertenece a una serie? (Si/No): ").strip().lower()
            if serie_opcionU == "si":
                id_serieU = input("Digite el ID de la serie: ").strip()
            else:                id_serieU = None  # Película
            v.editarVideo(ISAN, titulo_originalU, anio_produccionU, duracion_minU, tipo_clasificacionU, id_serieU)
        elif opcion == "4":
            ISAN = input("Digite el ISAN del video a eliminar: ").strip()
            v.eliminarVideo(ISAN)
        elif opcion == "5":
            nombre = input("Digite el nombre del video a buscar: ").strip()
            print("\n ISAN | Titulo_original | año_produccion | duracion_min | tipo_clasificacion | serie")
            v.buscarVideoPorNombre(nombre)
        elif opcion == "6":
            print("Saliendo del menú de videos...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
