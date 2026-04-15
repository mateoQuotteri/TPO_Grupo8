# Modulo
#doctores.py

"""
FUNCIÓN AGREGAR DOCTOR
Agrega un médico a la lista realizando las siguientes validaciones:
1. Matrícula: Debe ser de 5 dígitos y no estar repetida.
2. Teléfono: Debe tener exactamente 10 dígitos.
3. Especialidad: Se elige mediante un menú numérico predefinido.
4. Estado: Solo acepta 'S' (Activo) o 'N' (Inactivo).
Al finalizar, guarda los datos en la matriz y actualiza el contador.
"""

def agregar_doctor(matriz, contador):
    
    matricula = int(input("Ingrese el número de matricula: "))
    while matricula < 10000 or matricula > 99999:
            print("Dato incorrecto")
            matricula = int(input("Ingrese el número de matricula: "))
    
    encontrado = False
    indice = 1

    while indice < len(matriz) and not encontrado:
        if matriz[indice][1] == matricula:
            print("La matrícula ya está asociada a un doctor.")
            encontrado = True
        else:
            indice += 1
    
    if not encontrado:
        contador += 1
        nombre = input("Ingrese el nombre: ").upper()
        apellido = input("Ingrese el apellido: ").upper()
        telefono = int(input("Ingrese el telefono: "))
        while telefono < 1000000000 or telefono > 9999999999:
            print("Dato incorrecto.")
            telefono = int(input("Ingrese el número de teléfono: "))
        
        especialidades = ["CLÍNICA MÉDICA", "PEDIATRÍA", "GINECOLOGÍA Y OBSTETRICIA", "CARDIOLOGÍA", "OFTALMOLOGÍA", "ODONTOLOGÍA", "DERMATOLOGÍA", "TRAUMATOLOGÍA"]
        print("Seleccione una especialidad: ")
        for i in range(len(especialidades)):
            print(i + 1, "-", especialidades[i])
        
        opcion = int(input("Ingrese el número de su especialidad: "))
        while opcion < 1 or opcion > len(especialidades):
            print("Opcion invalida, seleccione una de las disponibles")
            opcion = int(input("Ingrese el número de su especialidad: "))
        
        especialidad = especialidades[opcion - 1]

        activo = input("Ingrese `S` para activo o `N` para inactivo: ").upper()
        while activo != "S" and activo != "N":
            print("Dato incorrecto. Ingrese `S` para activo o `N` para inactivo.")
            activo = input("Ingrese `S` para activo o `N` para inactivo: ").upper()
        
        
        nueva_fila = [contador, matricula, nombre, apellido, telefono, especialidad, activo]
        matriz.append(nueva_fila)
        print("\nDatos agregados con éxito!\n")
    return contador

"""
FUNCIÓN ELIMINAR DOCTOR
Busca un doctor por su matrícula y lo borra de la lista.
Si encuentra el número, elimina la fila completa de la matriz.
Si no lo encuentra, avisa que la matrícula no existe.
"""

def eliminar_doctor(matriz):
    matricula_buscada = int(input("Ingrese la matricula a eliminar: "))
    
    for i in range(len(matriz)):
        if int(matriz[i][1]) == matricula_buscada:
            matriz.pop(i)
            print("\nDoctor eliminado correctamente.\n")
            return
    print("\nNo se encontró la matricula\n")

"""
FUNCIÓN MODIFICAR DOCTOR
Permite editar los datos de un doctor ya registrado:
1. Localiza al doctor mediante su matrícula (5 dígitos).
2. Abre un menú interactivo para elegir qué cambiar: Nombre, Apellido, Teléfono, Especialidad o Estado (Activo/Inactivo).
3. Valida que los nuevos datos ingresados sean correctos.
4. Permite realizar múltiples cambios hasta que se elige "Terminar edición".
"""

def modificar_doctor(matriz):
    matricula_buscada = int(input("Ingrese la matricula del doctor que desea modificar: "))
    while matricula_buscada < 10000 or matricula_buscada > 99999:
        print("Dato incorrecto")
        matricula_buscada = int(input("Ingrese la matricula del doctor que desea modificar: "))
    
    encontrado = False
    i = 1

    while i < len(matriz) and not encontrado:
        if int(matriz[i][1]) == matricula_buscada:
            encontrado = True

            editando = True
            while editando:
                print("\nSeleccione el dato que desea modificar:")
                print("[1] Nombre")
                print("[2] Apellido")
                print("[3] Teléfono")
                print("[4] Especialidad")
                print("[5] Activo/Inactivo")
                print("[0] Terminar edición")
                
                opcion = input("Ingrese una opción: ")
                
                if opcion == "0":
                    print("\nEdición terminada.\n")
                    editando = False
                
                if opcion == "1": #Modifica matriz nombre
                    matriz[i][2] = input("Ingrese el nuevo nombre: ").upper()
                
                elif opcion == "2": # Modifica matriz apellido
                    matriz[i][3] = input("Ingrese el nuevo apellido: ").upper()
                
                elif opcion == "3": #Modifica matriz telefono
                    telefono = int(input("Ingrese el nuevo teléfono: "))
                    while telefono < 1000000000 or telefono > 9999999999:
                        print("Dato incorrecto")
                        telefono = int(input("Ingrese el nuevo teléfono: "))
                    matriz[i][4] = telefono
                
                elif opcion == "4": #Modifica matriz especialidad
                    especialidades = ["CLÍNICA MÉDICA", "PEDIATRÍA", "GINECOLOGÍA Y OBSTETRICIA", "CARDIOLOGÍA", "OFTALMOLOGÍA", "ODONTOLOGÍA", "DERMATOLOGÍA", "TRAUMATOLOGÍA"]
                    print("Seleccione una especialidad: ")
                    for j in range(len(especialidades)):
                        print(j + 1, "-", especialidades[j])
        
                    opcion_esp = int(input("Ingrese el número de su especialidad: "))
                    while opcion_esp < 1 or opcion_esp > len(especialidades):
                        print("Opcion invalida, seleccione una de las disponibles")
                        opcion_esp = int(input("Ingrese el número de su especialidad: "))
                    matriz[i][5] = especialidades[opcion_esp - 1]
                
                elif opcion == "5": #Modifica matriz activo/inactivo
                    activo = input("Ingrese `S` para activo o `N` para inactivo: ").upper()
                    while activo != "S" and activo != "N":
                        print("Dato incorrecto. Ingrese `S` para activo o `N` para inactivo.")
                        activo = input("Ingrese `S` para activo o `N` para inactivo: ").upper()
                    matriz[i][6] = activo    
        else:
            i += 1
    if not encontrado:
        print("\nNo se encontró la matricula\n")  
