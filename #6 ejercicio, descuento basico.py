#6 ejercicio, descuento basico

compra = float(input("Monto de la compra:"))
if compra > 100:
    total = compra * 0.85
    print(f" Descuento aplicado! total: ${total}")
else:
    print(f"Sin descuento. total: ${compra}")