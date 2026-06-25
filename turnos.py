# Módulo
# turnos.py

# Usamos datetime para convertir días de la semana a fechas concretas al mostrar disponibilidades
from datetime import date, timedelta

# Recursividad: Verifica si un DNI existe dentro de la lista de pacientes.
# ¿Por qué es válida esta función? Porque cada llamada recursiva reduce el tamaño de la lista de pacientes, 
# acercándonos al caso base donde la lista está vacía o encontramos el DNI buscado. 
# Esto garantiza que lleguemos a una conclusión sobre la existencia del DNI en la lista.
def buscarDni(lista_pacientes, dni_buscado):
    # Caso base: si la lista está vacía, el DNI no se encontró.
    if not lista_pacientes:
        return False
    
    # Caso base: si el DNI del primer paciente coincide con el buscado, lo encontramos.
    if int(lista_pacientes[0]["dni"]) == dni_buscado:
        return True
    
    #Caso recursivo y reducción del dominio.
    return buscarDni(lista_pacientes[1:], dni_buscado)

# Convierte un nombre de día de la semana (ej: "LUNES") a la próxima fecha concreta (ej: "21/04/2026")
# Usa la librería datetime para calcular cuántos días faltan hasta ese día de la semana
def proximo_dia_semana(nombre_dia):
    dias = {
        "LUNES": 0,
        "MARTES": 1, "MIÉRCOLES": 2, "MIERCOLES": 2,
        "JUEVES": 3, "VIERNES": 4, "SABADO": 5, "SÁBADO": 5, "DOMINGO": 6
    }
    hoy = date.today()
    objetivo = dias.get(nombre_dia.upper())
    if objetivo is None:
        return nombre_dia
    dias_hasta = (objetivo - hoy.weekday()) % 7
    if dias_hasta == 0:
        dias_hasta = 7
    proxima = hoy + timedelta(days=dias_hasta)
    return proxima.strftime("%d/%m/%Y")  # Devolvemos la fecha en formato correcto.

# Recursividad: Busca y devuelve el nombre completo de un médico utilizando su número de matrícula.
# ¿Por qué es válida esta función? Porque cada llamada recursiva reduce el tamaño de la lista de doctores, 
# acercándonos al caso base donde la lista está vacía o encontramos la matrícula buscada. 
# Esto garantiza que lleguemos a una conclusión sobre la existencia de la matrícula en la lista y 
# podamos devolver el nombre del doctor o un mensaje de desconocido.

def buscarNombreDoctor(lista_doctores, matricula):
    # Caso base: lista vacía, el médico no está registrado.
    if not lista_doctores:
        return "Dr. o Dra. desconocid@"

    # Caso base: encontramos la matrícula en el primer elemento.
    if str(lista_doctores[0]["matricula"]) == str(matricula):
        return f"{lista_doctores[0]['nombre']} {lista_doctores[0]['apellido']}"

    # Caso recursivo y reducción del dominio: seguimos buscando en el resto de la lista.
    return buscarNombreDoctor(lista_doctores[1:], matricula)

# Recursividad: Filtra y muestra los médicos activos que pertenecen a una especialidad específica.
# ¿Por qué es válida esta función? Porque cada llamada recursiva reduce el tamaño de la lista de doctores, 
# acercándonos al caso base donde la lista está vacía. 
# Esto garantiza que procesemos todos los doctores y devolvamos solo aquellos que cumplen con los criterios de especialidad y si está activo.

def filtrarDoctoresRecursivo(lista_doctores, especialidad_seleccionada):
    # Caso base: si no hay doctores, devolvemos una lista vacía.
    if not lista_doctores:
        return []

    primer_doc = lista_doctores[0]
    # Caso recursivo y reducción del dominio: obtenemos primero los doctores válidos del resto de la lista.
    resto_filtrado = filtrarDoctoresRecursivo(lista_doctores[1:], especialidad_seleccionada)

    if primer_doc["especialidad"] == especialidad_seleccionada and primer_doc["activo"] == "S":
        return [primer_doc] + resto_filtrado
    else:
        return resto_filtrado


def buscarDoctorPorEspecialidad(lista_doctores, especialidad_seleccionada):
    # Filtramos usando la función recursiva que devuelve solo los doctores activos de la especialidad seleccionada por el usuario.
    doctores_encontrados = filtrarDoctoresRecursivo(lista_doctores, especialidad_seleccionada)

    # Sorted con lambda: doctores ordenados alfabeticamente por apellido
    doctores_ordenados = sorted(doctores_encontrados, key=lambda doc: doc["apellido"])

    print(f"Médicos disponibles en:  {especialidad_seleccionada}")
 
    for i in range(len(doctores_ordenados)):
        print(f"{i+1} - Matrícula: {doctores_ordenados[i]['matricula']} | {doctores_ordenados[i]['nombre']} {doctores_ordenados[i]['apellido']}")

    return doctores_ordenados


# Retorna la matrícula del médico elegido o una lista de matrículas si se seleccionan todos los de la especialidad.
def doctor_seleccionado(especialistas, seleccion):
    if seleccion == 0:
        # map con lambda - extrae la matrícula de cada especialista de la especialidad elegida por usuario
        matricula = list(map(lambda e: e["matricula"], especialistas))
    else:
        matricula = especialistas[seleccion - 1]["matricula"]
    return matricula

# Genera, filtra y muestra los horarios libres de un médico comparando su disponibilidad con los turnos ya reservados.
def turnos_disponibles(matricula, lista_disponibilidad, lista_turnos, especialidad, lista_doctores):
    # filter con lambda: filtra disponibilidades del doctor puntual o de todos los de la especialidad seleccionada
    if isinstance(matricula, list):
        dispo = list(filter(lambda fila: fila["matricula"] in matricula, lista_disponibilidad))
    else:
        dispo = list(filter(lambda fila: fila["matricula"] == matricula, lista_disponibilidad))

    if not dispo:
        print("No hay disponibilidades registradas para el médico seleccionado.")
        return None

    # Expandir cada disponibilidad en slots hora a hora y filtrar los ya ocupados
    slots = []
    for fila in dispo:
        mat = fila["matricula"]
        dia = fila["dia"]
        hora_inicio = int(fila["hora_inicio"])
        hora_fin = int(fila["hora_fin"])

        fecha = proximo_dia_semana(dia)
        for hora in range(hora_inicio, hora_fin):
            # filter con lambda: verifica si ese slot ya está ocupado en lista_turnos usando la fecha concreta
            tomado = list(filter(
                lambda t: t["matricula"] == mat and t["hora"] == str(hora) and t["fecha"] == fecha,
                lista_turnos
            ))
            if not tomado:
                # Guardamos mat, fecha concreta, hora y nombre del doctor para mostrarlo en pantalla
                nombre_doctor = buscarNombreDoctor(lista_doctores, mat)
                slots.append({"matricula": mat, "fecha": fecha, "hora": hora, "nombre_doctor": nombre_doctor})

    if not slots:
        print("No hay turnos disponibles para el médico o la especialidad seleccionada.")
        return False

    print("\nTurnos disponibles:")
    for i in range(len(slots)):
        slot = slots[i]
        # Mostramos matrícula y nombre del doctor junto a la fecha concreta (DD/MM/YYYY) y hora
        print(f"  {i+1} - Matrícula: {slot['matricula']} | Dr./Dra.: {slot['nombre_doctor']} | Fecha: {slot['fecha']} | Hora: {slot['hora']}:00 hs")
    print("  0  - Volver atrás")

    seleccion = int(input("Seleccione un turno (número): "))
    if seleccion == 0:
        return "volver"
    while seleccion < 1 or seleccion > len(slots):
        print("Opción inválida.")
        seleccion = int(input("Seleccione un turno (número): "))

    slot_elegido = slots[seleccion - 1]
    return [slot_elegido["fecha"], str(slot_elegido["hora"]), slot_elegido["matricula"], especialidad]

# Verifica si un turno para esa fecha, hora y médico ya está tomado.
def turno_ocupado(lista_turnos, fecha, hora, matricula):
    for turno in lista_turnos:
        if turno["fecha"] == fecha and turno["hora"] == str(hora) and turno["matricula"] == matricula:
            return True
    return False

# Gestiona el flujo completo para registrar un nuevo turno: valida el paciente, elige especialidad, médico y horario.
def agregar_turno(lista_turnos, lista_pacientes, lista_doctores, contador, lista_disponibilidad):
    try:

        # DNI del paciente
        try:
            dni = int(input("Ingrese el DNI del paciente (0 para volver): "))
        except ValueError:
            print("Error: El DNI debe ser un número entero.")
            return contador

        if dni == 0:
            return contador

        if not buscarDni(lista_pacientes, dni):
            print("Dato incorrecto o DNI no registrado.")
            return contador

        # Selección de especialidad
        especialidades = [
            "CLÍNICA MÉDICA", "PEDIATRÍA", "GINECOLOGÍA",
            "CARDIOLOGÍA", "OFTALMOLOGÍA", "ODONTOLOGÍA",
            "DERMATOLOGÍA", "TRAUMATOLOGÍA"
        ]
        print("\nSeleccione una especialidad (0 para volver al menú): ")
        for i, esp in enumerate(especialidades, start=1):
            print(i, "-", esp)
        
        try:
            opcion = int(input("Ingrese el número de la especialidad: "))
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            return contador

        if opcion == 0:
            return contador
        if opcion < 1 or opcion > len(especialidades):
            print("Opción inválida. Debe estar dentro del rango.")
            return contador

        especialidad = especialidades[opcion - 1]
        especialistas = buscarDoctorPorEspecialidad(lista_doctores, especialidad)

        # Selección de doctor
        try:
            seleccion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            return contador

        if seleccion < 1 or seleccion > len(especialistas):
            print("Opción inválida.")
            return contador

        matricula = doctor_seleccionado(especialistas, seleccion)


        # Selección de turno disponible
        turno = turnos_disponibles(matricula, lista_disponibilidad, lista_turnos, especialidad, lista_doctores)
        if turno == "volver":
            return contador

        if turno and not turno_ocupado(lista_turnos, turno[0], turno[1], turno[2]):
            contador += 1
            nuevo_id = len(lista_turnos) + 1
            nuevo_turno = {
                "id": nuevo_id,
                "fecha": turno[0],
                "hora": turno[1],
                "dni": str(dni),
                "especialidad": turno[3],
                "matricula": turno[2]
            }
            lista_turnos.append(nuevo_turno)
            print("\nTurno agregado con éxito.\n")
        else:
            print("Ese turno ya fue tomado por otro paciente.")

        return contador

    except Exception as e:
        print(f"Error inesperado: {e}")
        return contador

# Permite al usuario visualizar los turnos de un paciente por DNI y dar de baja el que seleccione del listado.
def eliminar_turno(lista_pacientes, lista_turnos):
    try:
        dni = int(input("Ingrese el DNI del paciente (0 para volver): "))
    except ValueError:
        print("Error: El DNI debe ser un número entero.")
        return

    if dni == 0:
        return

    while not buscarDni(lista_pacientes, dni):
        print("Dato incorrecto o DNI no registrado.")
        try:
            dni = int(input("Ingrese el DNI del paciente o 0 para volver atrás: "))
        except ValueError:
            print("Error: El DNI debe ser un número entero.")
            return
        if dni == 0:
            return

    cantidad_turnos = []
    contador = 1

    for i in range(len(lista_turnos)):
        if int(lista_turnos[i]["dni"]) == dni:
            print(contador, "-", lista_turnos[i])
            cantidad_turnos.append(i)
            contador += 1

    if len(cantidad_turnos) == 0:
        print("El DNI no tiene turnos asociados.")
        return

    try:
        turno_para_eliminar = int(input("Ingrese el numero de turno a eliminar o 0 para salir: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return

    if turno_para_eliminar == 0:
        return

    while turno_para_eliminar < 1 or turno_para_eliminar > len(cantidad_turnos):
        print("Opcion Invalida")
        try:
            turno_para_eliminar = int(input("Ingrese el numero de turno a eliminar o 0 para salir: "))
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            return
        if turno_para_eliminar == 0:
            return

    indice_eliminado = cantidad_turnos[turno_para_eliminar - 1]
    lista_turnos.pop(indice_eliminado)
    print("\nTurno eliminado con éxito.\n")


# Permite cambiar la fecha, hora o médico de un turno ya existente manteniendo la misma especialidad original.
def modificar_turno(lista_turnos, lista_doctores, lista_pacientes, lista_disponibilidad):
    try:
        dni = int(input("Ingrese el DNI del paciente (0 para volver): "))
    except ValueError:
        print("Error: El DNI debe ser un número entero.")
        return

    if dni == 0:
        return

    while not buscarDni(lista_pacientes, dni):
        print("Dato incorrecto o DNI no registrado.")
        try:
            dni = int(input("Ingrese el DNI del paciente o 0 para volver atrás: "))
        except ValueError:
            print("Error: El DNI debe ser un número entero.")
            return
        if dni == 0:
            return

    turnos_reservados = []
    for i in range(len(lista_turnos)):
        if int(lista_turnos[i]["dni"]) == dni:
            print(lista_turnos[i])
            turnos_reservados.append(lista_turnos[i])

    if len(turnos_reservados) == 0:
        print("El DNI no tiene turnos asociados.")
        return

    print(f"LISTA TURNOS RESERVADOS", turnos_reservados)
    try:
        id_turno_a_modificar = int(input("Ingrese el numero de turno a modificar o 0 para volver: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return

    if id_turno_a_modificar == 0:
        return

    while id_turno_a_modificar not in [t["id"] for t in turnos_reservados]:
        print("Opcion Invalida")
        try:
            id_turno_a_modificar = int(input("Ingrese el numero de turno a modificar o 0 para volver: "))
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            return
        if id_turno_a_modificar == 0:
            return

    turno_a_modificar = None
    id_turno = None
    for x in range(len(turnos_reservados)):
        if id_turno_a_modificar == turnos_reservados[x]["id"]:
            id_turno = turnos_reservados[x]["id"] - 1
            especialidad = turnos_reservados[x]["especialidad"]
            turno_a_modificar = turnos_reservados[x]

    especialistas = buscarDoctorPorEspecialidad(lista_doctores, especialidad)

    try:
        seleccion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return

    while seleccion < 0 or seleccion > len(especialistas):
        print("Opción inválida.")
        try:
            seleccion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            return

    matricula = doctor_seleccionado(especialistas, seleccion)

    turno = turnos_disponibles(matricula, lista_disponibilidad, lista_turnos, turno_a_modificar["especialidad"], lista_doctores)

    if turno is not None and turno is not False:
        lista_turnos[id_turno]["fecha"] = turno[0]
        lista_turnos[id_turno]["hora"] = turno[1]
        lista_turnos[id_turno]["especialidad"] = turno[3]
        print("\nTurno modificado con éxito.\n")
