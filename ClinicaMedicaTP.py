#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

import random
import pacientes
import doctores
import disponibilidad
import turnos

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


#FUNCIONES DE DISPONIBILIDAD



# FUNCIONES DE TURNOS


def ordenar_matriz(matriz,encabezado):
    opciones = encabezado
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
    matriz.sort(key=lambda fila: fila[columna_a_ordenar])
    return matriz

def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(filas):
        for columna in range(columnas):
            print(f'{matriz[fila][columna]:^15}',end="\t")
        print()

def menu_principal(matriz_pacientes,matriz_doctores,matriz_disponibilidad,matriz_turnos,encabezados_pacientes,encabezados_doctores,encabezados_disponibilidad,encabezados_turnos,id_contador_pacientes, id_contador_doctores,id_contador_disponibilidad,id_contador_turnos):
    while True:
        while True:
            opciones = 5 
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
                    pacientes.agregar_paciente(matriz_pacientes, id_contador_pacientes)
                    id_contador_pacientes += 1
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_matriz(matriz_pacientes)
                    
                elif opcion == "2": #Opción 2
                    pacientes.eliminar_paciente(matriz_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_matriz(matriz_pacientes)
                    
                elif opcion == "3": #Opción 3
                    pacientes.modificar_paciente(matriz_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
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
                    doctores.agregar_doctor(matriz_doctores, id_contador_doctores)
                    id_contador_doctores += 1
                    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
                    mostrar_matriz(matriz_doctores)
            
                elif opcion == "2":
                    doctores.eliminar_doctor(matriz_doctores)
                    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
                    mostrar_matriz(matriz_doctores)
                    break
                elif opcion == "3":
                    doctores.modificar_doctor(matriz_doctores)
                    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
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
                    disponibilidad.agregar_disponibilidad(matriz_disponibilidad, id_contador_disponibilidad)
                    id_contador_disponibilidad += 1
                    print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
                    mostrar_matriz(matriz_disponibilidad)

                elif opcion == "2":
                    disponibilidad.eliminar_disponibilidad(matriz_disponibilidad)
                    print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
                    mostrar_matriz(matriz_disponibilidad)
                    break

                elif opcion == "3":
                    disponibilidad.modificar_disponibilidad(matriz_disponibilidad)
                    print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
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
                    turnos.agregar_turno(matriz_turnos, matriz_pacientes, matriz_doctores, id_contador_turnos)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_matriz(matriz_turnos)
                    
                elif opcion == "2":
                    turnos.eliminar_turno(matriz_turnos)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_matriz(matriz_turnos)

                elif opcion == "3":
                    turnos.modificar_turno(matriz_turnos, matriz_doctores)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_matriz(matriz_turnos)

        elif opcion == "5":
            
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > ORDENAMIENTO DE MATRICES")
                    print("---------------------------")
                    print("[1] Pacientes.")
                    print("[2] Médicos.")
                    print("[3] Disponibilidad.")
                    print("[4] Turnos.")
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
                    matriz_ordenada = ordenar_matriz(matriz_pacientes,encabezados_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_matriz(matriz_ordenada)
                    break

                elif opcion == "2":
                    matriz_ordenada = ordenar_matriz(matriz_doctores,encabezados_doctores)
                    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
                    mostrar_matriz(matriz_ordenada)
                    break

                elif opcion == "3":
                    matriz_ordenada = ordenar_matriz(matriz_disponibilidad,encabezados_disponibilidad)
                    print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
                    mostrar_matriz(matriz_ordenada)
                    break
                
                elif opcion == "4":
                    matriz_ordenada = ordenar_matriz(matriz_turnos,encabezados_turnos)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_matriz(matriz_ordenada)
                    break
    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

encabezados_pacientes = ['ID Paciente', 'DNI', 'Nombre', 'Apellido', 'Telefono', 'Correo']
encabezados_doctores = ['ID Profesional', 'Matricula', 'Nombre', 'Apellido', 'Telefono', 'Especialidad', 'Activo/Inactivo']
encabezados_disponibilidad = ['ID Disponibilidad', 'Matricula', 'Día', 'Hora Inicio', 'Hora Fin']
encabezados_turnos = ['ID Turno', 'Fecha', 'Hora', 'DNI Paciente', 'Especialidad', 'Matricula Doctor']

print("\n MATRIZ PACIENTES \n")
matriz_pacientes = []
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
print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^18}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^20}')
mostrar_matriz(matriz_pacientes)


print("\n MATRIZ DOCTORES \n")
matriz_doctores = []
matricula_doctor = ["12345", "67890", "54321", "09876",
                    "11223", "22334", "33445", "44556", "55667", "66778",
                    "77889", "88990", "99001", "10112", "12123",
                    "13134", "14145", "15156", "16167", "17178"]

nombre_doctor = ["Bruno", "Carmen", "Nadia", "Guada",
                 "Lucas", "Martina", "Juan", "Sofia", "Diego", "Valentina",
                 "Tomas", "Paula", "Agustin", "Florencia", "Mateo",
                 "Camila", "Franco", "Lara", "Nicolas", "Julieta"]

apellido_doctor = ["Gonzales", "Rivera", "Correa", "Smith",
                   "Perez", "Lopez", "Gomez", "Fernandez", "Martinez", "Rodriguez",
                   "Sanchez", "Ramirez", "Torres", "Acosta", "Benitez",
                   "Herrera", "Castro", "Ortiz", "Vega", "Morales"]

telefono_doctor = ["3478125690", "1256903478", "0965213478", "8743561290",
                   "3512345678", "3419876543", "3814567890", "2991234567", "2619876543", "3517654321",
                   "2234567890", "1167894321", "3794561230", "2611237894", "3519998888",
                   "2239871234", "2998887777", "2614445555", "3512223333", "1165554444"]

especialidad_doctor = ["Clinica", "Oftalmologia", "Cardiologia", "Oncologia",
                       "Pediatria", "Dermatologia", "Traumatologia", "Odontologia", "Cardiologia", "Ginecologia",
                       "Clinica", "Pediatria", "Oftalmologia", "Dermatologia", "Traumatologia",
                       "Odontologia", "Cardiologia", "Ginecologia", "Clinica", "Pediatria"]
# Usamos mayúsculas para que el formato de las especialidades sea uniforme, ya que al modificar un doctor se le pide al usuario que ingrese la especialidad en mayúscula, y así evitamos que haya especialidades repetidas por el mismo nombre pero con diferente formato (
# USAMOS LAMBDA PARA ESTO
especialidad_doctor = list(map(lambda e: e.upper(), especialidad_doctor))
activo_inactivo = ["S", "N", "S", "N"]
id_contador_doctores = 0
for i in range(4):
    id_contador_doctores += 1
    fila_doctores = [id_contador_doctores, matricula_doctor[i], nombre_doctor[i], apellido_doctor[i], telefono_doctor[i], especialidad_doctor[i], activo_inactivo[i]]
    matriz_doctores.append(fila_doctores)
print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
mostrar_matriz(matriz_doctores)

print("\n MATRIZ DISPONIBILIDAD \n")
matriz_disponibilidad = []
dia_disponibilidad = ["23/03/2026", "23/03/2026", "24/03/2026", "25/03/2026"]
hora_inicio = ["6 AM", "8 AM", "8 AM", "10 AM"]
hora_fin = ["6 PM", "6 PM", "4 PM", "8 PM"]
matricula_doctor = ["12345", "67890", "54321", "09876"]

id_contador_disponibilidad = 1
for i in range (len(dia_disponibilidad)):
    fila = [id_contador_disponibilidad, matricula_doctor[i], dia_disponibilidad[i], hora_inicio[i], hora_fin[i]]
    matriz_disponibilidad.append(fila)
    id_contador_disponibilidad += 1
print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
mostrar_matriz(matriz_disponibilidad)

print("\n MATRIZ TURNOS \n")
matriz_turnos = []
fecha_turno = ["3/4/2026", "3/4/2026", "5/4/2026", "7/4/2026"]
hora_turno = ["10 AM", "11 AM", "9 AM", "1 PM"]
id_contador_turnos = 0
for i in range(4):
    id_contador_turnos += 1
    fila_turnos = [id_contador_turnos, fecha_turno[i], hora_turno[i], dni_paciente[i], especialidad_doctor[i], matricula_doctor[i]]
    matriz_turnos.append(fila_turnos)
print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
mostrar_matriz(matriz_turnos)

menu_principal(matriz_pacientes,matriz_doctores,matriz_disponibilidad,matriz_turnos,encabezados_pacientes,encabezados_doctores,encabezados_disponibilidad,encabezados_turnos, id_contador_pacientes, id_contador_doctores,id_contador_disponibilidad,id_contador_turnos)
