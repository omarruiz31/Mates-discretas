#Identificador de numeros perfectos

def es_numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

numero = int(input("Ingresa un número:"))

if es_numero_perfecto(numero):
    print(numero, "Es un número perfecto.")
else:
    print(numero, "No es un número perfecto.")
