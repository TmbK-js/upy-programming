#ejercicio 20 tienda.csv = producto, unidades y precio
#generar un nuevo archivo reporte.csv (igual a la tienda.csv)
#agregar una nueva columna "total" = unidades * precio por cada fila

import csv

with open("tienda.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["Producto", "Unidades", "Precio"])
    w.writerow(["Clavos", "10", "1"])
    w.writerow(["Tornillos", "20", "2"])
    w.writerow(["Pernos", "5", "10"])
    
with open("tienda.csv","r") as entrada, open ("reporte.csv","w",newline="") as salida:
    s = csv.DictReader(entrada)
    e = csv.DictWriter(salida, fieldnames=["Producto","Unidades","Precio","total"])
    e.writeheader()
    for fila in s:
        fila["total"] = int(fila["Unidades"]) * int(fila["Precio"])
        e.writerow(fila)
        
with open("reporte.csv","r") as f:
    print(f.read())