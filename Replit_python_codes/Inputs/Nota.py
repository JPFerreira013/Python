while True:
    nota = float(input("¿Cuál es tu nota? "))
    if nota >= 0 and nota <= 10:
        break
    else:
        print("Error: La nota no puede ser un número negativo o mayor que 10. Por favor, intenta nuevamente.")
if nota >= 9:
    print("Sobre")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
print ("¡Tenga un buen día!")