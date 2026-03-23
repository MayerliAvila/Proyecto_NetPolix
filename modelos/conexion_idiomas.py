import sys
import os
from datetime import datetime

# Agregar la carpeta DAO al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DAO')))

import idiomasDAO as i
import VideosDAO as v
import Videos_idiomasDAO as vi

def menu_idiomas():
    while True:
        print("\n====MENÚ IDIOMAS ===")
        print("1. Mostrar idiomas")
        print("2. Crear idioma")
        print("3. Editar idioma")
        print("4. Eliminar idioma")
        print("5. Videos por idioma")
        print("6. Vincular video por idioma")
        print("7. Editar la vinculacion por idioma")
        print("8. Desvincular el idioma a video")
        print("9. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\nLista de idiomas")
            print("id_idioma | Nombre")
            i.findAllIdioma()
        elif opcion == "2":
            id_idioma = input("Digite el ID del idioma: ").strip()
            nombre = input("Digite el nombre del idioma: ").strip()
            i.crearIdioma(id_idioma, nombre)
        elif opcion == "3":
            id_idiomaU = input("Digite el ID del idioma a editar: ").strip()
            nombreU = input("Digite el nuevo nombre del idioma: ").strip()
            i.editarIdioma(id_idiomaU, nombreU)
        elif opcion == "4":
            id_idioma = input("Digite el ID del idioma a eliminar: ").strip()
            i.eliminarIdioma(id_idioma)
        elif opcion == "5":
            vi.findAllVideos_idioma()
        elif opcion == "6":
            print("\nISAN creados")
            v.mostrarSoloISAN()
            id_video = input("Digite el ISAN del video a vincular: ").strip()

            print("\nIdiomas disponibles")
            i.mostrarSoloID_Idioma()
            id_idioma = input("Digite el ID del idioma: ").strip()

            print("\nTipos disponibles:")
            print("1. Original")
            print("2. Subtitulos")
            print("3. Doblaje")

            tipo_op = input("Seleccione el tipo: ").strip()

            if tipo_op == "1":
                tipo = "original"
            elif tipo_op == "2":
                tipo = "subtitulos"
            elif tipo_op == "3":
                tipo = "doblaje"
            else:
                print("❌ Tipo inválido")
                continue

            vi.vincularVideoIdioma(id_video, id_idioma, tipo)
        elif opcion == "7":
            print("\nISAN creados")
            v.mostrarSoloISAN()
            id_video = input("Digite el ISAN del video: ").strip()

            print("\nIdiomas vinculados")
            vi.mostrarVinculosPorVideo(id_video)

            id_idioma = input("Digite el ID del idioma actual: ").strip()

            print("\nNuevo idioma")
            i.mostrarSoloID_Idioma()
            nuevo_id_idioma = input("Digite el nuevo ID del idioma: ").strip()

            print("\nTipos disponibles:")
            print("1. Original")
            print("2. Subtitulos")
            print("3. Doblaje")

            tipo_op = input("Seleccione el tipo: ").strip()

            if tipo_op == "1":
                tipo = "original"
            elif tipo_op == "2":
                tipo = "subtitulos"
            elif tipo_op == "3":
                tipo = "doblaje"
            else:
                print("❌ Tipo inválido")
                continue

            vi.editarVinculoVideoIdioma(id_video, id_idioma, nuevo_id_idioma, tipo)
        elif opcion == "8":
            print("\nISAN creados")
            v.mostrarSoloISAN()
            id_video = input("Digite el ISAN del video a desvincular: ").strip()
            print("\nIdiomas viculados")
            vi.mostrarVinculosPorVideo(id_video)
            id_idioma = input("Digite el ID del idioma para desvincular el video:  ").strip()
            vi.desvincularVideoIdioma(id_video, id_idioma)
        elif opcion == "9":
            break
        else:
            print("❌ Opción inválida") 