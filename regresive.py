# Pedimos al usuario que ingrese un número positivo
num = int(input("Ingrese un numero positivo: "))

# Verificamos si el número ingresado es válido
if num <= 0:
    # Si el número es 0 o negativo, mostramos un mensaje de error
    print("numero invalido")
else:
    # Si el número es positivo, comenzamos un bucle while
    while num >= 0:
        # Imprimimos el valor actual de num
        print(num)
        # Reducimos num en 1 en cada iteración
        num = num - 1
