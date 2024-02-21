#Algoritmo del triangulo de pascal hasta n numeros

def imprimir_triangulo_pascal(n):
    triangulo = []
    for i in range(n):
        fila = []
        for j in range(i + 1):
            if j == 0 or j == i:
                fila.append(1)
            else:
                fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
        triangulo.append(fila)

    for fila in triangulo:
        for elemento in fila:
            print(elemento, end=" ")
        print()

numero_filas = int(input("Ingrese el número de filas: "))
imprimir_triangulo_pascal(numero_filas)
