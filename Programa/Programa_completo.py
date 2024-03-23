'''Escribe un programa en Python que lleve a cabo las siguientes tareas:
1. Pregunte al usuario si desea introducir datos o realizar una consulta.
2. Si el usuario desea introducir datos se le solicitará la siguiente información y se añadirá a una estructura de datos de tal manera que permita su posterior consulta por DNI:
○ DNI
○ Nombre
○ Apellido 1
○ Apellido 2
3. Si el usuario desea realizar una consulta se le solicitará que introduzca el DNI y se buscará dicho DNI en laestructura datos creada. Si se encuentra una entrada con el DNI indicado se mostrará su nombre yapellidos. Si no se encuentra ninguna entrada con ese DNI se informará al usuario de que no existe.
4. Una vez introducidos los datos o realizada la consulta, el programa deberá volver al paso 1.'''

import json

def leer_usuarios():
    try:
        with open("usuarios.txt", "r") as fichero:
            usuarios = json.load(fichero)
    except FileNotFoundError:
        usuarios = {}
    return usuarios

def guardar_usuarios(usuarios):
    fichero = open("usuarios.txt","w")
    json.dump(usuarios, fichero)
    fichero.close()

def crear_usuario(usuarios):
    dni = input("Dime el DNI: \n")
    nombre = input("Nombre: \n")
    apellido1 = input("Apellido 1: \n")
    apellido2 = input("Apellido 2: \n")
    usuarios[dni] = {
            "nombre": nombre,
            "apellido1": apellido1,
            "apellido2": apellido2
        }
    return usuarios
    print("Datos añadidos correctamente.")
    guardar_usuarios(usuarios)

def buscar_usuario(usuarios):
    dni_consulta = input("Introduce el DNI para la consulta: ")
    if dni_consulta in usuarios:
        usuario = usuarios[dni_consulta]
        print(usuario["nombre"])
        print(usuario["apellido1"])
        print(usuario["apellido2"])
    else:
        print("No existe usuario.")

usuarios = leer_usuarios()
while True:
    print("Desea introducir datos o realizar una consulta?")
    print("1.Introducir datos")
    print("2.Realizar una consulta")
    opcion = input("Tu opción? (1 o 2): ")
    if opcion == "1":
        crear_usuario(usuarios)
    elif opcion == "2":
        leer_usuarios(usuarios)
        buscar_usuario(usuarios)
    else:
        print("Opción inválida. Por favor, elige 1 o 2.")