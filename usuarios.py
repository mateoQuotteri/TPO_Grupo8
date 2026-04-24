# Ya que los usuarios son datos inmutables, aplicamos una tupla para cada usuario
usuarios = {
    "admin": ("12345", "Maria Lomoro", "ADMINISTRATIVO"),
    "recep": ("54321", "Agustin Garcia", "RECEPCIONISTA"),
    "doc": ("11111", "Dr Martinez", "DOCTOR"),
}



def agregar_usuario(usuarios):

    perfiles = ["ADMINISTRATIVO", "RECEPCIONISTA", "DOCTOR"]
    print("AGREGAR UN USUARIO")
    print()

    for i in range(len(perfiles)):
        print([i+1], perfiles[i])

    print()
    aux=int(input("Seleccione el perfil del usuario. Ingrese 0 para salir. "))
    while aux<0 or aux>len(perfiles):
        print("Opción inválida. Vuelva a intentar.")
        aux=int(input("Seleccione el perfil del usuario. Ingrese 0 para salir. "))

    if aux!=0:
        perfil=perfiles[aux-1]
        print("Perfil seleccionado: ",perfil)

        user = input("Ingrese el nombre de usuario: ")
        clave = input("Ingrese la clave: ")
        nombre = input("Ingrese nombre y apellido: ")

        usuarios[user] = (clave,nombre,perfil)

        print()
        print("Usuario agregado de forma correcta.")
        print()

        return
    elif aux==0:
        return
    

def eliminar_usuario(usuarios):
    print("ELIMINAR UN USUARIO")
    print()
    user = input("Ingrese el nombre del usuario a eliminar o 0 para salir: ")
    
    if user == "0":
        return

    else:

        if user in usuarios:
            print("Usuario seleccionado: ", user)
            aux = int(input("Se va a eliminar el usuario seleccionado. Para confirmar ingrese 1. Para cancelar ingrese 0. "))
            while aux<0 or aux>1:
                print("Opción inválida. Vuelva a intentar.")
                aux = int(input("Se va a eliminar el usuario seleccionado. Para confirmar ingrese 1. Para cancelar ingrese 0. "))
            if aux==0:
                return
            else:
                user_eliminado=usuarios.pop(user)
                print("Se eliminó el usuario: ", user_eliminado)
        else:
                print("Usuario no encontrado.")
    return

            