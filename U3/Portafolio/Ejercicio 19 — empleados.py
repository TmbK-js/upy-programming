#ejercicio 19 empleados.csv = juan1000
#nombre, sueldo y fila por empleado
#calcular la suma de todos los sueldos
import csv

with open("empleados.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["nombre","sueldo"])
    w.writerow(["ana",1000])
    w.writerow(["jorge",500])
    w.writerow(["rodrigo",700])
    w.writerow(["didier",10000])
    w.writerow(["francisco",600])
    
total = 0
with open("empleados.csv","r") as f:
    for fila in csv.DictReader(f):
        total = total + int(fila["sueldo"])
print(total)