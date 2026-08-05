def procesar_pedido(stock, cantidad):
    if cantidad <= 0:
        raise ValueError("cantidad debe ser positiva")
    if cantidad > stock:
        raise ValueError(f"faltan {cantidad - stock} unidades")
    return stock - cantidad


pedidos = [(100, 30), (100, 500), (100, 0)]
exitosos = 0

for stock, cantidad in pedidos:
    try:
        procesar_pedido(stock, cantidad)
        exitosos = exitosos + 1
    except ValueError as e:
        print("Rechazado:", e)

print("Exitosos:", exitosos)

# Output:
# Rechazado: faltan 400 unidades
# Rechazado: cantidad debe ser positiva
# Exitosos: 1
