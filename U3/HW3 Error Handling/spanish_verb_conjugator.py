# INPUT

pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# PROCESS & ERROR HANDLING

verbo_valido = False

while not verbo_valido:
    try:
        verbo = input("Ingrese verbo: ").strip().lower()
        
        if not verbo.isalpha():
            raise ValueError("El verbo solo debe contener letras (sin números ni caracteres especiales).")
        
        if len(verbo) < 3:
            raise ValueError("El texto ingresado es demasiado corto para ser un verbo en infinitivo.")
        
        terminacion = verbo[-2:]
        
        if terminacion not in terminaciones:
            raise KeyError(f"El verbo debe terminar en 'ar', 'er' o 'ir'. Terminación detectada: '{terminacion}'.")
        
        verbo_valido = True

    except (ValueError, KeyError) as e:
        print(f"Error de entrada: {e} Por favor, intente de nuevo.\n")

raiz = verbo[:-2]
sufijos = terminaciones[terminacion]

# OUTPUT

for i in range(len(pronombres)):
    print(f"{pronombres[i]} {raiz}{sufijos[i]}")
