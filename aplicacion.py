import sqlite3

def connect_db():
    return sqlite3.connect('Isla_almacen.db')

def registrar():
    nombre = input("Introduce el nombre del producto: ")
    codigo = int(input("Introduce el código del producto: "))
    precio = int(input("Introduce el precio del producto: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO producto (codigo, nombre, precio) VALUES (?, ?, ?)", (codigo, nombre, precio))
    conn.commit()
    conn.close()

    print("Producto registrado con éxito!")

def eliminar():
    codigo = int(input("Introduce el código del producto a eliminar: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE codigo = ?", (codigo,))
    conn.commit()
    conn.close()

    print("Producto eliminado con éxito!")

def editar():
    codigo = int(input("Introduce el código del producto a editar: "))

    conn = connect_db()
    cursor = conn.cursor()
    producto = cursor.execute("SELECT * FROM producto WHERE codigo = ?", (codigo,)).fetchone()

    if producto:
        print(f"Editando producto: {producto[2]}")
        nuevo_nombre = input("Introduce el nuevo nombre (deja en blanco para mantener el actual): ")
        nuevo_precio = input("Introduce el nuevo precio (deja en blanco para mantener el actual): ")

        if nuevo_nombre:
            producto[2] = nuevo_nombre
        if nuevo_precio:
            producto[3] = int(nuevo_precio)

        cursor.execute("UPDATE producto SET nombre = ?, precio = ? WHERE codigo = ?", (producto[2], producto[3], codigo))
        conn.commit()
        print("Producto editado con éxito!")
    else:
        print("Producto no encontrado.")

    conn.close()

def listar():
    conn = connect_db()
    cursor = conn.cursor()
    productos = cursor.execute("SELECT * FROM producto").fetchall()
    conn.close()

    if productos:
        print("Lista de productos:")
        for producto in productos:
            print(f"Código: {producto[1]}, Nombre: {producto[2]}, Precio: {producto[3]}")
    else:
        print("No hay productos registrados.")

def menu():
    print("* MENU PRINCIPAL *")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

opcion = 1
while opcion != 5:
    menu()
    opcion = int(input("opcion: "))
    if opcion == 1:
        registrar()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        editar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        print("# Adiós!")
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")