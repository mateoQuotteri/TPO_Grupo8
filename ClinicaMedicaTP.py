#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

import json
import os
import datetime
import pacientes
import doctores
import disponibilidad
import turnos
import usuarios

#----------------------------------------------------------------------------------------------
# FUNCIONES JSON
#----------------------------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def cargar_json(nombre_archivo):
    ruta = os.path.join(BASE_DIR, nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_json(nombre_archivo, datos):
    ruta = os.path.join(BASE_DIR, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

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

# Permite al usuario elegir una clave de un dict y ordena la lista de forma ascendente usando una función lambda.
def ordenar_lista_dicts(lista, claves, encabezado):
    print("Ingrese la opción por la cual ordenar: ")
    for i in range(len(encabezado)):
        print(i + 1, "-", encabezado[i])

    continuar = False
    columna_a_ordenar = 0
    while continuar == False:
        opcion = int(input("Ingrese la opcion: "))
        if 1 <= opcion <= len(claves):
            columna_a_ordenar = opcion - 1
            continuar = True
        else:
            print("Opcion inválida.")

    lista.sort(key=lambda fila: str(fila[claves[columna_a_ordenar]]))
    return lista

def pedir_especialidad():
    return input("Ingrese especialidad: ").strip().upper()

def filtrar_por_especialidad(lista_doctores, especialidad):
    return list(filter(lambda doc: especialidad in doc["especialidad"], lista_doctores))

def mostrar_reporte(encabezados, datos):
    print("\n--- REPORTE ---\n")
    ancho = 18
    for col in encabezados:
        print(f"{str(col):<{ancho}}", end="")
    print()
    print("-" * (ancho * len(encabezados)))
    for item in datos:
        for valor in item.values():
            print(f"{str(valor):<{ancho}}", end="")
        print()

# Recorre y muestra en consola cualquier lista de dicts con un formato de columnas alineadas.
def mostrar_lista(lista):
    print('-' * 115)
    for item in lista:
        for valor in item.values():
            print(f'{str(valor):^15}', end="\t")
        print()

# Muestra la lista de diccionarios de pacientes con un formato tabular específico, accediendo a cada campo por su clave.
def mostrar_pacientes(lista_pacientes):
    print('-' * 115)
    for p in lista_pacientes:
        print(f"{p['id']:^15}\t{p['dni']:^15}\t{p['nombre']:^15}\t{p['apellido']:^15}\t{p['telefono']:^15}\t{p['correo']:^15}")

# Punto central del programa que gestiona la navegación entre los submenús.
def menu_principal(rol, matricula_sesion, lista_pacientes, lista_doctores, lista_disponibilidad, lista_turnos,
                   encabezados_pacientes, encabezados_doctores, encabezados_disponibilidad, encabezados_turnos,
                   claves_doctores, claves_disponibilidad, claves_turnos,
                   id_contador_pacientes, id_contador_doctores, id_contador_disponibilidad, id_contador_turnos,
                   usuarios_data):
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
                print("[5] Ordenar.")
                print("[6] Reportes.")
                print("[7] Usuarios.")
                opciones_validas = [str(i) for i in range(0, 8)]  # 0 al 7

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
                mostrar_lista(lista_disponibilidad)
            elif opcion == "4":
                print(f"\nTURNOS DE LA MATRÍCULA: {matricula_sesion}")
                print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                encontrado = False
                for t in lista_turnos:
                    if str(t["matricula"]) == str(matricula_sesion):
                        for valor in t.values():
                            print(f'{str(valor):^15}', end="\t")
                        print()
                        encontrado = True
                if not encontrado:
                    print("No posee turnos asignados.")
            continue  # El medico no puede entrar a los submenus de edicion

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

                if opcion == "0":  # Salir del submenú
                    break  # No sale del programa, vuelve al menú anterior
                elif opcion == "1":  # Opción 1
                    pacientes.agregar_paciente(lista_pacientes, id_contador_pacientes)
                    id_contador_pacientes += 1
                    guardar_json("pacientes.json", lista_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_pacientes(lista_pacientes)
                elif opcion == "2":  # Opción 2
                    pacientes.eliminar_paciente(lista_pacientes)
                    guardar_json("pacientes.json", lista_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_pacientes(lista_pacientes)
                elif opcion == "3":  # Opción 3
                    pacientes.modificar_paciente(lista_pacientes)
                    guardar_json("pacientes.json", lista_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_pacientes(lista_pacientes)

        elif opcion == "2":  # OPCIÓN 2
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

                if opcion == "0":  # Salir del submenú
                    break  # No sale del programa, vuelve al menú anterior
                elif opcion == "1":
                    id_contador_doctores = doctores.agregar_doctor(lista_doctores, id_contador_doctores)
                    guardar_json("doctores.json", lista_doctores)
                    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
                    mostrar_lista(lista_doctores)
                elif opcion == "2":
                    doctores.eliminar_doctor(lista_doctores)
                    guardar_json("doctores.json", lista_doctores)
                    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
                    mostrar_lista(lista_doctores)
                    break
                elif opcion == "3":
                    doctores.modificar_doctor(lista_doctores)
                    guardar_json("doctores.json", lista_doctores)
                    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
                    mostrar_lista(lista_doctores)

        elif opcion == "3":  # OPCIÓN 3
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

                if opcion == "0":  # Salir del submenú
                    break
                elif opcion == "1":
                    disponibilidad.agregar_disponibilidad(lista_disponibilidad, id_contador_disponibilidad)
                    id_contador_disponibilidad += 1
                    guardar_json("disponibilidad.json", lista_disponibilidad)
                    print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
                    mostrar_lista(lista_disponibilidad)
                elif opcion == "2":
                    disponibilidad.eliminar_disponibilidad(lista_disponibilidad)
                    guardar_json("disponibilidad.json", lista_disponibilidad)
                    print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
                    mostrar_lista(lista_disponibilidad)
                    break
                elif opcion == "3":
                    disponibilidad.modificar_disponibilidad(lista_disponibilidad)
                    guardar_json("disponibilidad.json", lista_disponibilidad)
                    print(f'{encabezados_disponibilidad[0]:^5}\t{encabezados_disponibilidad[1]:^5}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
                    mostrar_lista(lista_disponibilidad)

        elif opcion == "4":  # OPCIÓN 4
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
                    if opcion in [str(i) for i in range(0, opciones + 1)]:  # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0":  # Opción salir del submenú
                    break  # No salimos del programa, volvemos al menú anterior
                elif opcion == "1":
                    turnos.agregar_turno(lista_turnos, lista_pacientes, lista_doctores, id_contador_turnos, lista_disponibilidad)
                    guardar_json("turnos.json", lista_turnos)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_lista(lista_turnos)
                elif opcion == "2":
                    turnos.eliminar_turno(lista_pacientes, lista_turnos)
                    guardar_json("turnos.json", lista_turnos)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_lista(lista_turnos)
                elif opcion == "3":
                    turnos.modificar_turno(lista_turnos, lista_doctores, lista_pacientes, lista_disponibilidad)
                    guardar_json("turnos.json", lista_turnos)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_lista(lista_turnos)

        elif opcion == "5":
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > ORDENAMIENTO")
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

                if opcion == "0":  # Salir del submenú
                    break
                elif opcion == "1":
                    lista_ordenada = ordenar_pacientes_dic(lista_pacientes, encabezados_pacientes)
                    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
                    mostrar_pacientes(lista_ordenada)
                    break
                elif opcion == "2":
                    lista_ordenada = ordenar_lista_dicts(lista_doctores, claves_doctores, encabezados_doctores)
                    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
                    mostrar_lista(lista_ordenada)
                    break
                elif opcion == "3":
                    lista_ordenada = ordenar_lista_dicts(lista_disponibilidad, claves_disponibilidad, encabezados_disponibilidad)
                    print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
                    mostrar_lista(lista_ordenada)
                    break
                elif opcion == "4":
                    lista_ordenada = ordenar_lista_dicts(lista_turnos, claves_turnos, encabezados_turnos)
                    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
                    mostrar_lista(lista_ordenada)
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

                if opcion == "0":  # Salir del submenú
                    break
                elif opcion == "1":
                    esp = pedir_especialidad()
                    datos = filtrar_por_especialidad(lista_doctores, esp)
                    mostrar_reporte(encabezados_doctores, datos)
                elif opcion == "2":
                    doctores.reporte_cobertura_medica(lista_doctores, lista_disponibilidad)
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

                if opcion == "0":  # Salir del submenú
                    break
                elif opcion == "1":
                    usuarios.agregar_usuario(usuarios_data)
                    guardar_json("usuarios.json", usuarios_data)
                elif opcion == "2":
                    usuarios.eliminar_usuario(usuarios_data)
                    guardar_json("usuarios.json", usuarios_data)

    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

# Función principal que carga los datos desde JSON, muestra las listas y lanza la ejecución del programa.
def main():
    encabezados_pacientes      = ['ID Paciente', 'DNI', 'Nombre', 'Apellido', 'Telefono', 'Correo']
    encabezados_doctores       = ['ID Profesional', 'Matricula', 'Nombre', 'Apellido', 'Telefono', 'Especialidad', 'Activo/Inactivo']
    encabezados_disponibilidad = ['ID Dispo.', 'Matricula', 'Día', 'Hora Inicio', 'Hora Fin']
    encabezados_turnos         = ['ID Turno', 'Fecha', 'Hora', 'DNI Paciente', 'Especialidad', 'Matricula Doctor']

    claves_doctores       = ["id", "matricula", "nombre", "apellido", "telefono", "especialidad", "activo"]
    claves_disponibilidad = ["id", "matricula", "dia", "hora_inicio", "hora_fin"]
    claves_turnos         = ["id", "fecha", "hora", "dni", "especialidad", "matricula"]

    # Carga de datos desde archivos JSON
    lista_pacientes      = cargar_json("pacientes.json")
    lista_doctores       = cargar_json("doctores.json")
    lista_disponibilidad = cargar_json("disponibilidad.json")
    lista_turnos         = cargar_json("turnos.json")
    usuarios_data        = cargar_json("usuarios.json")

    # Contadores inicializados a partir de los datos cargados
    id_contador_pacientes      = max((p["id"] for p in lista_pacientes),      default=0)
    id_contador_doctores       = max((d["id"] for d in lista_doctores),       default=0)
    id_contador_disponibilidad = max((d["id"] for d in lista_disponibilidad), default=0) + 1
    id_contador_turnos         = max((t["id"] for t in lista_turnos),         default=0)

    print("\n LISTA DE PACIENTES \n")
    print(f'{encabezados_pacientes[0]:^15}{encabezados_pacientes[1]:^15}{encabezados_pacientes[2]:^15}{encabezados_pacientes[3]:^15}{encabezados_pacientes[4]:^15}{encabezados_pacientes[5]:^15}')
    mostrar_pacientes(lista_pacientes)

    print("\n LISTA DE DOCTORES \n")
    print(f'{encabezados_doctores[0]:^15}\t{encabezados_doctores[1]:^15}\t{encabezados_doctores[2]:^15}\t{encabezados_doctores[3]:^15}\t{encabezados_doctores[4]:^15}\t{encabezados_doctores[5]:^15}\t{encabezados_doctores[6]:^15}')
    mostrar_lista(lista_doctores)

    print("\n LISTA DE DISPONIBILIDAD \n")
    print(f'{encabezados_disponibilidad[0]:^15}\t{encabezados_disponibilidad[1]:^15}\t{encabezados_disponibilidad[2]:^15}\t{encabezados_disponibilidad[3]:^15}\t{encabezados_disponibilidad[4]:^15}')
    mostrar_lista(lista_disponibilidad)

    print("\n LISTA DE TURNOS \n")
    print(f'{encabezados_turnos[0]:^15}\t{encabezados_turnos[1]:^15}\t{encabezados_turnos[2]:^15}\t{encabezados_turnos[3]:^15}\t{encabezados_turnos[4]:^15}\t{encabezados_turnos[5]:^15}')
    mostrar_lista(lista_turnos)

    # --- LOGIN ---
    print("\n" + "=" * 35)
    print("  INICIO DE SESIÓN - CLÍNICA")
    print("=" * 35)

    usuario_ingresado = input("Usuario: ").lower()
    clave_ingresada = input("Contraseña: ")

    if usuario_ingresado in usuarios_data:
        # Accedemos al dict del usuario por sus claves
        datos_usuario   = usuarios_data[usuario_ingresado]
        clave_correcta  = datos_usuario["clave"]
        nombre_completo = datos_usuario["nombre"]
        rol             = datos_usuario["rol"]

        if clave_ingresada == clave_correcta:
            matricula_sesion = None

            if rol == "DOCTOR":
                print("\n--- VALIDACIÓN DE IDENTIDAD MÉDICA ---")
                matricula_sesion = input("Por favor, ingrese su número de matrícula: ")

                nombre_bienvenida = nombre_completo
                for doc in lista_doctores:
                    if str(doc["matricula"]) == str(matricula_sesion):
                        nombre_bienvenida = f"{doc['nombre']} {doc['apellido']}"
                        break
                print(f"\nBienvenido/a Dr/a. {nombre_bienvenida}")
            else:
                print(f"\nBienvenido/a {nombre_completo}")

            menu_principal(
                rol, matricula_sesion,
                lista_pacientes, lista_doctores, lista_disponibilidad, lista_turnos,
                encabezados_pacientes, encabezados_doctores, encabezados_disponibilidad, encabezados_turnos,
                claves_doctores, claves_disponibilidad, claves_turnos,
                id_contador_pacientes, id_contador_doctores, id_contador_disponibilidad, id_contador_turnos,
                usuarios_data
            )
        else:
            print("\nError: Contraseña incorrecta.")
    else:
        print("\nError: El usuario no existe.")

main()

