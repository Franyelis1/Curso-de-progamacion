#1 Acumulador con interrupción 

suma_total= 0

while True:
    numero=int(input("Introduce un numero para sumar (0 parar parar)"))

    if numero == 0:
         break
    
    suma_total += numero

print(f"La suma total es: {suma_total}")

    