"""
This file contains logic interact with the user
"""
import user_service

def get_user():
    """
    """
    username = input("Ingrese el username: ")
    response = user_service.get_user(username)
    if response:
        print(response)
    else:
        print(f"El usuario {username} no esta registrado")


def menu():
    message = """\
    Seleccione una opcion

    1. Obtener informacion de un usuario
    2. Obtener usuarios
    3. Crear usuario
    4. Actualizar informacion del usuario
    5. Salir
    """
    print(message)


def main():
    """
    """
    flag = True
    user_service.user_repository.load_users()
    while flag:
        menu()
        option = input("Opcion: ")

        if option == "1":
            get_user()
        elif option == "5":
            flag = False
        else:
            print("opcion no valida")


if __name__ == "__main__":
    main()