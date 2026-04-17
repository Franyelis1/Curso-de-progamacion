#11 Ejercicio, calculadora basica

numero1 = float(input("numero 1: "))
numero2 = float(input("numero 2: "))
operacion = input("operacion (+, -, *, /): ")

if operacion == "+":
    print(f"Resultado: {numero1 + numero2}")
elif operacion == "-":
    print(f"Resultado: {numero1 - numero2}")
elif operacion == "*":
    print(f"Resultado: {numero1 * numero2}")
elif operacion == "/":
    if n2 != 0:
        print(f"Resultado: {numero1 / numero2}")
    else:
        print("Error: No se puede dividir por cero")
else:
    print("Operador no válido")