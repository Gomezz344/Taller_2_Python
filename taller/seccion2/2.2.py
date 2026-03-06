opcion1 = print("1. Saludar")
opcion2 = print("2. Despedirse")
opcion3 = print("3. Salir")
while True:
    try:
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            print("Hola, ¿cómo estás?")
        elif opcion == 2:
            print("Adiós, que tengas un buen día.")
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Error: Ingrese un número válido.")
