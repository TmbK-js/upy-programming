operaciones = [("8", "2"), ("9", "0"), ("a", "3"), ("6", "3")]

validas = 0
ceros = 0
invalidas = 0

for a, b in operaciones:
    try:
        int(a) / int(b)
        validas = validas + 1
    except ValueError:
        invalidas = invalidas + 1
    except ZeroDivisionError:
        ceros = ceros + 1

print("Validas:", validas)
print("Division entre cero:", ceros)
print("Datos invalidos:", invalidas)

# Output:
# Validas: 2
# Division entre cero: 1
# Datos invalidos: 1
