def menu():
    print("* MENU PRINCIPAL *")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")
opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("opcion: "))
    if opcion == 1:
        print("registrar()")
    elif opcion == 2:
        print("eliminar()")
    elif opcion == 3:
        print("editar()")
    elif opcion == 4:
        print("listar()")
    elif opcion == 5:
        print("#salir()")
    else:
        print("error()")
import sqlite3

# Conectar a la base de datos (esto creará un archivo si no existe)
conn = sqlite3.connect('Isla_almacen.db')

# Crear un cursor
cursor = conn.cursor()

# Definir la consulta SQL para crear la tabla
create_table_query = '''
CREATE TABLE producto (
    idproducto INTEGER,
    codigo INTEGER,
    nombre TEXT,
    precio INTEGER
);
'''

# Ejecutar la consulta para crear la tabla
cursor.execute(create_table_query)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()