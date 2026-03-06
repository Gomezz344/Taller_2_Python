contraseña = input("Ingrese su contraseña, debe tener almenos 8 caracteres, contener almenos una mayuscula, un número y un caracter especial (!@#$%^&*): ")

errores = []

if len(contraseña) < 8:
    errores.append("Debe tener almenos 8 caracteres")

if any(c.isupper() for c in contraseña):
    errores.append("Debe tener almenos una mayuscula.")

if any(c.isdigit() for c in contraseña):
    errores.append("Debe tener almenos un número.")

caracteres_especiales = "!@#$%&*"
if not any(c in caracteres_especiales for c in contraseña):
    errores.append("Debe tener almenos un caracter especial")

if not errores:
    print("Contraseña segura")
else:
    print("La contraseña no cumple uno de los criterios: ")
    for error in errores:
        print("-", error)