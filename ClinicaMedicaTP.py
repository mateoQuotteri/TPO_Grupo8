#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

import datetime
import pacientes
import doctores
import disponibilidad
import turnos
import usuarios

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# Permite al usuario elegir una columna de una matriz y la ordena de forma ascendente usando una función lambda.
def ordenar_matriz(matriz,encabezado):
    opciones = encabezado
    print("Ingrese la opción por la cual ordenar la matriz: ")
    for i in range(len(opciones)):
        print(i + 1, "-", opciones[i])
    
    continuar = False
    columna_a_ordenar = 0
    while continuar == False:
        opcion = int(input("Ingrese la opcion: "))
        if 1 <= opcion <= len(opciones):
            columna_a_ordenar = opcion - 1
            continuar = True
        else:
            print("Opcion inválida.")
            
    matriz.sort(key=lambda fila: fila[columna_a_ordenar])
    return matriz

# Ordena la lista de diccionarios de pacientes según la clave elegida (ID, DNI, Nombre, etc.) por el usuario.
def ordenar_pacientes_dic(lista, encabezado):
    claves = ["id", "dni", "nombre", "apellido", "telefono", "correo"]
    
    print("Ingrese la opción por la cual ordenar los pacientes: ")
    for i in range(len(encabezado)):
        print(f"{i + 1} - {encabezado[i]}")
    
    # Bandera para no utilizar break
    opcion_valida = False
    clave_elegida = ""
    
    while opcion_valida == False:
        opcion = int(input("Seleccione una opción: "))
        
        if 1 <= opcion <= len(claves):
            clave_elegida = claves[opcion - 1]
            opcion_valida = True
        else:
            print("Opción inválida. Intente nuevamente.")

    lista.sort(key=lambda p: p[clave_elegida])
    return lista

def pedir_especialidad():
    return input("Ingrese especialidad: ").strip().upper()

def filtrar_por_especialidad(matriz, encabezados, especialidad):
    i = encabezados.index("Especialidad")

    datos = list(filter(lambda fila: especialidad in fila[i],matriz))

    return datos

def mostrar_reporte(encabezados, datos):
    print("\n--- REPORTE ---\n")
    ancho = 18
    for col in encabezados:
        print(f"{str(col):<{ancho}}", end="")
    print()
    print("-" * (ancho * len(encabezados)))
    for fila in datos:
        for valor in fila:
            print(f"{str(valor):<{ancho}}", end="")
        print()

# Recorre y muestra en consola cualquier matriz de datos con un formato de columnas alineadas.
def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    print('-'*115)
    for fila in range(filas):
        for columna in range(columnas):
            print(f'{matriz[fila][columna]:^15}',end="\t")
        print()

# Muestra la lista de diccionarios de pacientes con un formato tabular específico, accediendo a cada campo por su clave.
def mostrar_pacientes(lista_pacientes):
        print('-'*115)
        for p in lista_pacientes:
            print(f"{p['id']:^15}\t{p['dni']:^15}\t{p['nombre']:^15}\t{p['apellido']:^15}\t{p['telefono']:^15}\t{p['correo']:^15}")

# Punto central del programa que gestiona la navegación entre los submenús de Pacientes, Doctores, Disponibilidad, Turnos, Roles de Usuarios, Matricula del Medico y Ordenamiento.
def menu_principal(rol, matricula_sesion, lista_pacientes, matriz_doctores, matriz_disponibilidad, matriz_turnos, encabezados_pacientes, encabezados_doctores, encabezados_disponibilidad, encabezados_turnos, id_contador_pacientes, id_contador_doctores, id_contador_disponibilidad, id_contador_turnos):
    while True:
        while True:
            print()
            print("---------------------------")
            print(f"MENÚ PRINCIPAL - ROL: {rol}")
            print("---------------------------")
            
            # Opciones a mostrar y cuales son validas segun el ROL
            if rol == "ADMINISTRATIVO":
                print("[1] ABM Pacientes.")
                print("[2] ABM Doctores.")
                print("[3] ABM Disponibilidad de Doctores.")
                print("[4] ABM Turnos Médicos.")
                print("[5] Ordenar Matrices.")
                print("[6] Reportes.")
                print("[7] Usuarios.")
                opciones_validas = [str(i) for i in range(0, 8)] # 0 al 6
            
            elif rol == "RECEPCIONISTA":
                print("[1] ABM Pacientes.")
                print("[4] ABM Turnos Médicos.")
                opciones_validas = ["0", "1", "4"]
            
            elif rol == "DOCTOR":
                print("[3] Ver Disponibilidad de Doctores.")
                print("[4] Ver mis Turnos Ocupados.")
                opciones_validas = ["0", "3", "4"]

            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcion = input("Seleccione una opción: ").strip()
            
            # Se valida que el usuario tenga permiso para esa opcion
            if opcion in opciones_validas:
                break
            else:
                input("Opción inválida o no permitida para su rol. Presione ENTER.")
        print()

        if opcion == "0": 
            exit()
            
        # MEDICO (Solo lectura y filtrado)
        if rol == "DOCTOR":
            if opcion == "3":
                print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
                mostrar_matriz(matriz_disponibilidad)
            elif opcion == "4":
                print(f"\nTURNOS DE LA MATRÍCULA: {matricula_sesion}")
                print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                encontrado = False
                for fila in matriz_turnos:
                    # Filtra la Matricula Doctor
                    if str(fila[5]) == str(matricula_sesion):
                        for valor in fila:
                            print(f'{str(valor):^15}', end="\t")
                        print()
                        encontrado = True
                if not encontrado:
                    print("No posee turnos asignados.")
            continue # El medico no puede entrar a los submenus de edicion

        # ADMINISTRATIVO Y RECEPCIONISTA (Menu original)
        if opcion == "1":
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
                    pacientes.agregar_paciente(lista_pacientes, id_contador_pacientes)
                    id_contador_pacientes += 1
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_pacientes(lista_pacientes)
                    
                elif opcion == "2": #Opción 2
                    pacientes.eliminar_paciente(lista_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_pacientes(lista_pacientes)
                    
                elif opcion == "3": #Opción 3
                    pacientes.modificar_paciente(lista_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_pacientes(lista_pacientes)
                    
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
                    print(f'{encabezados_disponibilidad[0]:^5}\t{encabezados_disponibilidad[1]:^5}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
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
                    turnos.agregar_turno(matriz_turnos, lista_pacientes, matriz_doctores, id_contador_turnos,matriz_disponibilidad)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_matriz(matriz_turnos)
                    
                elif opcion == "2":
                    turnos.eliminar_turno(lista_pacientes, matriz_turnos)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_matriz(matriz_turnos)

                elif opcion == "3":
                    turnos.modificar_turno(matriz_turnos, matriz_doctores, lista_pacientes, matriz_disponibilidad)
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
                    lista_ordenada = ordenar_pacientes_dic(lista_pacientes, encabezados_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_pacientes(lista_ordenada)
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

        elif opcion == "6":

            while True:
                while True:
                    opciones = 2
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE REPORTES MÉDICOS")
                    print("---------------------------")
                    print("[1] Reporte de Especialidades.")
                    print("---------------------------")
                    print("[2] Reporte de Disponibilidad horaria de Doctores.")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, 3)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0": # Salir del submenú
                    break

                elif opcion == "1":
                    esp = pedir_especialidad()
                    datos = filtrar_por_especialidad(matriz_doctores, encabezados_doctores, esp)
                    mostrar_reporte(encabezados_doctores, datos)

                elif opcion == "2":
                    doctores.reporte_cobertura_medica(matriz_doctores, matriz_disponibilidad)
                    input("\nPresione ENTER para continuar...")
       
        elif opcion == "7":
            
            while True:
                while True:
                    opciones = 2
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > USUARIOS")
                    print("---------------------------")
                    print("[1] Agregar usuario.")
                    print("[2] Eliminar usuario.")
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
                    usuarios.agregar_usuario(usuarios.usuarios)
                
                elif opcion == "2":
                    usuarios.eliminar_usuario(usuarios.usuarios)

    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Función principal que inicializa los datos de ejemplo, configura los encabezados y lanza la ejecución del programa.
def main():
    encabezados_usuarios = ['Contraseña', 'Nombre de Usuario', 'Rol']
    encabezados_pacientes = ['ID Paciente', 'DNI', 'Nombre', 'Apellido', 'Telefono', 'Correo']
    encabezados_doctores = ['ID Profesional', 'Matricula', 'Nombre', 'Apellido', 'Telefono', 'Especialidad', 'Activo/Inactivo']
    encabezados_disponibilidad = ['ID Dispo.', 'Matricula', 'Día', 'Hora Inicio', 'Hora Fin']
    encabezados_turnos = ['ID Turno', 'Fecha', 'Hora', 'DNI Paciente', 'Especialidad', 'Matricula Doctor']



    print("\n LISTA DE DICCIONARIOS: PACIENTES \n")
    
    lista_pacientes = []
    dni_paciente = ["26486592","35874126","41256987","28974135","33659874","40123789","27894561","38965412","34561278","29876543",
                    "36781245","42315678","31245789","27654389","39871256","42135698","30547891","28765412","36412578","40987612"]
    nombre_paciente = ["Miguel","Laura","Carlos","Ana","Diego","Sofia","Javier","Lucia","Martin","Valentina","Andres",
                       "Camila","Fernando","Paula","Ricardo","Marina","Gabriel","Florencia","Nicolas","Julieta"]
    apellido_paciente = ["Martinez","Gomez","Lopez","Fernandez","Perez","Ramirez","Torres","Flores","Diaz","Castro",
                         "Rojas","Silva","Ortiz","Morales","Suarez","Vega","Herrera","Mendez","Cabrera","Reyes"]
    telefono_paciente = ["1146329878","1189456721","1178345620","1167234598","1156123479","1145012367","1134901256",
                         "1123890145","1112789034","1191678923","1180567812","1169456701","1158345690","1147234589",
                         "1136123478","1125012367","1114901256","1193890145","1182789034","1171678923"]
    correo_paciente = ["mmartinez24@gmail.com","lauragomez@gmail.com","carloslopez@gmail.com","anafernandez@gmail.com",
                       "diegoperez@gmail.com","sofiaramirez@gmail.com","javiertorres@gmail.com","luciaflores@gmail.com",
                       "martindiaz@gmail.com","valentinacastro@gmail.com","andresrojas@gmail.com","camilasilva@gmail.com",
                       "fernandoortiz@gmail.com","paulamorales@gmail.com","ricardosuarez@gmail.com","marinavega@gmail.com",
                       "gabrielherrera@gmail.com","florenciamendez@gmail.com","nicolascabrera@gmail.com","julietareyes@gmail.com"]
    id_contador_pacientes = 0
    for i in range(len(dni_paciente)):
        id_contador_pacientes += 1

        paciente = {
            "id": id_contador_pacientes,
            "dni": dni_paciente[i],
            "nombre": nombre_paciente[i],
            "apellido": apellido_paciente[i],
            "telefono": telefono_paciente[i],
            "correo": correo_paciente[i]
        }
        lista_pacientes.append(paciente)

    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
    mostrar_pacientes(lista_pacientes)


    print("\n MATRIZ DOCTORES \n")
    matriz_doctores = []
    matricula_doctor = ["58321","67234","74512","83456","91234","67891","54321","45678","78901","89012","90123","81234",
                        "72345","63456","54567","45679","36789","27890","18901","29012"]

    nombre_doctor = ["Laura","Carlos","Ana","Diego","Sofia","Javier","Lucia","Martin","Valentina","Andres",
                     "Camila","Fernando","Paula","Ricardo","Marina","Gabriel","Florencia","Nicolas","Julieta","Bruno"]


    apellido_doctor = ["Gomez","Lopez","Fernandez","Perez","Ramirez","Torres","Flores","Diaz","Castro","Rojas",
                       "Silva","Ortiz","Morales","Suarez","Vega","Herrera","Mendez","Cabrera","Reyes","Acosta"]

    telefono_doctor = ["1145678901","1156789012","1167890123","1178901234","1189012345","1190123456","1111234567",
                       "1122345678","1133456789","1144567890","1155678901","1166789012","1177890123","1188901234",
                       "1199012345","1110123456","1121234567","1132345678","1143456789","1154567890"]


    especialidad_doctor = ["CLÍNICA MÉDICA","PEDIATRÍA","GINECOLOGÍA","CARDIOLOGÍA","OFTALMOLOGÍA","ODONTOLOGÍA",
                           "DERMATOLOGÍA","TRAUMATOLOGÍA","CLÍNICA MÉDICA","PEDIATRÍA","GINECOLOGÍA","CARDIOLOGÍA",
                           "OFTALMOLOGÍA","ODONTOLOGÍA","DERMATOLOGÍA","TRAUMATOLOGÍA","CLÍNICA MÉDICA","PEDIATRÍA","CARDIOLOGÍA","ODONTOLOGÍA"]

    
    # Usamos mayúsculas para que el formato de las especialidades sea uniforme, ya que al modificar un doctor se le pide al usuario que ingrese la especialidad en mayúscula, y así evitamos que haya especialidades repetidas por el mismo nombre pero con diferente formato (
    # USAMOS LAMBDA PARA ESTO
    especialidad_doctor = list(map(lambda e: e.upper(), especialidad_doctor))
    activo_inactivo = ["S","S","N","S","N","S","S","N","S","S","N","S","N","S","S","N","S","S","N","S"]

    id_contador_doctores = 0
    for i in range(len(matricula_doctor)):
        id_contador_doctores += 1
        fila_doctores = [id_contador_doctores, matricula_doctor[i], nombre_doctor[i], apellido_doctor[i], telefono_doctor[i], especialidad_doctor[i], activo_inactivo[i]]
        matriz_doctores.append(fila_doctores)
    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
    mostrar_matriz(matriz_doctores)

    print("\n MATRIZ DISPONIBILIDAD \n")
    matriz_disponibilidad = []
    dia_disponibilidad = ["LUNES","MIERCOLES","MARTES","JUEVES","LUNES","VIERNES","MIERCOLES","JUEVES",
                          "MARTES","VIERNES","LUNES","MIERCOLES","MARTES","JUEVES","LUNES","VIERNES",
                          "MIERCOLES","JUEVES","MARTES","VIERNES","LUNES","MIERCOLES","MARTES","JUEVES",
                          "LUNES","VIERNES","MARTES","MIERCOLES","JUEVES","VIERNES","LUNES","MIERCOLES",
                          "MARTES","JUEVES","MIERCOLES","VIERNES","LUNES","JUEVES","MARTES","VIERNES"]
    hora_inicio = ["8","13","9","10","8","12","9","14","10","8","13","8","9","13","8","14","10","8","9","13",
                   "8","14","10","9","11","8","13","9","8","13","9","14","8","12","9","10","8","13","9","14"]
    hora_fin = ["12","17","14","15","13","16","13","18","14","12","18","12","12","17","11","19","15","12","13",
                "18","12","18","16","13","15","12","18","13","14","17","12","18","13","16","14","15","12","17","13","18"]
    matricula_doctor =  ["58321","58321","67234","67234","74512","74512","83456","83456","91234","91234",
                         "67891","67891","54321","54321","45678","45678","78901","78901","89012","89012",
                         "90123","90123","81234","81234","72345","72345","63456","63456","54567","54567",
                         "45679","45679","36789","36789","27890","27890","18901","18901","29012","29012"]


    id_contador_disponibilidad = 1
    for i in range (len(dia_disponibilidad)):
        fila = [id_contador_disponibilidad, matricula_doctor[i], dia_disponibilidad[i], hora_inicio[i], hora_fin[i]]
        matriz_disponibilidad.append(fila)
        id_contador_disponibilidad += 1
    print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
    mostrar_matriz(matriz_disponibilidad)

    print("\n MATRIZ TURNOS \n")
    matriz_turnos = []
    fecha_turno = ["27/04/2026","28/04/2026","29/04/2026","30/04/2026","02/05/2026",
                   "04/05/2026","05/05/2026","06/05/2026","27/04/2026","28/04/2026",
                   "29/04/2026","30/04/2026","02/05/2026","04/05/2026","05/05/2026",
                   "06/05/2026","27/04/2026","28/04/2026","29/04/2026","30/04/2026"
]
    hora_turno = ["9","11","10","15","9","14","10","16","11","12","15","11","12","15","9","15","10","14","11","16"]

    dni_turno = ["26486592","35874126","41256987","28974135","33659874","40123789","27894561","38965412","34561278",
                  "29876543","36781245","42315678","31245789","27654389","39871256","42135698","30547891","28765412","36412578","40987612"]

    especialidad_turno = ["CLÍNICA MÉDICA","PEDIATRÍA","GINECOLOGÍA","CARDIOLOGÍA","OFTALMOLOGÍA","ODONTOLOGÍA",
                          "DERMATOLOGÍA","TRAUMATOLOGÍA","CLÍNICA MÉDICA","PEDIATRÍA","GINECOLOGÍA","CARDIOLOGÍA",
                          "OFTALMOLOGÍA","ODONTOLOGÍA","DERMATOLOGÍA","TRAUMATOLOGÍA","CLÍNICA MÉDICA","PEDIATRÍA","CARDIOLOGÍA","ODONTOLOGÍA"]
    matricula_turno = ["58321","67234","74512","83456","91234","67891","54321","45678","78901","89012","90123",
                       "81234","72345","63456","54567","45679","36789","27890","18901","29012"]

    id_contador_turnos = 0
    for i in range(len(fecha_turno)):
        id_contador_turnos += 1
        fila_turnos = [id_contador_turnos, fecha_turno[i], hora_turno[i], dni_turno[i], especialidad_turno[i], matricula_turno[i]]
        matriz_turnos.append(fila_turnos)
    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
    mostrar_matriz(matriz_turnos)

    # --- LOGIN ---
    print("\n" + "="*35)
    print("  INICIO DE SESIÓN - CLÍNICA")
    print("="*35)
    
    usuario_ingresado = input("Usuario: ").lower()
    clave_ingresada = input("Contraseña: ")

    if usuario_ingresado in usuarios.usuarios:
        #Desempaquetamos la tupla del usuario para obtener la clave, nombre completo y rol
        clave_correcta, nombre_completo, rol = usuarios.usuarios[usuario_ingresado]

        if clave_ingresada == clave_correcta:
            matricula_sesion = None
            
            if rol == "DOCTOR":
                print("\n--- VALIDACIÓN DE IDENTIDAD MÉDICA ---")
                matricula_sesion = input("Por favor, ingrese su número de matrícula: ")
                
                nombre_bienvenida = nombre_completo
                encontrado = False
                i = 0
                
                while i < len(matriz_doctores) and not encontrado:
                    doc = matriz_doctores[i]
                    if str(doc[1]) == str(matricula_sesion):
                        nombre_bienvenida = f"{doc[2]} {doc[3]}"
                        encontrado = True
                    i += 1
                print(f"\nBienvenido/a Dr/a. {nombre_bienvenida}")
            else:
                print(f"\nBienvenido/a {nombre_completo}")
            
            menu_principal(rol, matricula_sesion, lista_pacientes, matriz_doctores, matriz_disponibilidad, matriz_turnos, encabezados_pacientes, encabezados_doctores, encabezados_disponibilidad, encabezados_turnos, id_contador_pacientes, id_contador_doctores, id_contador_disponibilidad, id_contador_turnos)
        else:
            print("\nError: Contraseña incorrecta.")
    else:
        print("\nError: El usuario no existe.")
main()