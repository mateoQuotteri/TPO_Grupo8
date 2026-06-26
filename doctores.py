# Modulo
# doctores.py

# Valida matrícula única, datos de contacto y especialidad para sumar un nuevo doctor.
def agregar_doctor(lista, contador):
    try:
        matricula = input("Ingrese el número de matricula: ")
        while not matricula.isdigit() or not (10000 <= int(matricula) <= 99999):
            print("Dato incorrecto")
            matricula = input("Ingrese el número de matricula: ")

        for doctor in lista:
            if doctor["matricula"] == matricula:
                print("La matrícula ya está asociada a un doctor.")
                return contador

        contador += 1
        nombre = input("Ingrese el nombre: ").upper()
        apellido = input("Ingrese el apellido: ").upper()

        telefono = input("Ingrese el telefono: ")
        while not telefono.isdigit() or not (1000000000 <= int(telefono) <= 9999999999):
            print("Dato incorrecto.")
            telefono = input("Ingrese el número de teléfono: ")

        especialidades = ["CLÍNICA MÉDICA", "PEDIATRÍA", "GINECOLOGÍA Y OBSTETRICIA", "CARDIOLOGÍA", "OFTALMOLOGÍA", "ODONTOLOGÍA", "DERMATOLOGÍA", "TRAUMATOLOGÍA"]
        print("Seleccione una especialidad: ")
        for i in range(len(especialidades)):
            print(i + 1, "-", especialidades[i])

        opcion = int(input("Ingrese el número de su especialidad: "))
        while opcion < 1 or opcion > len(especialidades):
            print("Opcion invalida, seleccione una de las disponibles")
            opcion = int(input("Ingrese el número de su especialidad: "))

        especialidad = especialidades[opcion - 1]

        activo = input("Ingrese `S` para activo o `N` para inactivo: ").upper()
        while activo != "S" and activo != "N":
            print("Dato incorrecto. Ingrese `S` para activo o `N` para inactivo.")
            activo = input("Ingrese `S` para activo o `N` para inactivo: ").upper()


        nuevo_doctor = {
            "id": contador,
            "matricula": matricula,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "especialidad": especialidad,
            "activo": activo
        }
        lista.append(nuevo_doctor)
        print("\n Datos agregados con éxito!\n")
        return contador

    except ValueError:
        print ("\nDebe ingresar un número entero válido. Intente nuevamente.")
    except:
        print("\nError. Intente nuevamente.")

# Elimina el doctor correspondiente a la matrícula ingresada.
def eliminar_doctor(lista):
    matricula_buscada = input("Ingrese la matricula a eliminar: ")

    for i in range(len(lista)):
        if lista[i]["matricula"] == matricula_buscada:
            lista.pop(i)
            print("\nDoctor eliminado correctamente.\n")
            return
    print("\nNo se encontró la matricula\n")

# Permite editar campos individuales de un doctor mediante un menú de opciones.
def modificar_doctor(lista):
    try:
        matricula_buscada = input("Ingrese la matricula del doctor que desea modificar: ")
        while not matricula_buscada.isdigit() or not (10000 <= int(matricula_buscada) <= 99999):
            print("Dato incorrecto")
            matricula_buscada = input("Ingrese la matricula del doctor que desea modificar: ")

        for doctor in lista:
            if doctor["matricula"] == matricula_buscada:
                editando = True
                while editando:
                    print("\nSeleccione el dato que desea modificar:")
                    print("[1] Nombre")
                    print("[2] Apellido")
                    print("[3] Teléfono")
                    print("[4] Especialidad")
                    print("[5] Activo/Inactivo")
                    print("[0] Terminar edición")

                    opcion = input("Ingrese una opción: ")

                    if opcion == "0":
                        print("\nEdición terminada.\n")
                        editando = False

                    elif opcion == "1":
                        doctor["nombre"] = input("Ingrese el nuevo nombre: ").upper()

                    elif opcion == "2":
                        doctor["apellido"] = input("Ingrese el nuevo apellido: ").upper()

                    elif opcion == "3":
                        telefono = input("Ingrese el nuevo teléfono: ")
                        while not telefono.isdigit() or not (1000000000 <= int(telefono) <= 9999999999):
                            print("Dato incorrecto")
                            telefono = input("Ingrese el nuevo teléfono: ")
                        doctor["telefono"] = telefono

                    elif opcion == "4":
                        especialidades = ["CLÍNICA MÉDICA", "PEDIATRÍA", "GINECOLOGÍA Y OBSTETRICIA", "CARDIOLOGÍA", "OFTALMOLOGÍA", "ODONTOLOGÍA", "DERMATOLOGÍA", "TRAUMATOLOGÍA"]
                        print("Seleccione una especialidad: ")
                        for j in range(len(especialidades)):
                            print(j + 1, "-", especialidades[j])
                        opcion_esp = int(input("Ingrese el número de su especialidad: "))
                        while opcion_esp < 1 or opcion_esp > len(especialidades):
                            print("Opcion invalida, seleccione una de las disponibles")
                            opcion_esp = int(input("Ingrese el número de su especialidad: "))
                        doctor["especialidad"] = especialidades[opcion_esp - 1]

                    elif opcion == "5":
                        activo = input("Ingrese `S` para activo o `N` para inactivo: ").upper()
                        while activo != "S" and activo != "N":
                            print("Dato incorrecto. Ingrese `S` para activo o `N` para inactivo.")
                            activo = input("Ingrese `S` para activo o `N` para inactivo: ").upper()
                        doctor["activo"] = activo
                return

        print("\nNo se encontró la matricula\n")
    except ValueError:
        print ("\nDebe ingresar un número entero válido. Intente nuevamente.")
    except:
        print("\nError. Intente nuevamente.")

# Genera un reporte comparando doctores registrados vs doctores con disponibilidad cargada.
def reporte_cobertura_medica(lista_doctores, lista_disponibilidad):
    todos_los_doctores = set()
    for doc in lista_doctores:
        todos_los_doctores.add(doc["matricula"])

    # Matrículas que aparecen en la tabla de disponibilidad
    doctores_con_horario = set()
    for disp in lista_disponibilidad:
        doctores_con_horario.add(disp["matricula"])

    # Diferencia: doctores registrados pero SIN horarios cargados
    doctores_sin_horario = todos_los_doctores - doctores_con_horario

    ancho = 44
    print()
    print("╔" + "═" * ancho + "╗")
    print("║" + "  REPORTE DE COBERTURA MÉDICA".center(ancho) + "║")
    print("╠" + "═" * ancho + "╣")
    print("║" + f"  Total de doctores registrados:   {len(todos_los_doctores)}".ljust(ancho) + "║")
    print("║" + f"  Doctores con disponibilidad:     {len(doctores_con_horario)}".ljust(ancho) + "║")
    print("║" + f"  Doctores sin disponibilidad:     {len(doctores_sin_horario)}".ljust(ancho) + "║")
    print("╠" + "═" * ancho + "╣")
    if doctores_sin_horario:
        print("║" + "  [!] Matrículas a revisar:".ljust(ancho) + "║")
        # Para que el usuario vea las matriculas ordenadas usamos sorted
        for mat in sorted(doctores_sin_horario):
            print("║" + f"        - {mat}".ljust(ancho) + "║")
    else:
        print("║" + "  [OK] Todos los doctores tienen horarios.".ljust(ancho) + "║")
    print("╚" + "═" * ancho + "╝")
    print()

#Porcentaje de doctores activos
def reporte_doctores_activos(lista_doctores):
    activos = sum(1 for d in lista_doctores if d["activo"] == "S")
    inactivos = sum(1 for d in lista_doctores if d["activo"] == "N")
    total = activos + inactivos

    porcentaje = (activos / total) * 100 if total > 0 else 0

    print("\n--- REPORTE DE DOCTORES ACTIVOS ---")
    print(f"Doctores activos: {activos} ({porcentaje:.2f}%)")
    print(f"Doctores inactivos: {inactivos}")
