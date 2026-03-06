correo = input("Ingrese su correo: ")

if "@" in correo and "." in correo and correo.index("@") < correo.rindex("."):
    print("Correo valido.")
else:
    print("Correo incorrecto")
