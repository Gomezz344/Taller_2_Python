def saludar(nombre, hora):
    if 5 <= hora <= 12:
        saludo = "Buenos días"
    elif 13 <= hora <= 19:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"
    print(f"{saludo}, {nombre}!")

nombre = input("Ingresa tu nombre: ")
hora = int(input("Ingresa la hora (0-23): "))
saludar(nombre, hora)