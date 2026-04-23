#Módulo
#pacientes.py

import re

# Valida que el nombre solo contenga letras y espacios NO permite números ni caracteres especiales
def validar_nombre(nombre):
    return bool(re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$', nombre)) and nombre.strip() != ""

# Valida que el apellido solo permita letras y espacios
def validar_apellido(apellido):
    return bool(re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$', apellido)) and apellido.strip() != ""

# El DNI debe tener exactamente 8 dígitos y no contenga letras
def validar_dni(dni):
    return bool(re.match(r'^\d{8}$', dni))

# Telefono tenga exactamente 10 dígitos y no contenga letras
def validar_telefono(telefono):
    return bool(re.match(r'^\d{10}$', telefono))

# Valida que el correo tenga formato válido La validacion : usuario@dominio.ext
def validar_correo(correo):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', correo))

# Solicita datos, valida el formato y añade un nuevo paciente a la lista
def agregar_paciente(lista, contador):
    dni_str = input("Ingrese el DNI: ")
    while not validar_dni(dni_str):
        print("Dato incorrecto")
        dni_str = input("DNI: ")
    dni = int(dni_str)

    nombre = input("Ingrese el nombre: ").upper()
    while not validar_nombre(nombre):
        print("Dato incorrecto")
        nombre = input("Nombre: ").upper()

    apellido = input("Ingrese el apellido: ").upper()
    while not validar_apellido(apellido):
        print("Dato incorrecto")
        apellido = input("Apellido: ").upper()

    telefono_str = input("Ingrese el telefono: ")
    while not validar_telefono(telefono_str):
        print("Dato incorrecto")
        telefono_str = input("Telefono: ")
    telefono = int(telefono_str)

    correo = input("Ingrese el correo: ")
    while not validar_correo(correo):
        print("Dato incorrecto")
        correo = input("Correo: ")
    correo = correo.upper()
    
    nuevo_paciente = {
        "id": contador,
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "correo": correo
    }
    
    lista.append(nuevo_paciente)
    print("\nDatos agregados con éxito!\n")

# Busca un paciente por DNI y lo elimina de la lista si es encontrado
def eliminar_paciente(lista):
    dni_buscador = int(input("Ingrese el DNI a eliminar: "))

    indice_encontrado = -1
    for i in range(len(lista)):
        if int(lista[i]["dni"]) == dni_buscador:
            indice_encontrado = i

    if indice_encontrado != -1:
        lista.pop(indice_encontrado)
        print("Paciente eliminado correctamente.")
    else:
        print("No se encontró ningún paciente con ese DNI.")

# Busca un paciente por DNI y permite actualizar sus datos personales
def modificar_paciente(lista):
    dni_buscador = int(input("Ingrese el DNI del paciente que desea modificar datos: "))
    while dni_buscador < 10000000 or dni_buscador > 99999999:
        print("Dato incorrecto")
        dni_buscador = int(input("DNI: "))

    encontrado = False
    for paciente in lista:
        if int(paciente["dni"]) == dni_buscador:
            encontrado = True
            print(f"Modificando a: {paciente['nombre']} {paciente['apellido']}")

            nuevo_nombre = input("Ingrese el nuevo nombre: ").upper()
            nuevo_apellido = input("Ingrese el nuevo apellido: ").upper()
            nuevo_telefono = int(input("Ingrese el nuevo número de teléfono: "))
            while nuevo_telefono < 1000000000 or nuevo_telefono > 9999999999:
                print("Dato incorrecto")
                nuevo_telefono = int(input("Ingrese el nuevo teléfono (10 dígitos): "))
            
            nuevo_correo = input("Ingrese el correo: ").upper()
            

            paciente["nombre"] = nuevo_nombre
            paciente["apellido"] = nuevo_apellido
            paciente["telefono"] = nuevo_telefono
            paciente["correo"] = nuevo_correo

            print("\nPaciente modificado correctamente.\n")

    if encontrado == False:
        print("El paciente no fue encontrado.")