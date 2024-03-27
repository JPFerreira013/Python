usuarios = {"david":"2234",
           "joao":"1223",
            "Carlos":"1475",
            "Maria":"5236"
           }
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