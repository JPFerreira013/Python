# Solicitar al usuario un número de inicio y un número final
inicio = int(input("Ingrese un número de inicio: "))
final = int(input("Ingrese un número final: "))
# Usar un bucle for y la función range() para imprimir los números desde inicio hasta final
if final >= inicio:
    i=1
else:
    i=-1  
for numero in range(inicio, final + i, i):
    print(numero)