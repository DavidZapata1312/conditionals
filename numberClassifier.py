# Solicitamos al usuario que ingrese un número
num = int(input("Ingrese un numero: "))
# Comenzamos la estructura condicional para evaluar el número ingresado
if num < 0:
    # Si el número es menor que 0, informamos que es negativo
    print("Su numero es negativo")
elif num == 0:
    # Si el número es exactamente 0, informamos que es cero
    print("Su numero es cero")
else:
    # Si no es menor que 0 ni igual a 0, entonces debe ser positivo
    print("Su numero es positivo")
