import random

while True:
    # El programa "piensa" un número entre 1 y 100
    numero_pensado = random.randint(1, 100)
    intentos = 0
    
    while True:
        # Se solicita al usuario que escriba un número
        intento = int(input("Intenta adivinar el número entre 1 y 100: "))
        intentos += 1
        
        # Verificar si el usuario ha acertado el número
        if intento == numero_pensado:
            print(f"¡Correcto! ¡Has adivinado el número en {intentos} intentos!")
            break
        elif intento < numero_pensado:
            print("Demasiado pequeño. Intenta nuevamente.")
        else:
            print("Demasiado grande. Intenta nuevamente.")
    
    # Preguntar al usuario si quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ")
    if jugar_de_nuevo.lower() != 'sí':
        break

print("Gracias por jugar. ¡Hasta luego!")
