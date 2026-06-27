# Módulo
# disponibilidad.py

from functools import reduce

def buscar_matricula(lista_doctores):
    """
    Pide el ingreso de una matrícula por teclado y verifica que se encuentre en la lista de doctores.
    """
    matriculas=[m["matricula"] for m in lista_doctores]
    matricula = input("Ingrese matrícula del doctor: ")
    while matricula not in matriculas:
        print("\nLa matrícula ingresada no se encuentra en el sistema. Vuelva a intentar.")
        matricula = input("\nIngrese matrícula del doctor: ")
    return matricula
        
def hora_inicio():
    """
    Pide el ingreso de la hora de inicio por teclado y verifica que sea un valor válido.
    """
    while True:
        try:
            hora = int(input("Hora de inicio (8-20): "))
            if hora>=8 and hora<=20:
                return hora
            else:
                print("\nOpcion inválida. Intente nuevamente.\n")
        except ValueError:
            print ("\nDebe ingresar un número entero válido. Intente nuevamente.")
        except:
            print("Error. Intente nuevamente.")

def hora_fin():
    """
    Pide el ingreso de la hora de finalización por teclado y verifica que sea un valor válido.
    """
    while True:
        try:
            hora = int(input("Hora de finalización (8-20): "))
            if hora>=8 and hora<=20:
                return hora
            else:
                print("\nOpcion inválida. Intente nuevamente.")
        except ValueError:
            print ("\nDebe ingresar un número entero válido. Intente nuevamente.")
        except:
            print("Error. Intente nuevamente.")

def buscar_id_disponibilidad(lista_disponibilidad):
    """
    Pide el ingreso por teclado el ID de Disponibilidad a buscar y verifica que exista.
    """
    ids=[d["id"] for d in lista_disponibilidad]
    while True:
        try:
            id_buscar = int(input("\nIngrese ID de disponibilidad: "))
            while id_buscar not in ids:
                print("\nID no válido. Vuelva a intentar.")
                id_buscar = int(input("\nIngrese ID de disponibilidad: "))
            return id_buscar
        except ValueError:
            print("\nDebe ingresar un número entero. Vuelva a intentar.\n")
        except:
            print("Error. Vuelva a intentar.")

# Agregar una nueva disponibilidad a la lista de disponibilidad
def agregar_disponibilidad(lista_disponibilidad, id_contador,lista_doctores):
    """
    Permite agregar una disponibilidad pidiendo todos los datos por teclado. Verifica que la matrícula del médico exista.
    Verifica que los datos sean concordantes con el sistema.
    """
    print("\n--- AGREGAR DISPONIBILIDAD ---\n")

    dias = ["LUNES","MARTES", "MIÉRCOLES", "MIERCOLES",
        "JUEVES", "VIERNES", "SABADO", "SÁBADO", "DOMINGO"]
    matricula=buscar_matricula(lista_doctores)

    dia = input("\nIngrese día (Ej: Lunes): ").upper()
    while dia not in dias:
            print("\nIngrese un día válido. Vuelva a intentar.")
            dia = input("\nIngrese día (Ej: Lunes): ").upper()

    hora_i=hora_inicio()
    hora_f=hora_fin()
    
    # VALIDACIÓN SIMPLE
    if hora_i >= hora_f:
        print("\nError: Hora de inicio debe ser menor que hora finalización.\n")
        return id_contador

    # VALIDAR DUPLICADO (mismo doctor, mismo día y rango igual)
    for fila in lista_disponibilidad:
        if fila["matricula"] == str(matricula) and fila["dia"] == dia:
            if fila["hora_inicio"] == str(hora_i) and fila["hora_fin"] == str(hora_f):
                print("\nError: disponibilidad duplicada.\n")
                return id_contador
    id_contador += 1
    nueva_disp = {
        "id": id_contador,
        "matricula": matricula,
        "dia": dia,
        "hora_inicio": str(hora_i),
        "hora_fin": str(hora_f)
    }
    lista_disponibilidad.append(nueva_disp)
    print("\nDisponibilidad agregada correctamente.\n")
    return id_contador

# Eliminar una disponibilidad de la lista de disponibilidad
def eliminar_disponibilidad(lista_disponibilidad):
    '''
    Permite eliminar una disponibilidad ingresando el ID. Pide confirmación.
    '''
    print("\n--- ELIMINAR DISPONIBILIDAD ---\n")

    ids=[d["id"] for d in lista_disponibilidad]
    id_buscar=buscar_id_disponibilidad(lista_disponibilidad)
    index_eliminar=ids.index(id_buscar)
    print("\nSe va a eliminar la disponibilidad con ID: ",id_buscar)
    confirmar=input("\nIngresar S para confirmar, o N para cancelar: ")
    while confirmar != "S" and confirmar !="N":
        print("\nOpción inválida. Vuelva a intentar.")
        confirmar=input("\nIngresar S para confirmar, o N para cancelar: ")
    if confirmar == "S":
        lista_disponibilidad.pop(index_eliminar)
        print("\nDisponibilidad eliminada.\n")
    elif confirmar == "N":
        print("\nOperación cancelada.\n")

# Modificar una disponibilidad de la lista de disponibilidad
def modificar_disponibilidad(lista_disponibilidad,lista_doctores):
    '''
    Permite modificar los campos de una disponibilidad selecciona por ID y verifica que no exista una igual.
    Si hay una igual, deshace los cambios volviendo a dejar la información original guardada en el respaldo hecho al principio.
    '''
    print("\n--- MODIFICAR DISPONIBILIDAD ---\n")

    dias = ["LUNES","MARTES", "MIÉRCOLES", "MIERCOLES",
        "JUEVES", "VIERNES", "SABADO", "SÁBADO", "DOMINGO"]
    ids=[d["id"] for d in lista_disponibilidad]

    id_buscar=buscar_id_disponibilidad(lista_disponibilidad)
    index_modificar=ids.index(id_buscar)
    respaldo=lista_disponibilidad[index_modificar].copy()

    editando = True
    while editando:
        cambios = False
        print("\nSeleccione el dato que desea modificar:")
        print("[1] Matrícula.")
        print("[2] Día.")
        print("[3] Hora de Inicio.")
        print("[4] Hora de Finalización.")
        print("[5] Rango Horario Completo.")
        print("[0] Terminar edición.")

        opcion = input("Ingrese una opción: ")

        if opcion == "0":
            print("\nEdición terminada.\n")
            editando = False

        elif opcion == "1":
            matricula=buscar_matricula(lista_doctores)
            lista_disponibilidad[index_modificar]["matricula"]=matricula
            cambios=True
            
        elif opcion == "2":
            dia = input("\nIngrese día (Ej: Lunes): ").upper()
            while dia not in dias:
                print("\nIngrese un día válido. Vuelva a intentar.")
                dia = input("\nIngrese día (Ej: Lunes): ").upper()
            lista_disponibilidad[index_modificar]["dia"]=dia
            cambios=True
            
        elif opcion == "3":
            hora_i=hora_inicio()
            if hora_i>=int(lista_disponibilidad[index_modificar]["hora_fin"]):
                print("\nError: hora de inicio debe ser menor que hora de finalización.\n")
                hora_i=hora_inicio()
            else:
                lista_disponibilidad[index_modificar]["hora_inicio"]=str(hora_i)
                cambios=True
            
        elif opcion == "4":
            hora_f=hora_fin()
            if int(lista_disponibilidad[index_modificar]["hora_inicio"])>=hora_f:
                print("\nError: hora de inicio debe ser menor que hora de finalización.\n")
                hora_f=hora_fin()
            else:
                lista_disponibilidad[index_modificar]["hora_fin"]=str(hora_f)
                cambios=True

        elif opcion == "5":
            while True:
                hora_i=hora_inicio()
                hora_f=hora_fin()
                if hora_i >= hora_f:
                    print("\nError: hora de inicio debe ser menor que hora de finalización.\n")       
                else:
                    lista_disponibilidad[index_modificar]["hora_inicio"]=str(hora_i)
                    lista_disponibilidad[index_modificar]["hora_fin"]=str(hora_f)
                    cambios=True
                    break

        else: 
            print("\nOpción inválida.\n")

        if cambios:
            duplicado = False
            i = 0
            while i < len(lista_disponibilidad) and not duplicado:
                fila=lista_disponibilidad[i]
                if fila["id"] != id_buscar:
                    if fila["matricula"] == lista_disponibilidad[index_modificar]["matricula"] and fila["dia"] == lista_disponibilidad[index_modificar]["dia"]:
                        if str(fila["hora_inicio"]) == lista_disponibilidad[index_modificar]["hora_inicio"] and fila["hora_fin"] == lista_disponibilidad[index_modificar]["hora_fin"]:
                            duplicado = True
                i+=1

            if duplicado:
                print("\nError: disponibilidad duplicada.")
                print("No se guardaron los cambios realizados.\n")
                lista_disponibilidad[index_modificar] = respaldo
            else:
                print("\nSe guardaron los cambios. Datos actualizados correctamente.\n")

#Horas semanales por doctor
def reporte_horas_doctor(lista_disponibilidad, matricula):
    """
    Reporte de horas trabajadas según la disponibilidad del doctor, filtrado por la matricula que recibe de parámetro.
    """
    horas = [int(d["hora_fin"]) - int(d["hora_inicio"]) for d in lista_disponibilidad if d["matricula"] == matricula]

    if not horas:
        print(f"\nNo hay disponibilidad cargada para el doctor {matricula}.")
        return

    # Usamos reduce para sumar todas las horas
    total = reduce(lambda x, y: x + y, horas, 0)

    print("\n--- REPORTE DE HORAS SEMANALES ---\n")
    print(f"Doctor {matricula} trabaja {total} horas semanales.\n")
