#10 ejercicio, el mayor de tres numeros

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c
print(f"El mayor es {mayor}")