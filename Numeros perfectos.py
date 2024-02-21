#Identificador de numeros perfectos

#Factorizador
def factores(n):
    factores = []
    for i in range(1, n + 1):
        if n % i == 0:
            factores.append(i)
    return factores

numero = int(input("Ingresa un número para encontrar sus factores: "))
print(factores(numero)[1])