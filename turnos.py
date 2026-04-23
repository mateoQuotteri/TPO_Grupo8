#Módulo
#turnos.py

# Usamos datetime para convertir días de la semana a fechas concretas al mostrar disponibilidades
from datetime import date, timedelta


def buscarDni(matriz, dni_buscado):
    for fila in matriz[0:]:
        if int(fila[1]) == dni_buscado:
            return True
    return False


# Convierte un nombre de día de la semana (ej: "LUNES") a la próxima fecha concreta (ej: "21/04/2026")
# Usa la librería datetime para calcular cuántos días faltan hasta ese día de la semana
def proximo_dia_semana(nombre_dia):
    dias = {
        "LUNES": 0, 
        "MARTES": 1, "MIÉRCOLES": 2, "MIERCOLES": 2,
        "JUEVES": 3, "VIERNES": 4,  "SABADO": 5, "SÁBADO": 5, "DOMINGO": 6
    }
    hoy = date.today()
    objetivo = dias.get(nombre_dia.upper())
    if objetivo is None:
        return nombre_dia
    dias_hasta = (objetivo - hoy.weekday()) % 7
    if dias_hasta == 0:
        dias_hasta = 7  
    proxima = hoy + timedelta(days=dias_hasta)
    return proxima.strftime("%d/%m/%Y")  # Devolvemos la fecha en formato correcot


def buscarNombreDoctor(matriz_doctores, matricula):

    for fila in matriz_doctores:
        if str(fila[1]) == str(matricula):
            return f"{fila[2]} {fila[3]}"
    return "Dr. o Dra. desconocid@"  


def buscarDoctorPorEspecialidad(matriz_doctores, especialidad_seleccionada):
    doctores_encontrados = []
    for fila in matriz_doctores:
        if fila[5] == especialidad_seleccionada and fila[6] == "S":
            doctores_encontrados.append(fila)
    print(f"Médicos disponibles en:  {especialidad_seleccionada}")
    print("0 - Mostrar todos los turnos disponibles.")
    for i in range(len(doctores_encontrados)):
        
        print(f"{i+1} - Matrícula: {doctores_encontrados[i][1]} | {doctores_encontrados[i][2]} {doctores_encontrados[i][3]}")
    return doctores_encontrados


def doctor_seleccionado(especialistas, seleccion):
    if seleccion == 0:
        # map con lambda - extrae la matrícula de cada especialista de la especialidad elegida por usuario
        matricula = list(map(lambda e: e[1], especialistas))
    else:
        matricula = especialistas[seleccion - 1][1]
    return matricula


def turnos_disponibles(matricula, matriz_disponibilidad, matriz_turnos, especialidad, matriz_doctores):
    # filter con lambda: filtra disponibilidades del doctor puntual o de todos los de la especialidad seleccionada
    if isinstance(matricula, list):
        dispo = list(filter(lambda fila: fila[1] in matricula, matriz_disponibilidad))
    else:
        dispo = list(filter(lambda fila: fila[1] == matricula, matriz_disponibilidad))

    if not dispo:
        print("No hay disponibilidades registradas para el médico seleccionado.")
        return None

    # Expandir cada disponibilidad en slots hora a hora y filtrar los ya ocupados
    slots = []
    for fila in dispo:
        mat = fila[1]
        dia = fila[2]
        hora_inicio = int(fila[3])
        hora_fin = int(fila[4])
        
        fecha = proximo_dia_semana(dia)
        for hora in range(hora_inicio, hora_fin):
            # filter con lambda: verifica si ese slot ya está ocupado en matriz_turnos usando la fecha concreta
            tomado = list(filter(lambda t: t[5] == mat and t[2] == str(hora) and t[1] == fecha, matriz_turnos))
            if not tomado:
                # Guardamos mat, fecha concreta, hora y nombre del doctor para mostrarlo en pantalla
                nombre_doctor = buscarNombreDoctor(matriz_doctores, mat)
                slots.append([mat, fecha, hora, nombre_doctor])

    if not slots:
        print("No hay turnos disponibles para el médico o la especialidad seleccionada.")
        return False

    print("\nTurnos disponibles:")
    for i in range(len(slots)):
        slot = slots[i]
        # Mostramos matrícula y nombre del doctor junto a la fecha concreta (DD/MM/YYYY) y hora
        print(f"  {i+1} - Matrícula: {slot[0]} | Dr./Dra.: {slot[3]} | Fecha: {slot[1]} | Hora: {slot[2]}:00 hs")
    print("  0  - Volver atrás")

    seleccion = int(input("Seleccione un turno (número): "))
    if seleccion == 0:
        return "volver"  
    while seleccion < 1 or seleccion > len(slots):
        print("Opción inválida.")
        seleccion = int(input("Seleccione un turno (número): "))

    slot_elegido = slots[seleccion - 1]
    return [slot_elegido[1], str(slot_elegido[2]), slot_elegido[0], especialidad]


def agregar_turno(matriz_turnos, matriz_pacientes, matriz_doctores, contador, matriz_disponibilidad):
    contador += 1

    dni = int(input("Ingrese el DNI del paciente (0 para volver): "))
    if dni == 0:
        return

    while not buscarDni(matriz_pacientes, dni):
        print("Dato incorrecto o DNI no registrado.")
        dni = int(input("Ingrese el DNI del paciente o 0 para volver atrás: "))
        if dni == 0:
            return

    especialidades = ["CLÍNICA MÉDICA", "PEDIATRÍA", "GINECOLOGÍA Y OBSTETRICIA", "CARDIOLOGÍA", "OFTALMOLOGÍA", "ODONTOLOGÍA", "DERMATOLOGÍA", "TRAUMATOLOGÍA"]

   
    while True:
        print("\nSeleccione una especialidad (0 para volver al menú): ")
        for i in range(len(especialidades)):
            print(i + 1, "-", especialidades[i])
        opcion = int(input("Ingrese el número de la especialidad: \t"))

        if opcion == 0:
            return  
        while opcion < 1 or opcion > len(especialidades):
            print("Opción inválida.")
            opcion = int(input("Ingrese el número de la especialidad: \t"))

        especialidad = especialidades[opcion - 1]
        especialistas = buscarDoctorPorEspecialidad(matriz_doctores, especialidad)

        seleccion = int(input("Seleccione una opción: "))
        while seleccion < 0 or seleccion > len(especialistas):
            print("Opción inválida.")
            seleccion = int(input("Seleccione una opción: "))

        matricula = doctor_seleccionado(especialistas, seleccion)
        turno = turnos_disponibles(matricula, matriz_disponibilidad, matriz_turnos, especialidad, matriz_doctores)

        if turno == "volver":
            continue

        if turno is not None and turno is not False:
            nuevo_id = len(matriz_turnos) + 1
            nueva_fila = [nuevo_id, turno[0], turno[1], str(dni), turno[3], turno[2]]
            matriz_turnos.append(nueva_fila)
            print("\nTurno agregado con éxito.\n")

        break  


def eliminar_turno(matriz_pacientes,matriz_turnos):
    '''
    Busca los turnos asociados a un DNI indicado por el usuario y permite seleccionar de un listado el turno a eliminar.
    '''
    dni = int(input("Ingrese el DNI del paciente (0 para volver): "))
    if dni == 0:
        return
    while not buscarDni(matriz_pacientes, dni):
        print("Dato incorrecto o DNI no registrado.")
        dni = int(input("Ingrese el DNI del paciente o 0 para volver atrás: "))
        if dni == 0:
            return

    cantidad_turnos = []
    contador = 1

    for i in range(len(matriz_turnos)):
        if int(matriz_turnos[i][3]) == dni:
            print(contador, "-", matriz_turnos[i])
            cantidad_turnos.append(i)
            contador += 1

    if len(cantidad_turnos) == 0:
        print("El DNI no tiene turnos asociados.")
        return

    turno_para_eliminar = int(input("Ingrese el numero de turno a eliminar o 0 para salir: "))
    if turno_para_eliminar == 0:
        return
    while turno_para_eliminar > len(cantidad_turnos):
        print("Opcion Invalida")
        turno_para_eliminar = int(input("Ingrese el numero de turno a eliminar o 0 para salir: "))
        if turno_para_eliminar ==0 :
            return

    indice_eliminado = cantidad_turnos[turno_para_eliminar - 1]
    matriz_turnos.pop(indice_eliminado)
    print("\nTurno eliminado con éxito.\n")

def modificar_turno(matriz_turnos, matriz_doctores,matriz_pacientes, matriz_disponibilidad):
    '''
    Busca los turnos asociados a DNI ingresado por el usuario y permite seleccionar del listado un turno a modificar, permite la selección de otro turno dentro de la misma especialidad.
    '''
    dni = int(input("Ingrese el DNI del paciente (0 para volver): "))
    if dni == 0:
        return
    while not buscarDni(matriz_pacientes, dni):
        print("Dato incorrecto o DNI no registrado.")
        dni = int(input("Ingrese el DNI del paciente o 0 para volver atrás: "))
        if dni == 0:
            return

    turnos_reservados = []
    for i in range(len(matriz_turnos)):
        if int(matriz_turnos[i][3]) == dni:
            print(matriz_turnos[i])
            turnos_reservados.append(matriz_turnos[i])
    if len(turnos_reservados) == 0:
        print("El DNI no tiene turnos asociados.")
        return
    print(f"LISTA TURONS RESERVADOS",turnos_reservados)
    id_turno_a_modificar = int(input("Ingrese el numero de turno a modificar o 0 para volver: "))
    if id_turno_a_modificar == 0:
        return
    while id_turno_a_modificar not in turnos_reservados[0]:
        print("Opcion Invalida")
        id_turno_a_modificar = int(input("Ingrese el numero de turno a modificar o 0 para volver: "))
        if id_turno_a_modificar == 0:
            return
        
    for x in range(len(turnos_reservados)):
        if id_turno_a_modificar == turnos_reservados[x][0]:
            print(turnos_reservados[x][0])
            id_turno = turnos_reservados[x][0] -1 
            print("ID TURNO ",id_turno)
            especialidad=turnos_reservados[x][4]
            turno_a_modificar=turnos_reservados[x]

    especialistas = buscarDoctorPorEspecialidad(matriz_doctores, especialidad)

    seleccion = int(input("Seleccione una opción: "))
    while seleccion < 0 or seleccion > len(especialistas):
        print("Opción inválida.")
        seleccion = int(input("Seleccione una opción: "))

    matricula = doctor_seleccionado(especialistas, seleccion)
    
    turno = turnos_disponibles(matricula, matriz_disponibilidad, matriz_turnos, turno_a_modificar[4], matriz_doctores)

    if turno is not None and turno is not False:
        matriz_turnos[id_turno][1] = turno[0]
        matriz_turnos[id_turno][2] = turno[1]
        matriz_turnos[id_turno][4] = turno[3]
        print("\nTurno modificado con éxito.\n")
    
    return
    
    