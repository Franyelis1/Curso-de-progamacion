#5 ejercicio,el mayor de dos numeros

numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))
if numero1 > numero2:
    print(f"{numero1} es el mayor")
elif numero2 > numero1:
    print(f"{numero2} es el mayor")
else:
    print("Son iguales")