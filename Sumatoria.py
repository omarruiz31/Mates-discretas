#Suma de potencias hasta N

def potencia(n):
    if n==1:
        return 1
    else:
        for i in range(n):
            return n+n*n
n=int(input("Ingresa un numero"))
print(potencia(n))