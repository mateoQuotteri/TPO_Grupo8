#Módulo
#turnos.py
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