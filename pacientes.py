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
    try:
        dni_str = input("Ingrese el DNI: ")
        try:
            dni = int(dni_str)
            if not validar_dni(dni_str):
                raise ValueError("DNI inválido.")
        except ValueError as e:
            print(e)
            return contador

        # Validar duplicado
        for paciente in lista:
            if str(paciente["dni"]) == str(dni):
                print("Error: El paciente ya está registrado.")
                return contador

        nombre = input("Ingrese el nombre: ").upper()
        if not validar_nombre(nombre):
            print("Nombre inválido.")
            return contador

        apellido = input("Ingrese el apellido: ").upper()
        if not validar_apellido(apellido):
            print("Apellido inválido.")
            return contador

        telefono_str = input("Ingrese el teléfono: ")
        try:
            telefono = int(telefono_str)
            if not validar_telefono(telefono_str):
                raise ValueError("Teléfono inválido.")
        except ValueError as e:
            print(e)
            return contador

        correo = input("Ingrese el correo: ").upper()
        if not validar_correo(correo):
            print("Correo inválido.")
            return contador

        contador += 1
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

    except Exception as e:
        print(f"Error inesperado: {e}")
        return contador

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
        input("Presione ENTER para volver al menú...")
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

            nuevo_nombre = input("Ingrese el nombre: ").upper()
            while not validar_nombre(nuevo_nombre):
                print("Dato incorrecto")
                nuevo_nombre = input("Nombre: ").upper()

            nuevo_apellido = input("Ingrese el apellido: ").upper()
            while not validar_apellido(nuevo_apellido):
                print("Dato incorrecto")
                nuevo_apellido = input("Apellido: ").upper()

            nuevo_telefono = input("Ingrese el telefono: ")
            while not validar_telefono(nuevo_telefono):
                print("Dato incorrecto")
                nuevo_telefono = input("Telefono: ")
            nuevo_telefono = int(nuevo_telefono)
            
            nuevo_correo = input("Ingrese el correo: ")
            while not validar_correo(nuevo_correo):
                print("Dato incorrecto")
                nuevo_correo = input("Correo: ")
            nuevo_correo = nuevo_correo.upper()
            
            paciente["nombre"] = nuevo_nombre
            paciente["apellido"] = nuevo_apellido
            paciente["telefono"] = nuevo_telefono
            paciente["correo"] = nuevo_correo

            print("\nPaciente modificado correctamente.\n")

    if encontrado == False:
        print("El paciente no fue encontrado.")