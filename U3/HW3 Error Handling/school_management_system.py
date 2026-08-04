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


# PROCESS & ERROR HANDLING

autenticado = False
usuario_actual = ""

while not autenticado:
    try:
        usuario_input = input("Usuario: ").strip()
        password_input = input("Contraseña: ").strip()

        if usuario_input not in usuarios or usuarios[usuario_input]['password'] != password_input:
            raise KeyError("Credenciales incorrectas. Verifique el usuario y/o la contraseña.")

        autenticado = True
        usuario_actual = usuario_input

    except KeyError as e:
        print(f"Error de acceso: {e}\n")

nombre_actual = usuarios[usuario_actual]['nombre']
rol_actual = usuarios[usuario_actual]['rol']

print(f"\nBienvenido, {nombre_actual} ({rol_actual})\n")


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
    
    edicion_exitosa = False
    
    while not edicion_exitosa:
        try:
            alumno_sel = input("Alumno: ").strip()
            if alumno_sel not in calificaciones:
                raise KeyError(f"El usuario '{alumno_sel}' no existe o no es un alumno registrado.")
            
            materia_sel = input("Materia: ").strip()
            if materia_sel not in materias:
                raise KeyError(f"La materia '{materia_sel}' no pertenece al plan de estudios.")
            
            try:
                nueva_nota = float(input("Nueva calificación: "))
            except ValueError:
                raise ValueError("La calificación debe ser un valor numérico válido (ej. 8.5).")

            if nueva_nota < 0.0 or nueva_nota > 10.0:
                raise ValueError("La calificación debe estar dentro del rango de 0.0 a 10.0.")

            calificaciones[alumno_sel][materia_sel] = nueva_nota
            print("Calificación actualizada con éxito.")
            edicion_exitosa = True

        except (KeyError, ValueError) as e:
            print(f"Error de operación: {e} Reintentando actualización...\n")

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
