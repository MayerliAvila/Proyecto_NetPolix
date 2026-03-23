import sys
import os
from datetime import datetime

# Agregar la carpeta DAO al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DAO')))

import VideosDAO as v
import Videos_categoriasDAO as vc
import CategoriasDAO as c

def menu_categorias():
    while True:
        print("\n====MENÚ CATEGORIAS ===")
        print("1. Mostrar categorias")
        print("2. Crear categoria")
        print("3. Editar categoria")
        print("4. Eliminar categoria")
        print("5. Videos por categorias")
        print("6. Vincular video por categoria")
        print("7. Editar la vinculacion por categoria")
        print("8. Desvincular el video a la categoria")
        print("9. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\nLista de categorias")
            print("id_categoria | Nombre")
            c.findAllCategorias()
        elif opcion == "2":
            id_categoria = input("Digite el ID de la categoria: ").strip()
            nombre = input("Digite el nombre de la categoria: ").strip()
            c.crearCategoria(id_categoria, nombre)
        elif opcion == "3":
            id_categoriaU = input("Digite el ID de la categoria a editar: ").strip()
            nombreU = input("Digite el nuevo nombre de la categoria: ").strip()
            c.editarCategoria(id_categoriaU, nombreU)
        elif opcion == "4":
            id_categoria = input("Digite el ID de la categoria a eliminar: ").strip()
            c.eliminarCategoria(id_categoria)
        elif opcion == "5":
            print("\nVideos por categorias")
            print("id_categoria | Nombre")
            c.findAllCategorias()
            id_categoria = input("Digite el ID de la categoria para mostrar los videos: ").strip()
            vc.obtenerVideosPorCategoria(id_categoria)
        elif opcion == "6":
            print("\nISAN creados")
            v.mostrarSoloISAN()
            id_video = input("Digite el ISAN del video a vincular: ").strip()
            print("\nCategorias disponibles")
            c.mostrarSoloID_Categoria()
            id_categoria = input("Digite el ID de la categoria para vincular el video: ").strip()
            vc.vincularVideoCategoria(id_video, id_categoria)
        elif opcion == "7":
            print("\nISAN creados")
            v.mostrarSoloISAN()
            id_video = input("Digite el ISAN del video a editar la vinculacion: ").strip()
            print("\nCategorias viculadas")
            v.mostrarViculacionCategoriasPorVideo(id_video)
            id_categoria = input("Digite el ID de la categoria actual para editar la vinculacion: ").strip()
            print("\nCategorias disponibles")
            c.mostrarSoloID_Categoria()
            id_categoria_nueva = input("Digite el nuevo ID de la categoria para actualizar la vinculacion: ").strip()
            vc.editarVinculacionVideoCategoria(id_video, id_categoria, id_categoria_nueva)
        elif opcion == "8":
            print("\nISAN creados")
            v.mostrarSoloISAN()
            id_video = input("Digite el ISAN del video a desvincular: ").strip()
            print("\nCategorias viculadas")
            v.mostrarViculacionCategoriasPorVideo(id_video)
            id_categoria = input("Digite el ID de la categoria para desvincular el video: ").strip()
            vc.desvincularVideoCategoria(id_video, id_categoria)
        elif opcion == "9":
            print("Saliendo del menú de categorias...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")
