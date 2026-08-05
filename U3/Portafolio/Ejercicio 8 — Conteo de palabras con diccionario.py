#ejercio 8 contar cuantas veces se repite una palabra
#imprimir el resulatado
sentence = "españa es el campeon del mundo y messi el lloron"
counts = {}
for word in sentence.split():
    counts[word] = counts.get(word,0)+1
print(counts)