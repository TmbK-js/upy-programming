#ejercicio 7 lista de compras de una tienda(name, age)
#loop se entregan como tuplas
#toda persona mayor a 20,y su nombre
records = [("Karla",20),("Juan",18),("Sofia",40),("Francisco",22)]
for name,age in records:
    if age >= 20:
        print(name)