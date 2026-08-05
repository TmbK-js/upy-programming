import logging

logger = logging.getLogger("proceso")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("errores.log", mode="w")
handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
logger.addHandler(handler)

lecturas = ["21", "35", "xx", "40"]
validas = 0

for x in lecturas:
    try:
        int(x)
        validas = validas + 1
    except ValueError:
        logger.error(f"lectura invalida: {x}")

handler.flush()

with open("errores.log") as f:
    print(f.read())

print("Lecturas validas:", validas)

# Output:
# ERROR - lectura invalida: xx
#
# Lecturas validas: 3
