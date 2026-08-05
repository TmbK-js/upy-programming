#ejercicio15 un archivo que contiene notas y calificaciom y se imprime nombre del que 0=> 8
with open ("notas.txt","w") as f:
    f.write("Ana 9\nLuis 10 \nDaniel 7 \nJesus 4 \nJose 8\n")
    
with open ("notas.txt", "r") as f:
    for linea in f:
        nombre, calif = linea.split()
        if int(calif) >= 8:
            print(nombre)