#16 lista de productos (producto y precio)
#encabezado
#producto precio
#lapiz		8

productos = [("lapiz",8),("borrador",3),("tajador",5),("cuaderno",10)]

with open ("productos.txt","w") as f:
    f.write("producto precio \n")
    for nombre, precio in productos:
        f.write(nombre + " " + str(precio) + "\n")