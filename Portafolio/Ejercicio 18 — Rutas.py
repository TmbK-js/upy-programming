#18 archivo.png construir un respaldo = respaldos (.bak)
#Verificar si existe el archivo o no
import os/

archivo = "foto.png"
nombre, ext = os.path.splitext(archivo)
respaldo = os.path.join("respaldo", nombre + ".bak")
print("respaldos", respaldo)
print("original: ", os.path.exists(archivo))