#sensor
sensor = [32,35,40,50,29,25,34,35,37,40,14,12]
morning = sensor[:6] #inicia con cero y acaba con 6
afternoon = sensor[6:] #inicia 6 termina hasta el fondo
sampled = sensor[::3] #toda la lista pero solo agarra 3
print("morning: ", morning)
print("afternoon: ", afternoon)
print("sampled: ", sampled)