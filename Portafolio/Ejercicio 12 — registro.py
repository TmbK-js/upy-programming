#ejercicio 12 crear archivo random "" se va a "w" y contendra la linea "inicio de sesion"
#agregar la palabra "cierre de sesion", y mostrar

with open("registro.txt", "w") as f:
    f.write("Inicio de sesion\n")
    
with open("registro.txt", "a") as f:
    f.write("Cierre de sesion\n")
    
with open("registro.txt", "r") as f:
    print(f.read())