lista = []

while True:
    print("\n1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar lista")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        producto = input("Nombre del producto: ")
        lista.append(producto)

    elif opcion == "2":
        producto = input("Producto a eliminar: ")
        if producto in lista:
            lista.remove(producto)
        else:
            print("El producto no está en la lista.")

    elif opcion == "3":
        print("Lista de compras:")
        for item in lista:
            print("-", item)

    elif opcion == "4":
        break

    else:
        print("Opción inválida.")