from scriptBD.crear_tablas import crear_tablas
from conexion_bd.conexionBD import probar_conexion
from modelos.conexion_usuarios import menu_usuarios
from modelos.conexion_clasificacion import menu_clasificaciones
from modelos.conexion_video import menu_videos
from modelos.conexion_categoria import menu_categorias


# 🔹 SUBMENÚ BASE DE DATOS
def menu_bd():
    while True:
        print("\n=== 🛠️ BASE DE DATOS ===")
        print("1. Probar conexión")
        print("2. Crear tablas")
        print("3. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            probar_conexion()
        elif opcion == "2":
            crear_tablas()
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida")


# 🔹 SUBMENÚ CATÁLOGO
def menu_catalogo():
    while True:
        print("\n=== 🎬 CATÁLOGO DE CONTENIDO ===")
        print("1. Clasificaciones")
        print("2. Videos")
        print("3. Categorías")
        print("4. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_clasificaciones()
        elif opcion == "2":
            menu_videos()
        elif opcion == "3":
            menu_categorias()
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida")


# 🔹 MENÚ PRINCIPAL
def menu():
    while True:
        print("\n==============================")
        print("🎥        NETPOLIX        🎥")
        print("==============================")
        print("1. Sistema BD")
        print("2. Módulo Cliente")
        print("3. Módulo Interacciones")
        print("4. Catálogo de Contenido")
        print("5. Ventas / Carrito")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_bd()

        elif opcion == "2":
            menu_usuarios()

        elif opcion == "3":
            print("⚠️ Módulo Interacciones en construcción...")

        elif opcion == "4":
            menu_catalogo()

        elif opcion == "5":
            menu_videos()  # puedes cambiar luego

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida")


# 🚀 PROGRAMA PRINCIPAL
if __name__ == "__main__":
    menu()