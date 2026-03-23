import sys
import os
from datetime import datetime

# Agregar la carpeta DAO al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DAO')))

import ClasificacionesDAO as c

def menu_clasificaciones():
    while True:
        print("\n--- Menú de Clasificaciones ---")
        print("1. Mostrar clasificaciones")
        print("2. Crear clasificación")
        print("3. Editar clasificación")
        print("4. Eliminar clasificación")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\nLista de Clasificaciones:")
            print("\ntipo | descripcion")
            c.findAllClasificacion()
        elif opcion == "2":
            tipo = input("Digite el tipo de clasificacion: ").strip()
            descripcion = input("Digite la descripción de la clasificación: ").strip()
            c.crearClasificacion(tipo, descripcion)
        elif opcion == "3":
            tipoU = input("Digite el tipo de clasificación a actualizar: ").strip()
            descripcion = input("Digite la nueva descripción de la clasificación: ").strip()
            c.editarClasificacion(tipoU, descripcion)
        elif opcion == "4":
            tipo = input("Digite el tipo de clasificación a eliminar: ").strip()
            c.eliminarClasificacion(tipo)
        elif opcion == "5":
            print("Saliendo del menú de principal...")

            break
        else:
            print("Opción inválida. Intente nuevamente.")