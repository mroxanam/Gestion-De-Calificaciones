# Diccionario de usuarios y contraseñas
usuarios = {
    'profesor1': 'contraseña1',
    'profesor2': 'contraseña2'
}

# Diccionario de calificaciones
calificaciones = {}

def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        return usuario
    else:
        print("Usuario o contraseña incorrectos.")
        return None

def agregar_nota():
    alumno = input("Ingrese el nombre del alumno: ")
    nota = float(input("Ingrese la nota: "))
    
    calificaciones[alumno] = nota
    print("Nota agregada exitosamente.")

def borrar_nota():
    alumno = input("Ingrese el nombre del alumno: ")
    
    if alumno in calificaciones:
        del calificaciones[alumno]
        print("Nota eliminada exitosamente.")
    else:
        print("El alumno no tiene una nota registrada.")

def calcular_promedio():
    if calificaciones:
        total_notas = sum(calificaciones.values())
        cantidad_alumnos = len(calificaciones)
        promedio = total_notas / cantidad_alumnos
        print(f"El promedio de notas es: {promedio}")
    else:
        print("No hay alumnos registrados.")

def asignar_condicion():
    alumno = input("Ingrese el nombre del alumno: ")
    
    if alumno in calificaciones:
        nota = calificaciones[alumno]
        if nota >= 7.0:
            condicion = "Promoción"
        elif nota >= 4.0:
            condicion = "Regular"
        else:
            condicion = "Libre"
        
        print(f"La condición de {alumno} es: {condicion}")
    else:
        print("El alumno no tiene una nota registrada.")

def ver_lista_alumnos():
    if calificaciones:
        print("Lista de Alumnos:")
        for alumno in calificaciones:
            print(alumno)
    else:
        print("No hay alumnos registrados.")

def profesor_menu(profesor):
    while True:
        print("\n--- Menú del Profesor ---")
        print("1. Agregar nota")
        print("2. Borrar nota")
        print("3. Calcular promedio")
        print("4. Asignar condición")
        print("5. Ver lista de alumnos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_nota()
        elif opcion == '2':
            borrar_nota()
        elif opcion == '3':
            calcular_promedio()
        elif opcion == '4':
            asignar_condicion()
        elif opcion == '5':
            ver_lista_alumnos()
        elif opcion == '6':
            print("Sesión finalizada.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def main():
    profesor = iniciar_sesion()
    
    if profesor:
        print("Inicio de sesión exitoso.")
        profesor_menu(profesor)

main()
