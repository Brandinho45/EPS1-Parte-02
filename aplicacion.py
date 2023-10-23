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