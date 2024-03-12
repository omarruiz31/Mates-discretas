#Escribe un programa que dado un número entero n indique todos los números primos de 2 a n
def numeros_primos_hasta_n(n):
    primos = []
    for num in range(2, n + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

try:
    limite_superior = int(input("Ingrese un número entero positivo: "))
    if limite_superior < 2:
        print("Por favor, ingrese un número entero positivo mayor o igual a 2.")
    else:
        print("Los números primos hasta", limite_superior, "son:")
        print(numeros_primos_hasta_n(limite_superior))
except ValueError:
    print("Por favor, ingrese un número entero válido.")
