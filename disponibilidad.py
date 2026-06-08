# Módulo
# disponibilidad.py

# Agregar una nueva disponibilidad a la lista de disponibilidad
def agregar_disponibilidad(lista_disponibilidad, id_contador):
    print("\n--- AGREGAR DISPONIBILIDAD ---")

    matricula = input("Ingrese matrícula del doctor: ")
    dia = input("Ingrese día (Ej: Lunes): ").upper()
    hora_inicio = int(input("Hora inicio (0-23): "))
    hora_fin = int(input("Hora fin (0-23): "))

    # VALIDACIÓN SIMPLE
    if hora_inicio >= hora_fin:
        print("Error: hora inicio debe ser menor que hora fin.")
        return

    # VALIDAR DUPLICADO (mismo doctor, mismo día y rango igual)
    for fila in lista_disponibilidad:
        if fila["matricula"] == matricula and fila["dia"] == dia:
            if fila["hora_inicio"] == str(hora_inicio) and fila["hora_fin"] == str(hora_fin):
                print("Error: disponibilidad duplicada.")
                return

    nueva_disp = {
        "id": id_contador,
        "matricula": matricula,
        "dia": dia,
        "hora_inicio": str(hora_inicio),
        "hora_fin": str(hora_fin)
    }
    lista_disponibilidad.append(nueva_disp)
    print("Disponibilidad agregada correctamente.")

# Eliminar una disponibilidad de la lista de disponibilidad
def eliminar_disponibilidad(lista_disponibilidad):
    print("\n--- ELIMINAR DISPONIBILIDAD ---")

    id_buscar = input("Ingrese ID de disponibilidad a eliminar: ")

    for i in range(len(lista_disponibilidad)):
        if str(lista_disponibilidad[i]["id"]) == id_buscar:
            lista_disponibilidad.pop(i)
            print("Disponibilidad eliminada.")
            return

    print("Error: no se encontró el ID.")

# Modificar una disponibilidad de la lista de disponibilidad
def modificar_disponibilidad(lista_disponibilidad):
    print("\n--- MODIFICAR DISPONIBILIDAD ---")

    id_buscar = input("Ingrese ID de disponibilidad a modificar: ")

    for fila in lista_disponibilidad:
        if str(fila["id"]) == id_buscar:
            print("Deje vacío para no modificar")

            nueva_matricula = input("Nueva matrícula: ")
            nuevo_dia = input("Nuevo día: ").upper()
            nueva_hora_inicio = input("Nueva hora inicio: ")
            nueva_hora_fin = input("Nueva hora fin: ")

            if nueva_matricula != "":
                fila["matricula"] = nueva_matricula
            if nuevo_dia != "":
                fila["dia"] = nuevo_dia
            if nueva_hora_inicio != "":
                fila["hora_inicio"] = nueva_hora_inicio
            if nueva_hora_fin != "":
                fila["hora_fin"] = nueva_hora_fin

            # VALIDACIÓN SIMPLE
            if int(fila["hora_inicio"]) >= int(fila["hora_fin"]):
                print("Error: rango horario inválido.")
                return

            print("Disponibilidad modificada correctamente.")
            return

    print("Error: no se encontró el ID.")
