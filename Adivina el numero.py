#Juego adivina el numero !!

import random
print("Hola bienvenido al juego de adivina el numero ")
numA= random.randrange(100)

#Bucle principal del juego

while True:
    numB=int(input("Adivina el numero!!:"))
    if numA==numB:
        print("ADIVINASTE!!")
        break
    elif numB>numA:
        print("Tu numero es mayor")
    elif numB<numA:
        print("Tu numero es menor")