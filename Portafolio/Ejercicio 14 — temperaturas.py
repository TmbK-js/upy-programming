#ejercicio 14 archivo contiene temperaturas
#imprimir contenido y decir cual es la mayor

with open("registro.txt","w") as f:
    f.write("18\n20\n30\n40\n35\n")
    
with open("registro.txt", "r") as f:
    lineas = f.readlines()
    
temperaturas = [int(x) for x in lineas]
print("Cantidad", len(temperaturas))
print("Maxima", max(temperaturas))