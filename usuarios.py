# Módulo
# usuarios.py

def pedir_entero(mensaje):
    """
    Solicita el ingreso de un número entero y maneja el error si el usuario ingresa un valor no válido.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero entero válido. Use -1 para cancelar.")

def ingresar_clave():
    """
    Pide ingreso de clave por teclado y verifica si cumple que sean 5 dígitos numéricos.
    """
    while True:
        try:        
            clave=int(input("Ingrese la nueva clave numérica (5 dígitos): "))
            if clave>10000 and clave<99999:
                return str(clave)
            else:
                print("Debe ingresar una clave de 5 dígitos númericos.")
                clave=int(input("Ingrese la nueva clave numérica (5 dígitos): "))
        except ValueError:
            print ("Debe ingresar un número entero válido. Intente nuevamente.")
        except:
            print("Error. Intente nuevamente.")

def seleccion_perfil():
    """
    Pide por pantalla que se seleccione un perfil de usuario entre las opciones disponibles.
    """
    try:
        perfiles = ["ADMINISTRATIVO", "RECEPCIONISTA", "DOCTOR"]
        for i in range(len(perfiles)):
            print([i + 1], perfiles[i])
        print()
        aux = int(input("\nSeleccione el perfil del usuario. Ingrese 0 para salir. "))
        while aux < 0 or aux > len(perfiles):
            print("\nOpción inválida. Vuelva a intentar.")
            aux = int(input("\nSeleccione el perfil del usuario. Ingrese 0 para salir. "))
        return aux
    except ValueError:
        print ("\nDebe ingresar un número entero válido. Intente nuevamente.")
    except:
        print("\nError. Intente nuevamente.")        

def agregar_usuario(usuarios):
    """
    Permite el ingreso de un usuario nuevo. 
    """
    perfiles = ["ADMINISTRATIVO", "RECEPCIONISTA", "DOCTOR"]
    print("---AGREGAR UN USUARIO---")
    print()

    seleccion=seleccion_perfil()
    if seleccion != 0:
        perfil = perfiles[seleccion - 1]
        print("\nPerfil seleccionado: ", perfil)
        user = input("\nIngrese el nombre de usuario: ")
        while user in usuarios:
            print("\nUsuario ya existe.")
            user = input("\nIngrese el nombre de usuario: ")

        clave=ingresar_clave()
        nombre = input("\nIngrese nombre y apellido: ")

        usuarios[user] = {"clave": clave, "nombre": nombre, "rol": perfil}
        print("\nUsuario agregado de forma correcta.\n")
        print()

def modificar_usuario(usuarios):
    """
    Permite ingresar un usuario por pantalla y modificar su clave y perfil.
    """
    perfiles = ["ADMINISTRATIVO", "RECEPCIONISTA", "DOCTOR"]

    print("\nSeleccione el dato que desea modificar:")
    print("[1] Modificar clave.")
    print("[2] Modificar perfil.")
    print("[0] Volver al menú anterior")
    print("[-1] Cancelar")

    opcion = input("Ingrese una opción: ")
    opciones=["1","2","0","-1"]
    while opcion not in opciones:
        print("Opción inválida.\n")
        opcion = input("Ingrese una opción: ")

    if opcion == "0" or opcion == "-1":
        print("\nOperación cancelada.\n")
        return

    user = input("Ingrese el nombre del usuario o -1 para cancelar: ")
    while user not in usuarios:
        if user == "-1":
            print("\nOperacion cancelada.\n")
            return
        print("\nUsuario no encontrado.\n")
        user = input("Ingrese el nombre del usuario o -1 para cancelar: ")

    if opcion == "1":
        print("\n---MODIFICAR CLAVE---\n")
        clave = ingresar_clave()
        if clave is None:
            print("\nOperacion cancelada.\n")
            return
        usuarios[user]["clave"] = clave
        print("\nClave modificada de forma correcta.\n")

    elif opcion == "2":
        print("\n---MODIFICAR PERFIL---\n")
        perfil = seleccion_perfil()
        if perfil is None:
            print("\nOperacion cancelada.\n")
            return
        print("\nPerfil seleccionado: ", perfil)
        usuarios[user]["rol"] = perfil

def eliminar_usuario(usuarios):
    print("ELIMINAR UN USUARIO")
    print()
    user = input("Ingrese el nombre del usuario a eliminar o -1 para cancelar: ").strip().lower()

    if user == "-1":
        return
    elif user in usuarios:
        if usuarios[user]["rol"] == "ADMINISTRATIVO":
            cant_admins = sum(1 for u in usuarios.values() if u["rol"] == "ADMINISTRATIVO")
            if cant_admins <= 1:
                print("\nError denegado: No se puede eliminar al único ADMINISTRATIVO del sistema.")
                return

        try:
            print("\nUsuario seleccionado: ", user)
            aux = pedir_entero("\nSe va a eliminar el usuario seleccionado. Para confirmar ingrese 1. Para cancelar ingrese 0 o -1: ")
            while aux not in [1, 0, -1]:
                print("\nOpcion invalida. Vuelva a intentar.\n")
                aux = pedir_entero("\nPara confirmar ingrese 1. Para cancelar ingrese 0 o -1: ")
            if aux == 0 or aux == -1:
                print("\nOperación cancelada.\n")
                return
            eliminado = usuarios.pop(user)
            print("\nSe elimino el usuario: ", eliminado["nombre"])
            print()
        except ValueError:
            print("\nDebe ingresar un número entero válido. Intente nuevamente.")
        except:
            print("\nError. Intente nuevamente.")
    else:
        print("\nUsuario no encontrado.")

def registrar_login(usuario, rol):
    """
    Registra el historial de inicios de sesión en un archivo de texto independiente,
    guardando el usuario, su rol y la fecha/hora exacta del evento.
    """
    import os
    from datetime import datetime
    
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_auditoria = os.path.join(base_dir, "historial_logins.txt")
        
        fecha_hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        with open(ruta_auditoria, "a", encoding="utf-8") as f:
            f.write(f"[{fecha_hora_actual}] Usuario: {usuario:<12} | Rol: {rol:<15} | Estado: INICIO DE SESIÓN EXITOSO\n")
            
    except OSError:
        print("ERROR DE SISTEMA: No se pudo registrar el evento en el historial de logins.")