import csv


def cargar_usuarios():
    # Usuarios existentes
    usuarios = []
    with open(db_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios.append(row)
    return usuarios

def guardar_usuarios(usuarios):
    # Guardar cambios
    with open(db_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(usuarios)

def crear_usuario(usuario):
    usuarios = cargar_usuarios()
    usuarios.append(usuario)
    guardar_usuarios(usuarios)

#Buscar
def obtener_usuario_por_id(boleta):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario['boleta'] == boleta:
            return usuario
    return None
# modificar
def actualizar_usuario(boleta, nuevos_datos):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario['boleta'] == boleta:
            usuario.update(nuevos_datos)
            guardar_usuarios(usuarios)
            return True
    return False
#Eliminar
def eliminar_usuario(boleta):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario['boleta'] == boleta:
            usuarios.remove(usuario)
            guardar_usuarios(usuarios)
            return True
    return False

#visualizar
def mostrar_usuarios():
    usuarios = cargar_usuarios()
    if usuarios:
        for usuario in usuarios:
            print(f"Boleta: {usuario['boleta']}, Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Email: {usuario['email']}")
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
            nuevo_usuario = {
                'boleta': boleta,
                'nombre': nombre,
                'edad': edad,
                'email': email
            }
            crear_usuario(nuevo_usuario)
            print("Usuario Nuevo dado de alta")

        elif opcion == "2":
            mostrar_usuarios()

        elif opcion == "3":
            boleta = input("Ingrese el Boleta del alumno a buscar: ")
            usuario_obtenido = obtener_usuario_por_id(boleta)
            if usuario_obtenido:
                print(f"Boleta: {usuario_obtenido['boleta']}, Nombre: {usuario_obtenido['nombre']}, Edad: {usuario_obtenido['edad']}, Email: {usuario_obtenido['email']}")
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
            if actualizar_usuario(boleta, nuevos_datos):
                print('Alumno actualizado exitosamente.')
            else:
                print('No se encontró el alumno para actualizar.')

        elif opcion == "5":
            boleta = input("Ingrese la Boleta del alumno a eliminar: ")
            if eliminar_usuario(boleta):
                print('Alumno eliminado exitosamente.')
            else:
                print('No se encontró el alumno para eliminar.')

        elif opcion == "6":
            break

        else:
            print("Opción incorrecta.")

if __name__ == '__main__':
    principal()
