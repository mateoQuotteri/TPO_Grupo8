#Módulo
#pacientes.py

import re

def pedir_entero(mensaje):
    '''
    Solicita el ingreso de un número entero por pantalla. 
    Evita errores si el usuario ingresa una letra o símbolo.
    '''
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero entero valido. Use -1 para cancelar.")


def validar_nombre(nombre):
    """
    Valida que el nombre solo contenga letras y espacios NO permite números ni caracteres especiales
    """
    return bool(re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$', nombre)) and nombre.strip() != ""


def validar_apellido(apellido):
    """
    Valida que el apellido solo permita letras y espacios
    """
    return bool(re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$', apellido)) and apellido.strip() != ""

def validar_dni(dni):
    """
    El DNI debe tener exactamente 8 dígitos y no contenga letras
    """
    return bool(re.match(r'^\d{8}$', dni))

def validar_telefono(telefono):
    """
    Telefono tenga exactamente 10 dígitos y no contenga letras
    """
    return bool(re.match(r'^\d{10}$', telefono))

def validar_correo(correo):
    """
    Valida que el correo tenga formato válido La validacion : usuario@dominio.ext
    """
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', correo))

def buscar_dni(lista_pacientes):
    """
    Pide el ingreso de un DNI por teclado y verifica si existe en la lista de pacientes.
    Brinda la opción para salir con 0.
    """
    try:
        dnis=[d["dni"] for d in lista_pacientes]
        dni = int(input("Ingrese el DNI o 0 para salir: "))
        while str(dni) not in dnis and dni!=0:
            print("No se ha encontrado un paciente asociado al DNI indicado. Vuelva a intentar.")
            dni = int(input("Ingrese el DNI o 0 para salir: "))
        return str(dni)
    except ValueError:
        print("Debe ingresar un número entero. Vuelva a intentar.")
    except:
        print("Error. Vuelva a intentar.")

def agregar_paciente(lista, contador):
    """
    # Solicita datos, valida el formato y añade un nuevo paciente a la lista
    """
    print("\n---AGREGAR PACIENTE---\n")
    dnis=[d["dni"] for d in lista]
    
    try:
        dni = input("Ingrese el DNI o 0 para salir: ")
        if dni !="0":
            
            while not validar_dni(dni):
                print("Dato incorrecto")
                dni = input("DNI: ")
            
            if dni in dnis:
                print("\nEl DNI ya se encuentra asociado a un paciente.\n")
                return contador

            
            nombre = input("Ingrese el nombre: ").upper()
            while not validar_nombre(nombre):
                print("Dato incorrecto")
                nombre = input("Nombre: ").upper()

            apellido = input("Ingrese el apellido: ").upper()
            while not validar_apellido(apellido):
                print("Dato incorrecto")
                apellido = input("Apellido: ").upper()

            telefono = input("Ingrese el telefono: ")
            while not validar_telefono(telefono):
                print("Dato incorrecto")
                telefono = input("Telefono: ")

            correo = input("Ingrese el correo: ")
            while not validar_correo(correo):
                print("Dato incorrecto")
                correo = input("Correo: ")
            correo = correo.upper()

            contador+=1
            nuevo_paciente = {
                "id": contador,
                "dni": dni,
                "nombre": nombre,
                "apellido": apellido,
                "telefono": telefono,
                "correo": correo
            }

            lista.append(nuevo_paciente)
            print("\nPaciente agregado con éxito!\n")
            return contador
        else:
            print("\nOperación cancelada.\n")

    except ValueError:
        print ("\nDebe ingresar un número entero válido. Intente nuevamente.")
    except:
        print("\nError. Intente nuevamente.")

def eliminar_paciente(lista):
    """
    Busca un paciente por DNI y lo elimina de la lista si es encontrado. Pide confirmar la operación.
    """
    print("\n---ELIMINAR PACIENTE---\n")
    try:
        dnis=[d["dni"] for d in lista]

        dni_buscado=buscar_dni(lista)
        if dni_buscado!="0":
            index_eliminar=dnis.index(dni_buscado)
            print(f"Se va a eliminar el paciente con DNI: ",dni_buscado," Nombre y Apellido: ",lista[index_eliminar]["nombre"]+" "+lista[index_eliminar]["apellido"])
            confirmar=input("Ingresar S para confirmar, o N para cancelar: ")
            while confirmar != "S" and confirmar !="N":
                print("Opción inválida. Vuelva a intentar.")
                confirmar=input("Ingresar S para confirmar, o N para cancelar: ")
            if confirmar == "S":
                lista.pop(index_eliminar)
                print("Disponibilidad eliminada.")
            elif confirmar == "N":
                print("\nOperación cancelada.\n")
        else:
            print("\nOperación cancelada.\n")
    except ValueError:
        print("Debe ingresar un número entero válido. Intente nuevamente.")
    except:
        print("Error. Intente nuevamente.")

def modificar_paciente(lista):
    """
    Busca un paciente por DNI y permite actualizar sus datos personales
    """
    print("\n---MODIFICAR PACIENTE---\n")
    try:
        dnis=[d["dni"] for d in lista]
    
        dni_buscado=buscar_dni(lista)
        if dni_buscado!="0":
            index_modificar=dnis.index(dni_buscado)
            print(f"Se va a modificar el paciente con DNI: ",dni_buscado," Nombre y Apellido: ",lista[index_modificar]["nombre"]+" "+lista[index_modificar]["apellido"])
            
            editando = True
            while editando:
                print("\nSeleccione el dato que desea modificar:")
                print("[1] Nombre.")
                print("[2] Apellido.")
                print("[3] Teléfono.")
                print("[4] Correo.")
                print("[0] Terminar edición.")

                opcion = input("Ingrese una opción: ")

                if opcion == "0":
                    print("\nEdición terminada.\n")
                    editando = False

                elif opcion == "1":
                    nuevo_nombre = input("Ingrese el nombre: ").upper()
                    while not validar_nombre(nuevo_nombre):
                        print("Dato incorrecto")
                        nuevo_nombre = input("Nombre: ").upper()
                    lista[index_modificar]["nombre"] = nuevo_nombre
                    
                elif opcion == "2":
                    nuevo_apellido = input("Ingrese el apellido: ").upper()
                    while not validar_apellido(nuevo_apellido):
                        print("Dato incorrecto")
                        nuevo_apellido = input("Apellido: ").upper()
                    lista[index_modificar]["apellido"] = nuevo_apellido
                    
                elif opcion == "3":
                    nuevo_telefono = input("Ingrese el telefono: ")
                    while not validar_telefono(nuevo_telefono):
                        print("Dato incorrecto")
                        nuevo_telefono = input("Telefono: ")
                    nuevo_telefono = str(nuevo_telefono)
                    lista[index_modificar]["telefono"] = nuevo_telefono
                    
                elif opcion == "4":
                    nuevo_correo = input("Ingrese el correo: ")
                    while not validar_correo(nuevo_correo):
                        print("Dato incorrecto")
                        nuevo_correo = input("Correo: ")
                    nuevo_correo = nuevo_correo.upper()
                    lista[index_modificar]["correo"] = nuevo_correo

                else: 
                    print("Opción inválida.")

    except ValueError:
        print ("\nDebe ingresar un número entero válido. Intente nuevamente.")
    except:
        print("\nError. Intente nuevamente.")
