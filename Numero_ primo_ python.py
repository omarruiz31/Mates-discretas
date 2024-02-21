#Haz un programa que indique si un numero es primo

print("Hola bienvenido al identificador de numeros ")

numero=(int(input("Dame tu numero: ")))
primo=True

for i in range(2,(numero)//2+1):
    if numero%i==0:
        primo=False
        print("Tu nunero no es primo")
        break

if primo :
    print(f"El numero {numero} es primo ")
else:
    print(f"El numero {numero} no es primo")
    