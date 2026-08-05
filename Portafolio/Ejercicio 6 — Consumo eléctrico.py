consumo = [19, 22, 25, 27, 24, 21]

promedio = sum(consumo) / len(consumo)
print("Promedio:", promedio)

for hora, valor in enumerate(consumo):
    if valor > promedio:
        print("Hora", hora, "->", valor)

# Output:
# Promedio: 23.0
# Hora 2 -> 25
# Hora 3 -> 27
# Hora 4 -> 24
