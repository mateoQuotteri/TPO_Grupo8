#Módulo
#disponibilidad.py

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