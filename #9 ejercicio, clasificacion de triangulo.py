#9 ejercicio, clasificacion de triangulos

a = float(input("Lado A:"))
b = float(input("Lado B:"))
c = float(input("Lado C:"))

if a == b == c:
    print("Equilátero")
elif a == b or b == c or a == c:
    print("Isósceles")
else:
    print("Escaleno")