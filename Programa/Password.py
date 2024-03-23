intentos = 0  # Inicializa el contador de intentos en 0

while intentos < 3:  # Permitir hasta 3 intentos
    password = input("Contraseña?: ")
    if password == "1234":
        print("Contraseña correcta. ¡Bienvenido!")
        break
    else:
        print("Contraseña incorrecta. Intenta nuevamente.")
        intentos = intentos + 1  # Incrementa el contador de intentos
else:
    print("Has alcanzado el límite de intentos. Acceso denegado.")
