import sys
import os
from datetime import datetime

# Agregar la carpeta DAO al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DAO')))

import UsuariosDAO as u
import Detalles_clientesDAO as d

def menu_usuarios():
    """
    Menú interactivo para gestionar usuarios y detalles de clientes.
    """
    while True:
        print("\n===== MENÚ USUARIOS =====")
        print("1. Mostrar usuarios")
        print("2. Crear usuario")
        print("3. Editar usuario")
        print("4. Eliminar usuario")
        print("5. Iniciar sesión")
        print("6.  Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        # ------------------- MOSTRAR USUARIOS -------------------
        if opcion == "1":
            print("\nLista de Usuarios:")
            print("\ncedula | nombre | contraseña | rol_perfil")
            u.findAllUsuarios()
            print("\nDetalles de Clientes:")
            print("\ncedula | nombre | saldo | puntos | fecha_creacion")
            d.findAllClientesDetalles()

        # ------------------- CREAR USUARIO -------------------
        elif opcion == "2":
            cedula = input("Digite la cédula: ").strip()
            nombre = input("Digite el nombre: ").strip()
            contraseña = input("Digite la contraseña: ").strip()

            # Elegir rol_perfil primero
            print("Seleccione el rol del usuario: (1) Cliente, (2) Admin, (3) Gerente")
            rol_opcion = input("Opción: ").strip()
            rol_perfil = "Cliente"  # valor por defecto

            if rol_opcion == "1":
                rol_perfil = "Cliente"
            elif rol_opcion == "2":
                rol_perfil = "Admin"
            elif rol_opcion == "3":
                rol_perfil = "Gerente"
            # Crear usuario en la tabla USUARIOS
            u.crearUsuario(cedula, nombre, contraseña, rol_perfil)
            
            # Si es Cliente, crear detalles
            if rol_perfil == "Cliente":
                saldo = input("Digite el saldo inicial (o deje en blanco para 0): ").strip() or 0
                puntos = 0
                d.crearClienteDetalle(cedula, puntos, int(saldo), datetime.now())

                # Opción de referir a alguien
                print("\n¿Deseas referir a alguien? (si/no)")
                referir = input().strip().lower()
                if referir == "si":
                    invitado_cedula = input("Digite la cédula del invitado: ").strip()
                    invitado_puntos = d.obtenerPuntos(invitado_cedula)
                    if invitado_puntos is not None:
                        d.actualizarPuntos(invitado_cedula, 1)
                        print(f"¡{invitado_cedula} ganó 1 punto por la referencia!")
                    else:
                        print("El invitado no está registrado en el sistema. No se asignaron puntos.")
            

            print("Usuario creado exitosamente.")

        # ------------------- EDITAR USUARIO -------------------
        elif opcion == "3":
            cedulaU = input("Digite la cédula del usuario a actualizar: ").strip()
            nombreU = input("Digite el nuevo nombre: ").strip()
            contraseñaU = input("Digite la nueva contraseña: ").strip()

            # Elegir rol_perfil
            print("Seleccione el nuevo rol del usuario: (1) Cliente, (2) Admin, (3) Gerente")
            rol_opcion = input("Opción: ").strip()
            rol_perfil = None
            if rol_opcion == "1":
                rol_perfil = "Cliente"
            elif rol_opcion == "2":
                rol_perfil = "Admin"
            elif rol_opcion == "3":
                rol_perfil = "Gerente"

            # Actualizar usuario en tabla USUARIOS
            u.editarUsuario(nombreU, 0, cedulaU, contraseñaU, rol_perfil)
            
            # Si es Cliente, actualizar saldo
            if rol_perfil == "Cliente":
                saldoU = input("Digite el nuevo saldo (o deje en blanco para no cambiar): ").strip()
                if saldoU:
                    d.actualizarSaldo(cedulaU, int(saldoU))

            


            print("Usuario actualizado exitosamente.")

        # ------------------- ELIMINAR USUARIO -------------------
        elif opcion == "4":
            cedulaE = input("Digite la cédula del usuario a eliminar: ").strip()
            
            # Si existe en detalles de cliente, eliminar primero
            if d.obtenerPuntos(cedulaE) is not None:
                d.eliminarClienteDetalle(cedulaE)
            
            u.eliminarUsuario(cedulaE)
            print("Usuario eliminado exitosamente.")

        # ------------------- INICIO DE SESIÓN -------------------
        elif opcion == "5":
            cedula_login = input("Digite su cédula: ").strip()
            contraseña_login = input("Digite su contraseña: ").strip()

            usuario = u.loginUsuario(cedula_login, contraseña_login)
            if usuario:
                rol = usuario[3]  # rol_perfil
                print(f"\n¡Bienvenido {usuario[1]}!")
                if rol == "Cliente":
                    saldo = d.obtenerSaldo(cedula_login)
                    puntos = d.obtenerPuntos(cedula_login)
                    print(f"Saldo: {saldo}, Puntos: {puntos}, Rol: {rol}")
                else:
                    print(f"Rol: {rol}")
            else:
                print("Cédula o contraseña incorrecta. Intente de nuevo.")

        # ------------------- SALIR -------------------
        elif opcion == "6":
            print("Saliendo del menú de principal...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")