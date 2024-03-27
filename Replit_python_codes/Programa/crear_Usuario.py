import json

def leer_diccionario():
    fichero = open("usuarios.txt")
    usuarios = json.load(fichero)
    fichero.close()
    return usuarios

def guardar_diccionario(usuarios):
    fichero = open("usuarios.txt","w")
    json.dump(usuarios, fichero)
    fichero.close()

def iniciar_sesion():
    intentos = 0
    while intentos < 3:
            user = input("User Name: \n")
            password = input("Password: \n")
            if user in usuarios and password == usuarios[user]:
                print("Bien Venido")
                break
            else:
                print ("Aceso Denegado")
                intentos = intentos + 1
    else:
        print("Has alcanzado el límite de intentos. Acceso denegado")
def crear_user():
    username = input("Nombre de usuario?: ")
    password = input("Contraseña?: ")
    usuarios[username] = password
    print ("Usuario", username, "creado")

usuarios = leer_diccionario()

print("Selecionar una opción:")
print("1.Crear cuenta")
print("2.Iniciar sesión")
while True: 
    opcion = input("Tu opción ?(1 o 2)")
    if opcion == "1":
        crear_user()
        guardar_diccionario(usuarios)
    elif opcion == "2":
        leer_diccionario()
        iniciar_sesion()
        break
    else:
        print("Denegado")