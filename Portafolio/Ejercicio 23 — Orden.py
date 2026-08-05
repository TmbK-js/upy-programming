registros = ["100", "abc", "50"]

for r in registros:
    orden = []
    try:
        valor = int(r)
        orden.append("try")
    except ValueError:
        orden.append("except")
    else:
        orden.append("else")
    finally:
        orden.append("finally")
    print(r, "->", orden)

# Output:
# 100 -> ['try', 'else', 'finally']
# abc -> ['except', 'finally']
# 50 -> ['try', 'else', 'finally']
