# Importamos el módulo random para generar números aleatorios
import random

# Generamos un número aleatorio entre 1 y 10
numTGuess = random.randint(1, 10)

# Inicializamos el contador de intentos en 0
trys = 0

# Iniciamos un bucle while que permite un máximo de 3 intentos
while trys < 3:
    # Pedimos al usuario que ingrese un número
    answer = int(input("Ingrese un número: "))
    
    # Si el número ingresado es igual al número aleatorio
    if answer == numTGuess:
        # ¡Ganó! Informamos y salimos del bucle con break
        print(f"¡Adivinaste! {numTGuess} es correcto.")
        break  
    # Si el número ingresado es menor que el número a adivinar
    elif answer < numTGuess:
        print("Es un poco mayor.")  # Le damos una pista
    # Si el número ingresado es mayor
    else:
        print("Es un poco menor.")  # Otra pista, pero hacia abajo
    
    # Sumamos 1 intento
    trys += 1  

# Si después de 3 intentos no adivinó, mostramos el número correcto
if trys == 3 and answer != numTGuess:
    print(f"Lo siento, el número correcto era {numTGuess}. ¡Suerte para la próxima!")
 