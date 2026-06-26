import turnos


def test_ordenar_turnos_por_fecha():
    turnos_desordenados = [
        {"id": 1, "fecha": "15/05/2026", "hora": "9", "dni": "11111111", "especialidad": "CARDIOLOGIA", "matricula": "10001"},
        {"id": 2, "fecha": "02/04/2026", "hora": "9", "dni": "22222222", "especialidad": "CARDIOLOGIA", "matricula": "10001"},
        {"id": 3, "fecha": "10/05/2026", "hora": "9", "dni": "33333333", "especialidad": "CARDIOLOGIA", "matricula": "10001"},
    ]

    ordenados = turnos.ordenar_turnos_por_fecha(turnos_desordenados)

    assert [t["id"] for t in ordenados] == [2, 3, 1]


def test_turno_ocupado_detecta_turno_existente():
    lista_turnos = [
        {"id": 1, "fecha": "02/04/2026", "hora": "10", "dni": "11111111", "especialidad": "PEDIATRIA", "matricula": "10001"}
    ]

    assert turnos.turno_ocupado(lista_turnos, "02/04/2026", "10", "10001") == True


def test_porcentaje_turnos_por_medico():
    lista_turnos = [
        {"id": 1, "fecha": "02/04/2026", "hora": "10", "dni": "11111111", "especialidad": "PEDIATRIA", "matricula": "10001"},
        {"id": 2, "fecha": "03/04/2026", "hora": "10", "dni": "22222222", "especialidad": "PEDIATRIA", "matricula": "10001"},
        {"id": 3, "fecha": "04/04/2026", "hora": "10", "dni": "33333333", "especialidad": "CLINICA", "matricula": "10002"},
    ]
    lista_doctores = [
        {"matricula": "10001", "nombre": "ANA", "apellido": "LOPEZ"},
        {"matricula": "10002", "nombre": "JUAN", "apellido": "PEREZ"},
    ]

    reporte = turnos.calcular_porcentajes_turnos_por_medico(lista_turnos, lista_doctores)

    assert reporte[0]["turnos"] == 2
    assert reporte[0]["porcentaje"] == 66.67


def test_porcentajes_suman_100():
    lista_turnos = [
        {"id": 1, "fecha": "02/04/2026", "hora": "10", "dni": "11111111", "especialidad": "PEDIATRIA", "matricula": "10001"},
        {"id": 2, "fecha": "03/04/2026", "hora": "10", "dni": "22222222", "especialidad": "CLINICA", "matricula": "10002"},
        {"id": 3, "fecha": "04/04/2026", "hora": "10", "dni": "33333333", "especialidad": "CARDIOLOGIA", "matricula": "10003"},
    ]
    lista_doctores = [
        {"matricula": "10001", "nombre": "ANA", "apellido": "LOPEZ"},
        {"matricula": "10002", "nombre": "JUAN", "apellido": "PEREZ"},
        {"matricula": "10003", "nombre": "MARA", "apellido": "DIAZ"},
    ]

    reporte = turnos.calcular_porcentajes_turnos_por_medico(lista_turnos, lista_doctores)
    total_porcentajes = round(sum(fila["porcentaje"] for fila in reporte), 2)

    # Test: se valida que los porcentajes calculados sumen 100
    assert total_porcentajes == 100


def test_ordenar_pacientes_con_dni_mixto():
    pacientes = [
        {"id": 1, "dni": 30000000, "nombre": "ANA", "apellido": "LOPEZ", "telefono": "1111111111", "correo": "A@A.COM"},
        {"id": 2, "dni": "20000000", "nombre": "JUAN", "apellido": "PEREZ", "telefono": "2222222222", "correo": "B@B.COM"},
    ]

    pacientes.sort(key=lambda p: str(p["dni"]))

    assert [p["dni"] for p in pacientes] == ["20000000", 30000000]


def test_ordenar_turnos_por_hora_y_especialidad():
    lista_turnos = [
        {"id": 1, "fecha": "02/04/2026", "hora": "12", "dni": "11111111", "especialidad": "PEDIATRIA", "matricula": "10001"},
        {"id": 2, "fecha": "02/04/2026", "hora": "9", "dni": "22222222", "especialidad": "CARDIOLOGIA", "matricula": "10002"},
    ]

    por_hora = turnos.ordenar_turnos_por_campo(lista_turnos, "hora")
    por_especialidad = turnos.ordenar_turnos_por_campo(lista_turnos, "especialidad")

    assert [t["id"] for t in por_hora] == [2, 1]
    assert [t["id"] for t in por_especialidad] == [2, 1]


test_ordenar_turnos_por_fecha()
test_turno_ocupado_detecta_turno_existente()
test_porcentaje_turnos_por_medico()
test_porcentajes_suman_100()
test_ordenar_pacientes_con_dni_mixto()
test_ordenar_turnos_por_hora_y_especialidad()
print("Pruebas con assert ejecutadas correctamente.")


