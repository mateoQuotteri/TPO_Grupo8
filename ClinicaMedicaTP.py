#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
# convierte hora de formato 12hs AM/PM a formato 24hs
def convertir_hora(hora, am_pm):
    if am_pm == "PM" and hora != 12:
        return hora + 12
    elif am_pm == "AM" and hora == 12:
        return 0
    return hora

#FUNCIONES DE PACIENTES
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
    for i in range(1, len(matriz)):
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


# FUNCIONES DE DOCTORES
def agregar_doctor(matriz, contador):
    contador += 1
    
    matricula = int(input("Ingrese el número de matricula: "))
    while matricula < 10000 or matricula > 99999:
            print("Dato incorrecto")
            matricula = int(input("Ingrese el número de matricula: "))
    
    encontrado = False
    for fila in matriz[1:]:
        if fila[1] == matricula:
            print("La matricula ya esta asociada a un doctor.")
            encontrado = True
            break
    
    if not encontrado:
        nombre = input("Ingrese el nombre: ").upper()
        apellido = input("Ingrese el apellido: ").upper()
        telefono = int(input("Ingrese el telefono: "))
        while telefono < 1000000000 or telefono > 9999999999:
            print("Dato incorrecto.")
            telefono = int(input("Ingrese el número de teléfono: "))
        
        especialidades = ["Clínica Médica", "Pediatría", "Ginecología y Obstetricia", "Cardiología", "Oftalmología","Odontología","Dermatología","Traumatología"]
        print("Seleccione una especialidad: ")
        for i in range(len(especialidades)):
            print(i + 1, "-", especialidades[i])
        
        opcion = int(input("Ingrese el número de su especialidad: "))
        while opcion < 1 or opcion > len(especialidades):
            print("Opcion invalida, seleccione una de las disponibles")
            opcion = int(input("Ingrese el número de su especialidad: "))
        
        especialidad = especialidades[opcion - 1]
        
        nueva_fila = [contador, matricula, nombre, apellido, telefono, especialidad]
        matriz.append(nueva_fila)
        print("\nDatos agregados con éxito!\n")
    return contador

def eliminar_doctor(matriz):
    matricula_buscada = int(input("Ingrese la matricula a eliminar: "))
    
    for i in range(1, len(matriz)):
        if int(matriz[i][1]) == matricula_buscada:
            matriz.pop(i)
            print("\nDoctor eliminado correctamente.\n")
            return
    print("\nNo se encontró la matricula\n")

def modificar_doctor(matriz):
    matricula_buscada = int(input("Ingrese la matricula del doctor que desea modificar: "))
    while matricula_buscada < 10000 or matricula_buscada > 99999:
        print("Dato incorrecto")
        matricula_buscada = int(input("Ingrese la matricula del doctor que desea modificar: "))
    
    for i in range(1, len(matriz)):
        if int(matriz[i][1]) == matricula_buscada:
        
         while True:
                print("\nSeleccione el dato que desea modificar:")
                print("[1] Nombre")
                print("[2] Apellido")
                print("[3] Teléfono")
                print("[4] Especialidad")
                print("[0] Terminar edición")
                
                opcion = input("Ingrese una opción: ")
                
                if opcion == "0":
                    print("\nEdición terminada.\n")
                    return # Termina la función
                
                if opcion == "1": #Modifica matriz nombre
                    matriz[i][2] = input("Ingrese el nuevo nombre: ").upper()
                
                elif opcion == "2": # Modifica matriz apellido
                    matriz[i][3] = input("Ingrese el nuevo apellido: ").upper()
                
                elif opcion == "3": #Modifica matriz telefono
                    telefono = input("Ingrese el nuevo teléfono: ").upper()
                    while telefono < 1000000000 or telefono > 9999999999:
                        print("Dato incorrecto")
                        telefono = int(input("Ingrese el nuevo teléfono: "))
                    matriz[i][4] = telefono
                
                elif opcion == "4": #Modifica matriz especialidad
                    especialidades = ["Clínica Médica", "Pediatría", "Ginecología y Obstetricia", "Cardiología", "Oftalmología","Odontología","Dermatología","Traumatología"]
                    print("Seleccione una especialidad: ")
                    for j in range(len(especialidades)):
                        print(j + 1, "-", especialidades[j])
        
                    opcion_esp = int(input("Ingrese el número de su especialidad: "))
                    while opcion_esp < 1 or opcion_esp > len(especialidades):
                        print("Opcion invalida, seleccione una de las disponibles")
                        opcion_esp = int(input("Ingrese el número de su especialidad: "))
                    matriz[i][5] = especialidades[opcion_esp - 1]
                
                else:
                    print("Opción inválida, intente nuevamente.")
    print("\nNo se encontró la matricula\n")  

#FUNCIONES DE DISPONIBILIDAD

#Agregar una nueva disponibilidad a la matriz de disponibilidad
def agregar_disponibilidad(matriz_disponibilidad, id_contador):
    print("\n--- AGREGAR DISPONIBILIDAD ---")

    matricula = input("Ingrese matrícula del doctor: ")
    dia = input("Ingrese día (Ej: Lunes): ")
    hora_inicio = int(input("Hora inicio (0-23): "))
    hora_fin = int(input("Hora fin (0-23): "))

    # VALIDACIÓN SIMPLE
    if hora_inicio >= hora_fin:
        print("Error: hora inicio debe ser menor que hora fin.")
        return

    # VALIDAR DUPLICADO (mismo doctor, mismo día y rango igual)
    for fila in matriz_disponibilidad[1:]:
        if fila[1] == matricula and fila[2] == dia:
            if fila[3] == hora_inicio and fila[4] == hora_fin:
                print("Error: disponibilidad duplicada.")
                return

    nueva_fila = [id_contador, matricula, dia, hora_inicio, hora_fin]
    matriz_disponibilidad.append(nueva_fila)

    print("Disponibilidad agregada correctamente.")

# Eliminar una disponibilidad de la matriz de disponibilidad
def eliminar_disponibilidad(matriz_disponibilidad):
    print("\n--- ELIMINAR DISPONIBILIDAD ---")

    id_buscar = input("Ingrese ID de disponibilidad a eliminar: ")

    for i in range(1, len(matriz_disponibilidad)):
        if str(matriz_disponibilidad[i][0]) == id_buscar:
            matriz_disponibilidad.pop(i)
            print("Disponibilidad eliminada.")
            return

    print("Error: no se encontró el ID.")

#Modificar una disponibilidad de la matriz de disponibilidad
def modificar_disponibilidad(matriz_disponibilidad):
    print("\n--- MODIFICAR DISPONIBILIDAD ---")

    id_buscar = input("Ingrese ID de disponibilidad a modificar: ")

    for fila in matriz_disponibilidad[1:]:
        if str(fila[0]) == id_buscar:

            print("Deje vacío para no modificar")

            nueva_matricula = input("Nueva matrícula: ")
            nuevo_dia = input("Nuevo día: ")
            nueva_hora_inicio = input("Nueva hora inicio: ")
            nueva_hora_fin = input("Nueva hora fin: ")

            if nueva_matricula != "":
                fila[1] = nueva_matricula

            if nuevo_dia != "":
                fila[2] = nuevo_dia

            if nueva_hora_inicio != "":
                fila[3] = int(nueva_hora_inicio)

            if nueva_hora_fin != "":
                fila[4] = int(nueva_hora_fin)

            # VALIDACIÓN SIMPLE
            if fila[3] >= fila[4]:
                print("Error: rango horario inválido.")
                return

            print("Disponibilidad modificada correctamente.")
            return

    print("Error: no se encontró el ID.")

# FUNCIONES DE TURNOS
def agregar_turno(matriz_turnos, matriz_pacientes, matriz_doctores, contador):
    contador += 1
    
    dia = int(input("Ingrese el día (1 al 31): "))
    while dia > 31 or dia < 1:
        print("Ingrese un dia válido.")
        dia = int(input("Ingrese el día (1 al 31): "))
    
    mes = int(input("Ingrese el mes (1 al 12): "))
    while mes > 12 or mes < 1:
        print("Ingrese un mes válido: ")
        mes = int(input("Ingrese el mes (1 al 12): "))
    
    anio = int(input("Ingrese el año: "))
    while anio < 2026:
        print("Ingrese un año válido.")
        anio = int(input("Ingrese el año: "))
    
    hora_turno = int(input("Ingrese la hora del turno: "))
    while hora_turno < 1 or hora_turno > 12:
        print("Dato incorrecto.")
        hora_turno = int(input("Ingrese la hora del turno: "))
    
    am_pm_turno = input("Ingrese AM o PM: ").upper()
    while am_pm_turno != 'AM' and am_pm_turno != 'PM':
        print("Dato incorrecto.")
        am_pm_turno = input("Ingrese AM o PM: ").upper()
    hora_turno_num = convertir_hora(hora_turno, am_pm_turno)
    
    contador_pacientes = 1
    print("\n\nSeleccione al paciente\n\n")
    for fila in matriz_pacientes[1:]:
        print(f"{contador_pacientes}. DNI: {fila[1]} - Nombre: {fila[2]} - Apellido: {fila[3]}")
        contador_pacientes += 1
    
    opcion_pacientes = int(input("\n\nSeleccione al paciente:\n"))
    while opcion_pacientes < 1 or opcion_pacientes > len(matriz_pacientes)-1:
        print("Opcion inválida.")
        opcion_pacientes = int(input("\n\nSeleccione al paciente\n"))
    opcion_elegida_pacientes = matriz_pacientes[opcion_pacientes]
    
    contador_doctores = 1
    print("\n\nSeleccione al doctor\n\n")
    for fila in matriz_doctores[1:]:
        print(f"{contador_doctores}. Matricula: {fila[1]} - Especialidad: {fila[5]}")
        contador_doctores += 1
   
    opcion_doctores = int(input("\n\nSeleccione al doctor:\n"))
    while opcion_doctores < 1 or opcion_doctores > len(matriz_doctores)-1:
        print("Opcion inválida")
        opcion_doctores = int(input("\n\nSeleccione al doctor\n"))
    opcion_elegida_doctores = matriz_doctores[opcion_doctores]

    fecha = str(dia) + '/' + str(mes) + '/' + str(anio)
    hora = str(hora_turno) + ' ' + am_pm_turno
    doctor = opcion_elegida_doctores[1]
    
    # VALIDAR DISPONIBILIDAD
    # Bandera
    disponible = False

    #Recorre la matriz buscando coincidencias 
    for fila in matriz_disponibilidad[1:]:
        matricula_disp = fila[1]
        fecha_disp = fila[2]
    
    # convertir horas de disponibilidad
        hora_inicio_str = fila[3].split()
        hora_fin_str = fila[4].split()
    
        hora_inicio = convertir_hora(int(hora_inicio_str[0]), hora_inicio_str[1])
        hora_fin = convertir_hora(int(hora_fin_str[0]), hora_fin_str[1])

        #compara matricula, dia y horario 
        if matricula_disp == doctor and fecha_disp == fecha:
            if hora_inicio <= hora_turno_num <= hora_fin:
                disponible = True
                break

    if not disponible:
        print("Error: El doctor no atiende en ese día y horario.")
        return
    
    duplicado = False
    for fila in matriz_turnos[1:]:
        if fila[1] == fecha and fila[2] == hora and fila[5] == doctor:
            duplicado = True
            break
    if duplicado:
        print("Error: El doctor no está disponible en ese día y horario.")
    else:
        nueva_fila = [contador, fecha, hora, opcion_elegida_pacientes[1], opcion_elegida_doctores[5], doctor]
        matriz_turnos.append(nueva_fila)
        print("\nDatos agregados con éxito!\n")

def eliminar_turno(matriz):
    dni_buscado = int(input("Ingrese el DNI asociado al turno a eliminar: "))
    while dni_buscado < 10000000 or dni_buscado > 99999999:
        print("Dato incorrecto")
        dni_buscado = int(input("Ingrese el DNI asociado al turno a eliminar: "))
    
    cantidad_turnos = []
    contador = 1
    
    for i in range(1, len(matriz)):
        if int(matriz[i][3]) == dni_buscado:
            print(contador, "-", matriz[i])
            cantidad_turnos.append(i)
            contador += 1
    
    if len(cantidad_turnos) == 0:
        print("El DNI no tiene turnos asociados")
        return
    
    turno_para_eliminar = int(input("Ingrese el numero de turno a eliminar: "))
    while turno_para_eliminar < 1 or turno_para_eliminar > len(cantidad_turnos):
        print("Opcion Invalida")
        turno_para_eliminar = int(input("Ingrese el numero de turno a eliminar: "))
    
    indice_eliminado = cantidad_turnos[turno_para_eliminar - 1]
    matriz.pop(indice_eliminado)
    print("\nTurno eliminado con éxito!\n")

def modificar_turno(matriz_turnos, matriz_doctores):
    dni_buscado = int(input("Ingrese el DNI asociado al turno a modificar: "))
    while dni_buscado < 10000000 or dni_buscado > 99999999:
        print("Dato incorrecto")
        dni_buscado = int(input("Ingrese el DNI asociado al turno a modificar: "))
    cantidad_turnos = []
    contador = 1
    for i in range(1, len(matriz_turnos)):
        if int(matriz_turnos[i][3]) == dni_buscado:
            print(contador, "-", matriz_turnos[i])
            cantidad_turnos.append(i)
            contador += 1
    if len(cantidad_turnos) == 0:
        print("El DNI no tiene turnos asociados")
        return
    turno_para_modificar = int(input("Ingrese el numero de turno a modificar: "))
    while turno_para_modificar < 1 or turno_para_modificar > len(cantidad_turnos):
        print("Opcion Invalida")
        turno_para_modificar = int(input("Ingrese el numero de turno a modificar: "))
    indice_modificado = cantidad_turnos[turno_para_modificar - 1]
    for i in range(1, len(matriz_turnos)):
        if int(matriz_turnos[i][3]) == dni_buscado:
            dia = int(input("Ingrese el dia (1 al 31): "))
            while dia > 31 or dia < 1:
                print("Ingrese un dia valido")
                dia = int(input("Ingrese el dia (1 al 31): "))
            mes = int(input("Ingrese el mes (1 al 12): "))
            while mes > 12 or mes < 1:
                print("Ingrese un mes valido: ")
                mes = int(input("Ingrese el mes (1 al 12): "))
            anio = int(input("Ingrese el año: "))
            while anio < 2026:
                print("Ingrese un año valido")
                anio = int(input("Ingrese el año: "))
            hora_turno = int(input("Ingrese la hora del turno: "))
            while hora_turno < 1 or hora_turno > 12:
                print("Dato incorrecto")
                hora_turno = int(input("Ingrese la hora del turno: "))
            am_pm_turno = input("Ingrese AM o PM: ").upper()
            while am_pm_turno != 'AM' and am_pm_turno != 'PM':
                print("Dato incorrecto")
                am_pm_turno = input("Ingrese AM o PM: ").upper()
            contador_doctores = 1
            print("\nLISTA DE DOCTORES\n")
            for fila in matriz_doctores[1:]:
                print(f"{contador_doctores}. Matricula: {fila[1]} - Especialidad: {fila[5]}")
                contador_doctores += 1
            opcion_doctores = int(input("\n\nSeleccione al doctor\n"))
            while opcion_doctores < 1 or opcion_doctores > len(matriz_doctores)-1:
                print("Opcion Invalida")
                opcion_doctores = int(input("\n\nSeleccione al doctor\n"))
            opcion_elegida_doctores = matriz_doctores[opcion_doctores]
            fecha = str(dia) + '/' + str(mes) + '/' + str(anio)
            hora = str(hora_turno) + ' ' + am_pm_turno
            doctor = opcion_elegida_doctores[1]
            duplicado = False
            for fila in matriz_turnos[1:]:
                if fila[1] == fecha and fila[2] == hora and fila[5] == doctor:
                    duplicado = True
                    break
            if duplicado:
                print("Error: el doctor ya tiene un turno en esa fecha y hora")
            else:
                matriz_turnos[indice_modificado] = [contador - 1, fecha, hora, dni_buscado, opcion_elegida_doctores[5], doctor] #aca me falta arreglar que mantenga el indice del turno modificado
                print("\nDatos modificados con exito\n")


def ordenar_matriz(matriz):
    opciones = matriz[0]
    print("Ingrese la opcion por la cual ordenar la matriz: ")
    for i in range(len(opciones)):
        print(i + 1, "-", opciones[i])
    while True:
        opcion = int(input("Ingrese la opcion por la cual desea ordenar la matriz: "))
        if 1 <= opcion <= len(opciones):
            columna_a_ordenar = opcion - 1
            break
        else:
            print("Opcion invalida, seleccione una de las disponibles")
    for i in range(1, len(matriz)):
        for j in range(1, len(matriz) - 1):
            if matriz[j][columna_a_ordenar] > matriz[j + 1][columna_a_ordenar]:
                aux = matriz[j]
                matriz[j] = matriz[j + 1]
                matriz[j + 1] = aux
    return matriz


def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(filas):
        for columna in range(columnas):
            print(matriz[fila][columna], end="\t")
        print()

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

encabezados_pacientes = ['ID Paciente', 'DNI', 'Nombre', 'Apellido', 'Telefono', 'Correo']
encabezados_doctores = ['ID Profesional', 'Matricula', 'Nombre', 'Apellido', 'Telefono', 'Especialidad']
encabezados_disponibilidad = ['ID Disponibilidad', 'Matricula', 'Día', 'Hora Inicio', 'Hora Fin']
encabezados_turnos = ['ID Turno', 'Fecha', 'Hora', 'DNI Paciente', 'Especialidad', 'Matricula Doctor']

print("\n MATRIZ PACIENTES \n")
matriz_pacientes = []
matriz_pacientes.append(encabezados_pacientes)
dni_paciente = ["12345678", "87654321", "56781234", "43215678"]
nombre_paciente = ["Jose", "Ivana", "Mateo", "Evelyn"]
apellido_paciente = ["Sanchez", "Cervera", "Lopez", "Sanchez"]
telefono_paciente = ["1234567890", "0987654321", "1234509876", "6789012345"]
correo_paciente = ["josesan@gmail.com", "ivanacer@gmail.com", "mateolo@gmail.com", "evelynsan@gmail.com"]
id_contador_pacientes = 0
for i in range(4):
    id_contador_pacientes += 1
    fila_pacientes = [id_contador_pacientes, dni_paciente[i], nombre_paciente[i], apellido_paciente[i], telefono_paciente[i], correo_paciente[i]]
    matriz_pacientes.append(fila_pacientes)
for fila in matriz_pacientes:
    print(fila)

print("\n MATRIZ DOCTORES \n")
matriz_doctores = []
matriz_doctores.append(encabezados_doctores)
matricula_doctor = ["12345", "67890", "54321", "09876"]
nombre_doctor = ["Bruno", "Carmen", "Nadia", "Guada"]
apellido_doctor = ["Gonzales", "Rivera", "Correa", "Smith"]
telefono_doctor = ["3478125690", "1256903478", "0965213478", "8743561290"]
especialidad_doctor = ["Clinica", "Oftalmologia", "Cardiologia", "Oncologia"]
id_contador_doctores = 0
for i in range(4):
    id_contador_doctores += 1
    fila_doctores = [id_contador_doctores, matricula_doctor[i], nombre_doctor[i], apellido_doctor[i], telefono_doctor[i], especialidad_doctor[i]]
    matriz_doctores.append(fila_doctores)
for fila in matriz_doctores:
    print(fila)

print("\n MATRIZ DISPONIBILIDAD \n")
matriz_disponibilidad = []
matriz_disponibilidad.append(encabezados_disponibilidad)
 
dia_disponibilidad = ["23/03/2026", "23/03/2026", "24/03/2026", "25/03/2026"]
hora_inicio = ["6 AM", "8 AM", "8 AM", "10 AM"]
hora_fin = ["6 PM", "6 PM", "4 PM", "8 PM"]
matricula_doctor = ["12345", "67890", "54321", "09876"]

id_contador_disponibilidad = 1
for i in range (len(dia_disponibilidad)):
    fila = [id_contador_disponibilidad, matricula_doctor[i], dia_disponibilidad[i], hora_inicio[i], hora_fin[i]]
    matriz_disponibilidad.append(fila)
    id_contador_disponibilidad += 1

for fila in matriz_disponibilidad:
     print(fila)

print("\n MATRIZ TURNOS \n")
matriz_turnos = []
matriz_turnos.append(encabezados_turnos)
fecha_turno = ["3/4/2026", "3/4/2026", "5/4/2026", "7/4/2026"]
hora_turno = ["10 AM", "11 AM", "9 AM", "1 PM"]
id_contador_turnos = 0
for i in range(4):
    id_contador_turnos += 1
    fila_turnos = [id_contador_turnos, fecha_turno[i], hora_turno[i], dni_paciente[i], especialidad_doctor[i], matricula_doctor[i]]
    matriz_turnos.append(fila_turnos)
for fila in matriz_turnos:
    print(fila)

#----------------------------------------------------------------------------------------------------------------------------
# Bloque de menú
#----------------------------------------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 4 
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] ABM Pacientes.")
            print("[2] ABM Doctores.")
            print("[3] ABM Disponibilidad de Doctores.")
            print("[4] ABM Turnos Médicos.")
            print("[5] Ordenar Matrices.")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit()
            
        elif opcion == "1": #OPCIÓN 1
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE PACIENTES")
                    print("---------------------------")
                    print("[1] Agregar Paciente.")
                    print("[2] Eliminar Paciente.")
                    print("[3] Modificar Paciente.")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                                    
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0": # Salir del submenú
                    break # No sale del programa, vuelve al menú anterior
                    
                elif opcion == "1": # Opción 1
                    agregar_paciente(matriz_pacientes, id_contador_pacientes)
                    id_contador_pacientes += 1
                    mostrar_matriz(matriz_pacientes)
                    
                elif opcion == "2": #Opción 2
                    eliminar_paciente(matriz_pacientes)
                    mostrar_matriz(matriz_pacientes)
                    
                elif opcion == "3": #Opción 3
                    modificar_paciente(matriz_pacientes)
                    mostrar_matriz(matriz_pacientes)
                    
        elif opcion == "2": #OPCIÓN 2
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE DOCTORES")
                    print("---------------------------")
                    print("[1] Agregar Doctor.")
                    print("[2] Eliminar Doctor.")
                    print("[3] Modificar Doctor.")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                                    
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                
                if opcion == "0": # Salir del submenú
                    break # No sale del programa, vuelve al menú anterior

                elif opcion == "1":
                    agregar_doctor(matriz_doctores, id_contador_doctores)
                    id_contador_doctores += 1
                    mostrar_matriz(matriz_doctores)
            
                elif opcion == "2":
                    eliminar_doctor(matriz_doctores)
                    mostrar_matriz(matriz_doctores)
                    break
                elif opcion == "3":
                    modificar_doctor(matriz_doctores)
                    mostrar_matriz(matriz_doctores)

        elif opcion == "3": # OPCIÓN 3
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE DISPONIBILIDAD DE DOCTORES")
                    print("---------------------------")
                    print("[1] Agregar Disponibilidad.")
                    print("[2] Eliminar Disponibilidad.")
                    print("[3] Modificar Disponibilidad.")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                                                
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
        
                if opcion == "0": # Salir del submenú
                    break
        
                elif opcion == "1":
                    agregar_disponibilidad(matriz_disponibilidad, id_contador_disponibilidad)
                    id_contador_disponibilidad += 1
                    mostrar_matriz(matriz_disponibilidad)

                elif opcion == "2":
                    eliminar_disponibilidad(matriz_disponibilidad)
                    mostrar_matriz(matriz_disponibilidad)
                    break

                elif opcion == "3":
                    modificar_disponibilidad(matriz_disponibilidad)
                    mostrar_matriz(matriz_disponibilidad)

        
        elif opcion == "4": #OPCIÓN 4
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE TURNOS MÉDICOS")
                    print("---------------------------")
                    print("[1] Agregar Turno.")
                    print("[2] Eliminar Turno.")
                    print("[3] Modificar Turno.")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0": # Opción salir del submenú
                    break # No salimos del programa, volvemos al menú anterior
                
                elif opcion == "1":
                    agregar_turno(matriz_turnos, matriz_pacientes, matriz_doctores, id_contador_turnos)
                    mostrar_matriz(matriz_turnos)
                    
                elif opcion == "2":
                    eliminar_turno(matriz_turnos)
                    mostrar_matriz(matriz_turnos)

                elif opcion == "3":
                    modificar_turno(matriz_turnos, matriz_doctores)
                    mostrar_matriz(matriz_turnos)

        elif opcion == "5":
            matriz_ordenada = ordenar_matriz(matriz_pacientes)
            for fila in matriz_ordenada:
                print(fila)
