while True:
    edad = int(input("¿Cuál es tu edad? "))
    if edad >= 0:
        break
    else:
        print("Error: La edad no puede ser un número negativo. Por favor, intenta nuevamente.")

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
