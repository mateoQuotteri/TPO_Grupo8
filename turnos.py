#Módulo
#turnos.py


def buscarDni(matriz, dni_buscado):
        for fila in matriz[0:]:
            if int(fila[1]) == dni_buscado:
                return True
        return False

def buscarDoctorPorEspecialidad(matriz_doctores, especialidad_seleccionada):
    doctores_encontrados = []
    for fila in matriz_doctores:
        if fila[5] == especialidad_seleccionada and fila[6] == "S":
            doctores_encontrados.append(fila)
    print(f"Médicos disponibles en:  {especialidad_seleccionada}\t")
    print("0 - Mostrar todos los turnos disponibles.")
    for i in range(len(doctores_encontrados)):
        print(f"{i+1} - {doctores_encontrados[i][2]} {doctores_encontrados[i][3]}")
    return doctores_encontrados

def doctor_seleccionado(especialistas, seleccion):
    if seleccion == 0:
        # map con lambda - extrae la matrícula de cada especialista de la especialidad elegida por usuario
        matricula = list(map(lambda e: e[1], especialistas))
    else:
        matricula = especialistas[seleccion - 1][1]
    return matricula

def turnos_disponibles(matricula, matriz_disponibilidad, matriz_turnos, especialidad):
    # filter con lambda: filtra disponibilidades del doctor puntual o de todos los de la especialidad que selecciono el usuario por consola
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
        print("La fila mostrada es: " + str(fila)) 
        mat = fila[1]
        dia = fila[2]
        hora_inicio = int(fila[3])
        hora_fin = int(fila[4])
        for hora in range(hora_inicio, hora_fin):
            # filter con lambda: verifica si ese slot ya está ocupado en matriz_turnos
            tomado = list(filter(lambda t: t[5] == mat and t[2] == str(hora) and t[1] == dia, matriz_turnos))
            if not tomado:
                slots.append([mat, dia, hora])

    if not slots:
        print("No hay turnos disponibles para el medico o la especialidad seleccionad.")
        return False

    print("\nTurnos disponibles:")
    for i in range(len(slots)):
        slot = slots[i]
        print(f"  {i+1} - Matrícula: {slot[0]} | Día: {slot[1]} | Hora: {slot[2]}:00 hs")

    seleccion = int(input("Seleccione un turno (número): "))
    while seleccion < 1 or seleccion > len(slots):
        print("Opción inválida.")
        seleccion = int(input("Seleccione un turno (número): "))

    slot_elegido = slots[seleccion - 1]
    return [slot_elegido[1], str(slot_elegido[2]), slot_elegido[0], especialidad]



def agregar_turno(matriz_turnos, matriz_pacientes, matriz_doctores, contador, matriz_disponibilidad):
    contador += 1

    
    dni = int(input("Ingrese el DNI del paciente: "))

    while not buscarDni(matriz_pacientes, dni):
        print("Dato incorrecto o DNI no registrado.")
        dni = int(input("Ingrese el DNI del paciente o 0 para volver atrás: "))

    
    
    especialidades=["CLÍNICA MÉDICA", "PEDIATRÍA", "GINECOLOGÍA Y OBSTETRICIA", "CARDIOLOGÍA", "OFTALMOLOGÍA", "ODONTOLOGÍA", "DERMATOLOGÍA", "TRAUMATOLOGÍA"]
    print("Seleccione una especialidad: ")
    for i in range(len(especialidades)):
        print(i + 1, "-", especialidades[i])
    opcion = int(input(f"Ingrese la especialidad del turno con el que quiere atenderse: \t"))
    
    print(f"La especialidad con la que quiere atenderse es: {especialidades[opcion - 1]}\t")
    especialidad = especialidades[opcion - 1]
    especialistas=buscarDoctorPorEspecialidad(matriz_doctores,especialidad)
    
    seleccion=int(input("Seleccione una opción: "))
    matricula=doctor_seleccionado(especialistas,seleccion)
    turno = turnos_disponibles(matricula, matriz_disponibilidad, matriz_turnos, especialidad)

    if turno is not None:
        nuevo_id = len(matriz_turnos) + 1
        nueva_fila = [nuevo_id, turno[0], turno[1], str(dni), turno[3], turno[2]]
        matriz_turnos.append(nueva_fila)
        print("\nTurno agregado con éxito.\n")
    






    return



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