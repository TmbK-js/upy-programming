#ejercicio 13 copia el contenido de una archivo a otro
#1 - Contener 3 lineas
#2 - Luego copiar
#3 - Imprimir
with open("registro.txt","w") as f:
    f.write("linea1\nlinea2\nlinea3\n")
    
with open("registro.txt","r") as origen, open("copia.txt","w") as destino:
    for linea in origen:
        destino.write(linea)

with open("copia.txt", "r") as f:
    print(f.read())