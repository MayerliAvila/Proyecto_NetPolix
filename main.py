from scriptBD.crear_tablas import crear_tablas
from conexion_bd.conexionBD import probar_conexion
from modelos.conexion_usuarios import menu_usuarios
from modelos.conexion_clasificacion import menu_clasificaciones
from modelos.conexion_video import menu_videos

def menu():
    print("\n===== NETPOLIX =====")
    print("1. Probar conexión")
    print("2. Crear tablas")
    print("3. Menú Usuarios")
    print("4. Menú Clasificaciones")
    print("5. Menú Videos")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        probar_conexion()
    elif opcion == "2":
        crear_tablas()
    elif opcion == "3":
        menu_usuarios()
    elif opcion == "4":
        menu_clasificaciones()
    elif opcion == "5":
        menu_videos()
    elif opcion == "6":
        print("👋 Saliendo del sistema...")
        return False 
    else:
        print("❌ Opción inválida")

    return True 

# Programa principal
if __name__ == "__main__":
    continuar = True
    while continuar:
        continuar = menu()