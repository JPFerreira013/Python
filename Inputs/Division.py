# Divide dos números
while True:
    try:
        dividendo = int(input('Dividendo?: '))
        divisor = int(input('Divisor?: '))
        resultado = dividendo/divisor
    except ValueError:
        print('Debes introducir un número válido')
    except ZeroDivisionError:
        print('El divisor no puede ser cero')
    except:
        print('Se ha producido un error inesperado')
    else:
        print('Resultado:', resultado)