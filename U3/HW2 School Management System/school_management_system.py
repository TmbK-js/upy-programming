# INPUT

usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
    'cgomez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Carlos Gómez'},
    'lhernandez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Lucía Hernández'},
    'pdiaz': {'password': '1234', 'rol': 'alumno', 'nombre': 'Pedro Díaz'},
    'sromero': {'password': '1234', 'rol': 'alumno', 'nombre': 'Sofía Romero'},
    'mlopez': {'password': '1234', 'rol': 'maestro', 'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

materias = ('Matemáticas', 'Programación', 'Inglés')

calificaciones = {
    'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'cgomez': {'Matemáticas': 7.0, 'Programación': 8.5, 'Inglés': 9.0},
    'lhernandez': {'Matemáticas': 9.5, 'Programación': 10.0, 'Inglés': 8.0},
    'pdiaz': {'Matemáticas': 6.5, 'Programación': 7.0, 'Inglés': 8.0},
    'sromero': {'Matemáticas': 8.0, 'Programación': 8.5, 'Inglés': 9.0}
}


# PROCESS

autenticado = False
usuario_actual = ""

while not autenticado:
    usuario_input = input("Usuario: ").strip()
    password_input = input("Contraseña: ").strip()

    if usuario_input in usuarios and usuarios[usuario_input]['password'] == password_input:
        autenticado = True
        usuario_actual = usuario_input
    else:
        print("Credenciales incorrectas. Intente de nuevo.\n")

nombre_actual = usuarios[usuario_actual]['nombre']
rol_actual = usuarios[usuario_actual]['rol']

print(f"Bienvenido, {nombre_actual} ({rol_actual})\n")


# OUTPUT

if rol_actual == 'alumno':
    print(f"Boleta de {nombre_actual}")
    
    aprobadas = set()
    
    for materia in materias:
        nota = calificaciones[usuario_actual][materia]
        print(f"{materia}: {nota}")
        if nota >= 8.0:
            aprobadas.add(materia)
            
    pendientes = set(materias) - aprobadas
    
    print(f"Materias aprobadas: {aprobadas}")
    print(f"Materias pendientes: {pendientes}")

elif rol_actual == 'maestro':
    print("--- Alumnos registrados ---")
    for usr, datos in usuarios.items():
        if datos['rol'] == 'alumno':
            print(f"- {usr}: {datos['nombre']}")
            
    print("\n--- Modificar Calificación ---")
    alumno_sel = input("Alumno: ").strip()
    materia_sel = input("Materia: ").strip()
    nueva_nota = float(input("Nueva calificación: "))
    
    if alumno_sel in calificaciones and materia_sel in materias:
        calificaciones[alumno_sel][materia_sel] = nueva_nota
        print("Calificación actualizada.")
    else:
        print("Error: El usuario o la materia no son válidos.")

elif rol_actual == 'coordinador':
    print("--- REPORTE DE COORDINACIÓN ---")
    
    print("\nMaestros:")
    for usr, datos in usuarios.items():
        if datos['rol'] == 'maestro':
            print(f"- {datos['nombre']}")
            
    print("\nMaterias:")
    for materia in materias:
        print(f"- {materia}")
        
    print("\nAlumnos y Calificaciones:")
    for usr_alumno, notas in calificaciones.items():
        nombre_alumno = usuarios[usr_alumno]['nombre']
        print(f"\n{nombre_alumno} ({usr_alumno}):")
        for materia in materias:
            print(f"  {materia}: {notas[materia]}")
