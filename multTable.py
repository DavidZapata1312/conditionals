# Pedimos al usuario que ingrese un número para generar su tabla de multiplicar
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Mostramos un encabezado para la tabla
print(f"\nTabla de multiplicar del {numero}:\n")

# Usamos un bucle for para recorrer los números del 1 al 10
for i in range(1, 11):
    # Calculamos el resultado de multiplicar el número ingresado por el valor actual de i
    resultado = numero * i
    # Imprimimos la multiplicación en formato bonito
    print(f"{numero} x {i} = {resultado}")
