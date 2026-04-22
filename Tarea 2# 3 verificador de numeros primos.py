#verificador de numeros primos

numero = int(input("introduce un numero:"))

if numero < 2:
    print(f"{numero} no es un numero primo")
else:
    for i in range (2,numero):
        if numero % i == 0:
            print(f"{numero} no es primo")
            break
    else:
        print(f"{numero} es primo")
        