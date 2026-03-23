#Matrices de prueba y ABM completo de paciente unicamente, filtrado por DNI, no estoy pudiendo lograr filtrar el primer ingreso,
#tengo que consultar con el profesor para que me diga que puedo hacer, ya que chatgpt dice que es un error de tipo de dato al momento de comparar.
#En este programa no valido los ingresos, pero es algo que tranquilamente se puede tomar de la otra version (aunque solo era algo base para tener).

def agregar_paciente(matriz):
    global contador_id_paciente
    contador_id_paciente += 1
    dni = int(input("Ingrese el DNI: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = int(input("Ingrese el telefono: "))
    correo = input("Ingrese el correo: ")
    nueva_fila = [contador_id_paciente, dni, nombre, apellido, telefono, correo]
    matriz.append(nueva_fila)
    print("Datos agregados con exito")

def eliminar_paciente(matriz):
    dni_buscador = int(input("Ingrese el DNI a eliminar: "))

    for i in range(1, len(matriz)):
        if int(matriz[i][1]) == dni_buscador:
            matriz.pop(i)
            print("Paciente eliminado correctamente\n")
            return

    print("\nNo se encontró el DNI\n")

def modificar_paciente(matriz):
    dni_buscador = int(input("Ingrese el DNI del paciente que desea modificar datos: "))
    for i in range(1, len(matriz)):
        if int(matriz[i][1]) == dni_buscador:
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            telefono = int(input("Ingrese el telefono: "))
            correo = input("Ingrese el correo: ")
            matriz[i] = [matriz[i][0], matriz[i][1], nombre, apellido, telefono, correo]
            print("Paciente modificado correctamente")
            return
    print("El paciente no fue encontrado")

def mostrar_matriz(encabezados, matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for titulo in encabezados:
        print(titulo, end="\t")
    print()
    for fila in range(filas):
        for columna in range(columnas):
            print(matriz[fila][columna], end="\t")
        print()




#PROGRAMA PRINCIPAL
encabezados_pacientes = ['ID Paciente', 'DNI', 'Nombre', 'Apellido', 'Telefono', 'Correo']
encabezados_doctores = ['ID Profesional', 'Matricula', 'Nombre', 'Apellido', 'Telefono', 'Especialidad']
matriz_pacientes = []
matriz_doctores = []
contador_id_paciente = 0

print("MENU PRINCIPAL\n\n 1. Mostrar Matrices de Prueba.\n 2. ABM Paciente.\n 3. ABM Doctor\n 4. ABM Disponibilidad Doctores.\n 5. ABM Turnos.\n")
opciones = int(input("Ingrese la opcion deseada, 0 para terminar: "))
while opciones != 0:
    if opciones == 1:
        print("\n MATRIZ PACIENTES \n")
        matriz_pacientes_prueba = []
        matriz_pacientes_prueba.append(encabezados_pacientes)
        dni_paciente = ["12345678", "87654321", "56781234", "43215678"]
        nombre_paciente = ["Jose", "Ivana", "Mateo", "Evelyn"]
        apellido_paciente = ["Sanchez", "Cervera", "Lopez", "Sanchez"]
        telefono_paciente = ["1234567890", "0987654321", "1234509876", "6789012345"]
        correo_paciente = ["josesan@gmail.com", "ivanacer@gmail.com", "mateolo@gmail.com", "evelynsan@gmail.com"]
        id_contador_pacientes = 1
        for i in range(4):
            fila_pacientes = [id_contador_pacientes, dni_paciente[i], nombre_paciente[i], apellido_paciente[i], telefono_paciente[i], correo_paciente[i]]
            matriz_pacientes_prueba.append(fila_pacientes)
            id_contador_pacientes += 1
        for fila in matriz_pacientes_prueba:
            print(fila)
            
        print("\n MATRIZ DOCTORES \n")
        matriz_doctores_prueba = []
        matriz_doctores_prueba.append(encabezados_doctores)
        matricula_doctor = ["12345", "67890", "54321", "09876"]
        nombre_doctor = ["Bruno", "Carmen", "Nadia", "Guada"]
        apellido_doctor = ["Gonzales", "Rivera", "Correa", "Smith"]
        telefono_doctor = ["3478125690", "1256903478", "0965213478", "8743561290"]
        especialidad_doctor = ["Clinica", "Oftalmologia", "Cardiologia", "Oncologia"]
        id_contador_doctores = 1
        for i in range(4):
            fila_doctores = [id_contador_doctores, matricula_doctor[i], nombre_doctor[i], apellido_doctor[i], telefono_doctor[i], especialidad_doctor[i]]
            matriz_doctores_prueba.append(fila_doctores)
            id_contador_doctores += 1
        for fila in matriz_doctores_prueba:
            print(fila)
        break
    elif opciones == 2:
        print("\n 1. Agregar Paciente.\n 2. Eliminar Paciente.\n 3. Modificar Paciente\n")
        opcion_pacientes = int(input("Seleccione la opcion deseada, 0 para volver al menu principal: "))
        while opcion_pacientes != 0:
            if opcion_pacientes == 1:
                agregar_paciente(matriz_pacientes)
                mostrar_matriz(encabezados_pacientes, matriz_pacientes)
                break
            elif opcion_pacientes == 2:
                eliminar_paciente(matriz_pacientes)
                mostrar_matriz(encabezados_pacientes, matriz_pacientes)
                break
            elif opcion_pacientes == 3:
                modificar_paciente(matriz_pacientes)
                mostrar_matriz(encabezados_pacientes, matriz_pacientes)
                break
            elif opcion_pacientes > 3:
                print("La opcion no existe")
                print("\n 1. Agregar Paciente.\n 2. Eliminar Paciente.\n 3. Modificar Paciente\n")
                opcion_pacientes = int(input("Seleccione la opcion deseada, 0 para volver al menu principal: "))
        if opcion_pacientes == 0:
            print("Volviendo al Menu Principal")
            print("MENU PRINCIPAL\n\n 1. Mostrar Matrices de Prueba.\n 2. ABM Paciente.\n 3. ABM Doctor\n 4. ABM Disponibilidad Doctores.\n 5. ABM Turnos.\n")
            opciones = int(input("Ingrese la opcion deseada, 0 para terminar: "))
    elif opciones == 3:
        pass
    elif opciones == 4:
        pass
    elif opciones == 5:
        pass
    elif opciones > 5:
        print("La Opcion no Existe")
        print("MENU PRINCIPAL\n\n 1. Mostrar Matrices de Prueba.\n 2. ABM Paciente.\n 3. ABM Doctor\n 4. ABM Disponibilidad Doctores.\n 5. ABM Turnos.\n")
        opciones = int(input("Ingrese la opcion deseada, 0 para terminar: "))

