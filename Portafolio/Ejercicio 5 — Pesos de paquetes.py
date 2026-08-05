pesos = [12, 5, 20, 5, 8, 20, 5]

print("Veces que aparece el peso 5:", pesos.count(5))
print("Indice del primer paquete de 20:", pesos.index(20))

pesos.remove(5)
print("Lista despues de quitar un 5:", pesos)
print("Orden descendente:", sorted(pesos, reverse=True))

# Output:
# Veces que aparece el peso 5: 3
# Indice del primer paquete de 20: 2
# Lista despues de quitar un 5: [12, 20, 5, 8, 20, 5]
# Orden descendente: [20, 20, 12, 8, 5, 5]
