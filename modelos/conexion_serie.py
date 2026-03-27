import sys
import os
from datetime import datetime

# Agregar la carpeta DAO al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DAO')))

import SeriesDAO as s

def menu_series():
    """
    Menú interactivo para gestionar series.
    """
    while True:
        print("\n===== MENÚ SERIES =====")
        print("1. Mostrar series")
        print("2. Crear serie")
        print("3. Editar serie")
        print("4. Eliminar serie")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        # ------------------- MOSTRAR SERIES -------------------
        if opcion == "1":
            print("\n Lista de Series:")
            s.findAllSeries()

        # ------------------- CREAR SERIE -------------------
        elif opcion == "2":
            id_serie = input("Digite el ID de la serie: ").strip()
            titulo = input("Digite el título de la serie: ").strip()
            sinopsis = input("Digite la sinopsis de la serie: ").strip()
            temporadas = input("Digite el número de temporadas: ").strip()
            s.crearSerie(id_serie, titulo, sinopsis, int(temporadas))

        # ------------------- EDITAR SERIE -------------------
        elif opcion == "3":
            id_serie = input("Digite el ID de la serie a editar: ").strip()
            titulo = input("Digite el nuevo título de la serie: ").strip()
            sinopsis = input("Digite el nuevo sinopsis de la serie: ").strip()
            temporadas = input("Digite el nuevo número de temporadas: ").strip()
            s.editarSerie(id_serie, titulo, sinopsis, int(temporadas))
        elif opcion == "4":
            id_serie = input("Digite el ID de la serie a eliminar: ").strip()
            s.eliminarSerie(id_serie)

        # Volver al menú principal
        elif opcion == "5":
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")