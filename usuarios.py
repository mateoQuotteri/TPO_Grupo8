# Módulo
# usuarios.py


def ingresar_clave():
    """
    Pide ingreso de clave por teclado y verifica si cumple que sean 5 dígitos numéricos.
    """
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
    perfiles = ["ADMINISTRATIVO", "RECEPCIONISTA", "DOCTOR"]
    print("AGREGAR UN USUARIO")
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

    opcion = input("Ingrese una opción: ")
    opciones=["1","2","0"]
    while opcion not in opciones:
        print("Opción inválida.\n")
        opcion = input("Ingrese una opción: ")

    if opcion == "0":
        print("\nOperación cancelada.\n")

    elif opcion =="1" or opcion == "2":
        user = input("Ingrese el nombre del usuario o 0 para salir: ")   
        buscando=True
        while buscando:
            while user not in usuarios:
                print("\nUsuario no encontrado.\n")
                user = input("Ingrese el nombre del usuario o 0 para salir: ")
            buscando=False

        if opcion == "1": 
            print("\n---MODIFICAR CLAVE---\n")
            clave=ingresar_clave()
            usuarios[user]["clave"]=clave
            print("\nClave modificada de forma correcta.\n")

        elif opcion=="2":
            print("\n---MODIFICAR PERFIL---\n")
            perfil=seleccion_perfil()
            if perfil != 0:
                perfil = perfiles[perfil - 1]
                print("\nPerfil seleccionado: ", perfil)
                usuarios[user]["rol"]=perfil
    
    else: 
        print("Opción inválida.")

def eliminar_usuario(usuarios):
    print("ELIMINAR UN USUARIO")
    print()
    user = input("Ingrese el nombre del usuario a eliminar o 0 para salir: ")

    if user == "0":
        return
    elif user in usuarios:
        try:
            print("\nUsuario seleccionado: ", user)
            aux = int(input("\nSe va a eliminar el usuario seleccionado. Para confirmar ingrese 1. Para cancelar ingrese 0. "))
            while aux < 0 or aux > 1:
                print("\nOpción inválida. Vuelva a intentar.\n")
                aux = int(input("\nSe va a eliminar el usuario seleccionado. Para confirmar ingrese 1. Para cancelar ingrese 0. "))
            if aux == 0:
                return
            else:
                eliminado = usuarios.pop(user)
                print("\nSe eliminó el usuario: ", eliminado["nombre"])
                print()
        except ValueError:
            print ("\nDebe ingresar un número entero válido. Intente nuevamente.")
        except:
            print("\nError. Intente nuevamente.")
    else:
        print("\nUsuario no encontrado.")