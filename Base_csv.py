import csv


def cargar_alumno():
    # Usuarios existentes
    usuarios = []
    with open(db_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios.append(row)
    return usuarios

def guardar_alumnos(alumnos):
    # Guardar cambios
    with open(db_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(alumnos)

def crear_alumno(alumno):
    alumnos = cargar_alumno()
    alumnos.append(alumno)
    guardar_alumnos(alumnos)

#Buscar
def obtener_alumno_por_boleta(boleta):
    alumnos = cargar_alumno()
    for alumno in alumnos:
        if alumno['boleta'] == boleta:
            return alumno
    return None
# modificar
def actualizar_alumno(boleta, nuevos_datos):
    alumnos = cargar_alumno()
    for alumno in alumnos:
        if alumno['boleta'] == boleta:
            alumno.update(nuevos_datos)
            guardar_alumnos(alumnos)
            return True
    return False
#Eliminar
def eliminar_alumno(boleta):
    alumnos = cargar_alumno()
    for alumno in alumnos:
        if alumno['boleta'] == boleta:
            alumnos.remove(alumno)
            guardar_alumnos(alumnos)
            return True
    return False

#visualizar
def mostrar_alumnos():
    alumnos = cargar_alumno()
    if alumnos:
        for alumno in alumnos:
            print(f"Boleta: {alumno['boleta']}, Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Email: {alumno['email']}")
    else:
        print("No hay alumnos registrados.")


# Ruta del archivo CSV 
db_file = 'usuarios.csv'
campos = ['boleta', 'nombre', 'edad', 'email']

def mi_menu():
    print("**********MENU ESCOLAR ESCOLAR IPN *************")
    print("1. Dar de alta nuevo alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno por boleta")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Salir")

def principal():
    while True:
        mi_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            boleta = input("Ingrese el boleta del alumno: ")
            nombre = input("Ingrese el nombre del alumno: ")
            edad = input("Ingrese la edad del alumno: ")
            email = input("Ingrese el correo electrónico del alumno: ")
            nuevo_alumno = {
                'boleta': boleta,
                'nombre': nombre,
                'edad': edad,
                'email': email
            }
            crear_alumno(nuevo_alumno)
            print("Usuario Nuevo dado de alta")

        elif opcion == "2":
            mostrar_alumnos()

        elif opcion == "3":
            boleta = input("Ingrese el Boleta del alumno a buscar: ")
            alumno_obtenido = obtener_alumno_por_boleta(boleta)
            if alumno_obtenido:
                print(f"Boleta: {alumno_obtenido['boleta']}, Nombre: {alumno_obtenido['nombre']}, Edad: {alumno_obtenido['edad']}, Email: {alumno_obtenido['email']}")
            else:
                print('No se encontró el alumno.')

        elif opcion == "4":
            boleta = input("Ingrese la boleta del alumno a modificar: ")
            nuevos_datos = {}
            nombre = input("Ingrese el nuevo nombre del alumno (si no va realizar cambios de enter): ")
            if nombre:
                nuevos_datos['nombre'] = nombre
            edad = input("Ingrese la nueva edad del alumno (si no va realizar cambios de enter): ")
            if edad:
                nuevos_datos['edad'] = edad
            email = input("Ingrese el nuevo correo electrónico del alumno (si no va realizar cambios de enter): ")
            if email:
                nuevos_datos['email'] = email
            if actualizar_alumno(boleta, nuevos_datos):
                print('Alumno actualizado exitosamente.')
            else:
                print('No se encontró el alumno para actualizar.')

        elif opcion == "5":
            boleta = input("Ingrese la Boleta del alumno a eliminar: ")
            if eliminar_alumno(boleta):
                print('Alumno eliminado exitosamente.')
            else:
                print('No se encontró el alumno para eliminar.')

        elif opcion == "6":
            break

        else:
            print("Opción incorrecta.")

if __name__ == '__main__':
    principal()
#RJN