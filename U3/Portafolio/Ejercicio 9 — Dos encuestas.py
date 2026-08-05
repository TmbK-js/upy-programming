#9 dos encuestas de lenguajes de programación
#se compararan, se imprime lo siguiente
#lo que aparece en ambas, los valores unicos
#intersección y diferencia
set1 = ["python","C","java","c++"]
set2 = ["c++", "c","rubi","go"]
s1 = set(set1)
s2 = set(set2)
print("Ambas listas: ", sorted(s1 & s2))
#sorted sirve para que se ponga en orden y no al azar
print("Valores unicos: ", sorted((s1-s2)|(s2-s1)))9