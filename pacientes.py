#Módulo
#pacientes.py

def agregar_paciente(matriz, contador):
    contador += 1
    
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
    nueva_fila = [contador, dni, nombre, apellido, telefono, correo]
    matriz.append(nueva_fila)
    print("\nDatos agregados con éxito!\n")

def eliminar_paciente(matriz):
    dni_buscador = int(input("Ingrese el DNI a eliminar: "))
    for i in range(len(matriz)):
        if int(matriz[i][1]) == dni_buscador:
            matriz.pop(i)
            print("\nPaciente eliminado correctamente.\n")
            return
    print("\nNo se encontró el DNI\n")

def modificar_paciente(matriz):
    dni_buscador = int(input("Ingrese el DNI del paciente que desea modificar datos: "))
    while dni_buscador < 10000000 or dni_buscador > 99999999:
        print("Dato incorrecto")
        dni_buscador = int(input("DNI: "))
    
    for i in range(1, len(matriz)):
        if int(matriz[i][1]) == dni_buscador:
            nombre = input("Ingrese el nombre: ").upper()
            apellido = input("Ingrese el apellido: ").upper()
            telefono = int(input("Ingrese el número de teléfono: "))
            while telefono < 1000000000 or telefono > 9999999999:
                print("Dato incorrecto")
                telefono = int(input("Telefono: "))
            
            correo = input("Ingrese el correo: ").upper()
            matriz[i] = [matriz[i][0], matriz[i][1], nombre, apellido, telefono, correo]
            print("\nPaciente modificado correctamente!\n")
            return
    print("El paciente no fue encontrado.")