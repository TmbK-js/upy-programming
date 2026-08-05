class StockInsuficienteError(Exception):
    def __init__(self, faltan):
        self.faltan = faltan
        super().__init__(f"faltan {faltan} unidades")


def vender(stock, pedido):
    if pedido > stock:
        raise StockInsuficienteError(pedido - stock)
    return stock - pedido


try:
    vender(10, 25)
except StockInsuficienteError as e:
    print("Faltan (atributo):", e.faltan)
    print("Mensaje:", e)

# Output:
# Faltan (atributo): 15
# Mensaje: faltan 15 unidades
