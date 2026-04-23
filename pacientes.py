#Módulo
#pacientes.py

def agregar_paciente(lista, contador):
    dni = int(input("Ingrese el DNI: "))
    while dni < 10000000 or dni > 99999999:
        print("Dato incorrecto")
        dni = int(input("DNI: "))
    
    nombre = input("Ingrese el nombre: ").upper()
    apellido = input("Ingrese el apellido: ").upper()
    telefono = int(input("Ingrese el telefono: "))
    while telefono < 1000000000 or telefono > 9999999999:
        print("Dato incorrecto")
        telefono = int(input("Telefono: "))
    
    correo = input("Ingrese el correo: ").upper()
    
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

def eliminar_paciente(lista):
    dni_buscador = int(input("Ingrese el DNI a eliminar: "))
    for i in range(len(lista)):
        if lista[i]["dni"] == dni_buscador:
            lista.pop(i)
            print("\nPaciente eliminado correctamente.\n")
            return
    print("\nNo se encontró el DNI\n")

def modificar_paciente(lista):
    dni_buscador = int(input("Ingrese el DNI del paciente que desea modificar datos: "))
    while dni_buscador < 10000000 or dni_buscador > 99999999:
        print("Dato incorrecto")
        dni_buscador = int(input("DNI: "))
    
    for paciente in lista:
        if paciente["dni"] == dni_buscador:
            print(f"Modificando a: {paciente['nombre']} {paciente['apellido']}")

            nuevo_nombre = input("Ingrese el nuevo nombre: ").upper()
            nuevo_apellido = input("Ingrese el nuevo apellido: ").upper()
            nuevo_telefono = int(input("Ingrese el nuevo número de teléfono: "))
            while nuevo_telefono < 1000000000 or nuevo_telefono > 9999999999:
                print("Dato incorrecto")
                nuevo_telefono = int(input("Telefono: "))
            
            nuevo_correo = input("Ingrese el correo: ").upper()
            

            paciente["nombre"] = nuevo_nombre
            paciente["apellido"] = nuevo_apellido
            paciente["telefono"] = nuevo_telefono
            paciente["correo"] = nuevo_correo

            print("\nPaciente modificado correctamente!\n")
            return
    print("El paciente no fue encontrado.")