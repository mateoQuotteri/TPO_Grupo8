# Módulo
# disponibilidad.py


def buscar_matricula(lista_doctores):
    """
    Pide el ingreso de una matrícula por teclado y verifica que se encuentre en la lista de doctores.
    """
    matriculas=[m["matricula"] for m in lista_doctores]
    matricula = input("Ingrese matrícula del doctor: ")
    while matricula not in matriculas:
        print("La matrícula ingresada no se encuentra en el sistema. Vuelva a intentar.")
        matricula = input("Ingrese matrícula del doctor: ")
    return matricula
        

# Agregar una nueva disponibilidad a la lista de disponibilidad
def agregar_disponibilidad(lista_disponibilidad, id_contador,lista_doctores):
    print("\n--- AGREGAR DISPONIBILIDAD ---")

    dias = ["LUNES","MARTES", "MIÉRCOLES", "MIERCOLES",
        "JUEVES", "VIERNES", "SABADO", "SÁBADO", "DOMINGO"]

    matricula=buscar_matricula(lista_doctores)

    dia = input("Ingrese día (Ej: Lunes): ").upper()
    while dia not in dias:
            print("Ingrese un día válido. Vuelva a intentar.")
            dia = input("Ingrese día (Ej: Lunes): ").upper()

    while True:
        try:
            hora_inicio = int(input("Hora inicio (8-20): "))
            if hora_inicio>=8 and hora_inicio<=20:
                break
            else:
                print("Opcion inválida. Intente nuevamente")
        except ValueError:
            print ("Debe ingresar un número entero válido. Intente nuevamente.")
        except:
            print("Error. Intente nuevamente.")
    while True:
        try:
            hora_fin = int(input("Hora fin (0-23): "))
            if hora_fin>=8 and hora_fin<=20:
                break
            else:
                print("Opcion inválida. Intente nuevamente")
        except ValueError:
            print ("Debe ingresar un número entero válido. Intente nuevamente.")
        except:
            print("Error. Intente nuevamente.")
    

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

    ids=[d["id"] for d in lista_disponibilidad]
    

    while True:
        try:
            id_buscar = int(input("Ingrese ID de disponibilidad a eliminar: "))
            while id_buscar not in ids:
                print("ID no válido. Vuelva a intentar.")
                id_buscar = int(input("Ingrese ID de disponibilidad a eliminar: "))
            break
        except ValueError:
            print("Debe ingresar un número entero. Vuelva a intentar.")
        except:
            print("Error. Vuelva a intentar.")

    index_eliminar=ids.index(id_buscar)
    print("Se va a eliminar la disponibilidad con ID: ",id_buscar)
    confirmar=input("Ingresar S para confirmar, o N para cancelar: ")
    while confirmar != "S" and confirmar !="N":
        print("Opción inválida. Vuelva a intentar.")
        confirmar=input("Ingresar S para confirmar, o N para cancelar: ")
    if confirmar == "S":
        lista_disponibilidad.pop(index_eliminar)
        print("Disponibilidad eliminada.")
    elif confirmar == "N":
        "Operación cancelada."

# Modificar una disponibilidad de la lista de disponibilidad
def modificar_disponibilidad(lista_disponibilidad,lista_doctores):
    print("\n--- MODIFICAR DISPONIBILIDAD ---")

    ids=[d["id"] for d in lista_disponibilidad]

    while True:
        try:
            id_buscar = int(input("Ingrese ID de disponibilidad a modificar: "))
            while id_buscar not in ids:
                print("ID no válido. Vuelva a intentar.")
                id_buscar = int(input("Ingrese ID de disponibilidad a modificar: "))
            break
        except ValueError:
            print("Debe ingresar un número entero. Vuelva a intentar.")
        except:
            print("Error. Vuelva a intentar.")

    index_modificar=ids.index(id_buscar)

    #Falta terminar de modificar, tomar de referencia la modificación de doctores
    for fila in lista_disponibilidad:
        if str(fila["id"]) == id_buscar:
            print("Deje vacío para no modificar")

            nueva_matricula = input("Nueva matrícula: ")
            matricula=buscar_matricula(lista_doctores)
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
