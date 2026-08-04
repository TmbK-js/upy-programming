# INPUT
verbo = input("Ingrese verbo: ").strip().lower()
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# PROCESS
raiz = verbo[:-2]
terminacion = verbo[-2:]
sufijos = terminaciones[terminacion]

# OUTPUT
for i in range(len(pronombres)):
    pronombres_actual = pronombres[i]
    sufijo_actual = sufijos[i]
    print(f"{pronombres_actual} {raiz}{sufijo_actual}")
