#Simulador de acceso

contrasena_correcta ="franye123"
intentos = 0

while intentos < 3:
    acceso= input("Introduce la contrasena")

    if acceso == contrasena_correcta:
        print("acceso concedido")
        break

    intentos += 1
    print(f"incorrecto, intentos restantes: {3 - intentos}")

if intentos == 3:
    print("acceso bloqueado")