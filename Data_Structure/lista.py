# Crea una lista
lista = []
print(lista)

# Preguntar numero de elementos
num_elementos = int(input("cuantos elementos quiere en tu lista?\n"))

# Para cada elemento - Preguntar el valor
for i in range(1,num_elementos + 1):
    elemento = int(input("Valor elemento " + str(i) + ": \n"))
    lista.append(elemento)

# "" - Añadir elemento a la lista
#lista.append(i)
#lista.insert(i)

# imprimir lista
print(lista)

#ordenar lista
lista.sort()
print(lista)

lista.reverse()
print(lista)