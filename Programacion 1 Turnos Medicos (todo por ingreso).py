#Matrices de prueba, carga manual de todos los datos de matrices propuestas en excel (algunas restricciones para ingresos)

def crear_matriz_pacientes(pacientes):
    datos = []
    for i in range(pacientes):
        id_paciente = len(datos) + 1
        dni = int(input("DNI: "))
        while dni < 10000000 or dni > 99999999:
            print("Dato incorrecto")
            dni = int(input("DNI: "))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = int(input("Telefono: "))
        while telefono < 1000000000 or telefono > 9999999999:
            print("Dato incorrecto")
            telefono = int(input("Telefono: "))
        correo = input("Correo: ")
        ficha = [id_paciente, dni, nombre, apellido, telefono, correo]
        datos.append(ficha)
    return datos

def crear_matriz_doctores(doctores):
    datos = []
    for i in range(doctores):
        id_profesional = len(datos) + 1
        matricula = int(input("Matricula: "))
        while matricula < 10000 or matricula > 99999:
            print("Dato incorrecto")
            matricula = int(input("Matricula: "))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = int(input("Telefono: "))
        while telefono < 1000000000 or telefono > 9999999999:
            print("Dato incorrecto")
            telefono = int(input("Telefono: "))
        especialidad = input("Especialidad: ")
        ficha = [id_profesional, matricula, nombre, apellido, telefono, especialidad]
        datos.append(ficha)
    return datos

def crear_matriz_disponibilidad(registros, dia, mes, anio):
    datos = []
    for i in range(registros):
        id_disponibilidad = len(datos) + 1
        id_profesional = len(datos) + 1
        hora_inicio = int(input("Hora Inicio: "))
        while hora_inicio < 0 or hora_inicio > 12:
            print("Dato incorrecto")
            hora_inicio = int(input("Hora Inicio: "))
        am_pm_inicio = input("Ingrese AM o PM: ")
        while am_pm_inicio != 'am' and am_pm_inicio != 'pm' and am_pm_inicio != 'AM' and am_pm_inicio != 'PM':
            print("Dato incorrecto")
            am_pm_inicio = input("Ingrese AM o PM: ")
        hora_fin = int(input("Hora Fin: "))
        while hora_fin < 0 or hora_fin > 12:
            print("Dato incorrecto")
            hora_fin = int(input("Hora Fin: "))
        am_pm_fin = input("Ingrese AM o PM: ")
        while am_pm_fin != 'am' and am_pm_fin != 'pm' and am_pm_fin != 'AM' and am_pm_fin != 'PM':
            print("Dato incorrecto")
            am_pm_fin = input("Ingrese AM o PM: ")
        ficha = [id_disponibilidad, id_profesional, str(dia) + '/' + str(mes) + '/' + str(anio), str(hora_inicio) + ' ' + str(am_pm_inicio), str(hora_fin) + ' ' + str(am_pm_fin)]
        datos.append(ficha)
    return datos

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
        
# Programa principal
encabezados_pacientes = ['ID Paciente', 'DNI', 'Nombre', 'Apellido', 'Telefono', 'Correo']
encabezados_doctores = ['ID Profesional', 'Matricula', 'Nombre', 'Apellido', 'Telefono', 'Especialidad']
encabezados_matriz_disponibilidad = ['ID Disponibilidad', 'ID Profesional', 'Día', 'Hora Inicio', 'AM/PM']
encabezados_matriz_turnos = ['ID Turno', 'Fecha', 'Hora', 'ID Paciente', 'Especialidad', 'ID Profesional']

print("Menu: \n 1. Matrices de prueba \n 2. Matriz Pacientes \n 3. Matriz Profesionales \n 4. Matriz Disponibilidad \n 5. Matriz Turnos \n")
ingreso = int(input("Seleccione la matriz a cargar, 0 para terminar: "))
while ingreso != 0:
    while ingreso > 0 and ingreso < 6:
        if ingreso == 1:
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
            
        elif ingreso == 2:
            pacientes = int(input("Ingrese la cantidad de pacientes, 0 para volver al menu: "))
            while pacientes != 0:
                matriz_pacientes = crear_matriz_pacientes(pacientes)
                #print(matriz_pacientes)
                mostrar_matriz(encabezados_pacientes, matriz_pacientes)
                break
            break
        
        elif ingreso == 3:
            doctores = int(input("Ingrese la cantidad de doctores, 0 para volver al menu: "))
            while doctores != 0:
                matriz_doctores = crear_matriz_doctores(doctores)
                #print(matriz_doctores)
                mostrar_matriz(encabezados_doctores, matriz_doctores)
                break
            break
        
        elif ingreso == 4:
            registros = int(input("Ingrese la cantidad de registros a cargar, 0 para volver al menu: "))
            while registros != 0:
                dia = int(input("Ingrese el dia (1 al 31): "))
                while dia > 31:
                    print("Ingrese un dia valido")
                    dia = int(input("Ingrese el dia (1 al 31): "))
                mes = int(input("Ingrese el mes (1 al 12): "))
                while mes > 12:
                    print("Ingrese un mes valido: ")
                    mes = int(input("Ingrese el mes (1 al 12): "))
                anio = int(input("Ingrese el año: "))
                while anio < 2026:
                    print("Ingrese un año valido")
                    anio = int(input("Ingrese el año: "))
                matriz_disponibilidad = crear_matriz_disponibilidad(registros, dia, mes, anio)
                #print(matriz_disponibilidad)
                mostrar_matriz(encabezados_matriz_disponibilidad, matriz_disponibilidad)
                break
            break
                
        elif ingreso == 5:
            pass
    
        break
    
    print("Menu: \n 1. Matrices de prueba \n 2. Matriz Pacientes \n 3. Matriz Profesionales \n 4. Matriz Disponibilidad \n 5. Matriz Turnos \n")
    ingreso = int(input("Seleccione la matriz a cargar, 0 para terminar: "))










