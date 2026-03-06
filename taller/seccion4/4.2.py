contactos = {}

while True:
    print("\n--- DIRECTORIO DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Número telefónico: ")
        contactos[nombre] = telefono
        print("Contacto agregado correctamente.")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        if nombre in contactos:
            print("Teléfono:", contactos[nombre])
        else:
            print("Contacto no encontrado.")

    elif opcion == "3":
        nombre = input("Nombre a eliminar: ")
        if nombre in contactos:
            del contactos[nombre]
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")