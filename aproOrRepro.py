# Solicitamos al usuario que ingrese una nota
note = int(input("Ingrese la nota: "))

# Evaluamos la nota
if 0 <= note < 60:
    # Si la nota está entre 0 y 59, el usuario reprobó
    print("Lo siento, reprobaste")
elif 60 <= note <= 100:
    # Si la nota está entre 60 y 100, el usuario aprobó
    print("Felicidades, aprobaste")
else:
    # Si la nota no está en el rango 0-100, es inválida
    print("Nota invalida")
