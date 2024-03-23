# Función para registrar un nuevo usuario
def registrar_usuario(base_de_datos):
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    base_de_datos[nombre_usuario] = contraseña
    print("Usuario registrado con éxito.")

# Función para mostrar la información de todos los usuarios
def mostrar_usuarios(base_de_datos):
    print("Lista de usuarios registrados:")
    for usuario, contraseña in base_de_datos.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

# Función para realizar el login de un usuario
def login(base_de_datos):
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if nombre_usuario in base_de_datos and base_de_datos[nombre_usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def main():
    base_de_datos = {}  # Diccionario para almacenar usuarios y contraseñas

    while True:
        print("\nBienvenido al sistema de registro y login.")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Login")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(base_de_datos)
        elif opcion == "2":
            mostrar_usuarios(base_de_datos)
        elif opcion == "3":
            login(base_de_datos)
        elif opcion == "4":
            print("Gracias por utilizar nuestro sistema.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
