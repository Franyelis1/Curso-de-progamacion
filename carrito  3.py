carrito = []
precios = []
total = []

print("--- Tienda ---")
print("Producto: 'total' para pagar, 'ver' para revisar, 'salir' para cancelar.")

while True:
    producto = input("Producto: ").lower()

    if producto == 'salir':
        print("Compra cancelada")
        break
    
    elif producto == 'ver':
        if len(carrito) == 0:
            print("El carrito esta vacio.")
        else:
            print(f"Tu carrito actual: {carrito}")
            
    elif producto == 'total':
        
        total = sum(precios)
        print("--- TICKET  ---")
        
        indice = 0
        while indice < len(carrito):
            print(f"- {carrito[indice]}: ${precios[indice]}")
            indice += 1
            
        print(f"TOTAL: ${total}")
        print("Gracias por su compraa")
        break
    
    else:
       
        precio_texto = input(f"Precio de {producto}: ")
        
       
        precio_numero = float(precio_texto)
        
    
        carrito.append(producto)
        precios.append(precio_numero)
        print(f" Agregado: {producto}")
