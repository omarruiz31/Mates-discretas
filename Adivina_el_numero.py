#Juego adivina el numero !!

import random
print("Hola bienvenido al juego de adivina el numero ")
numA= random.randrange(100)
eventos=0

#Bucle principal del juego

while True:
    numB=int(input("Adivina el numero!!:"))
    if numA==numB:
        print("ADIVINASTE!!")
        print(f"Fueron necesarios {eventos} intentos")
        break
    elif numB>numA:
        print("Tu numero es mayor")
        eventos+=1
    elif numB<numA:
        print("Tu numero es menor")
        eventos+=1