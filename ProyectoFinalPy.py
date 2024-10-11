def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar usuario y clave")
    print("2. Mostrar todos los usuarios y sus claves")
    print("3. Iniciar sesión")
    print("4. Salir")

def registrar_usuario(bdd_usuarios):
    usuario = input("\nIngrese un nombre de usuario: ")
    if usuario in bdd_usuarios:
        print("El nombre de usuario ya existe.")
    else:
        clave = input("Ingrese una contraseña: ")
        bdd_usuarios[usuario] = clave
        guardar_datos(bdd_usuarios)
        print("\n*************************************************")
        print("Usuario registrado exitosamente.")
        print("*************************************************")
    return bdd_usuarios

def mostrar_usuarios(bdd_usuarios):
    if bdd_usuarios:
        print("\n--- Usuarios Registrados ---")
        for usuario, clave in bdd_usuarios.items():
            print(f"Usuario: {usuario}") #Puedo agregar la clave -> ", Clave: {clave}"
    else:
        print("No hay usuarios registrados.")

def iniciar_sesion(bdd_usuarios):
    usuario = input("Ingrese el nombre de usuario: ")
    clave = input("Ingrese la contraseña: ")
    if usuario in bdd_usuarios and bdd_usuarios[usuario] == clave:
        
        print("\nInicio de sesión exitoso.\n")
        return True
    else:
        print("\nUsuario o contraseña incorrectos.\n")
        return False

def guardar_datos(bdd_usuarios, archivo='BDD.json'):
    with open(archivo, 'w') as archivo_json:
        json.dump(bdd_usuarios, archivo_json, indent=4)

#------ MAIN -----
import json
bdd_usuarios = {} 

while True:
    mostrar_menu()
    print("")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == '1':
        bdd_usuarios = registrar_usuario(bdd_usuarios)
    elif opcion == '2':
        mostrar_usuarios(bdd_usuarios)
    elif opcion == '3':
        if iniciar_sesion(bdd_usuarios):
            break
    elif opcion == '4':
        print("\nUsted salio del programa. Para reingresar inicie nuevamente!\n")
        break 
    else:
        print("\nERROR!!!!! Elija una opción entre 1 y 4.\n")

