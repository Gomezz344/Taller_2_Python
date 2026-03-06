nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad de residencia: ")

if edad >= 0:
    print(f"Hola {nombre} , tienes {edad} años y vives en {ciudad}.")
else:
    print("Ingresa una edad valida.")