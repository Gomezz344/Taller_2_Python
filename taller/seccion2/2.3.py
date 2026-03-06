opcion1 = print("1. Sumar")
opcion2 = print("2. Restar")
opcion3 = print("3. Multiplicar")
opcion4 = print("4. Dividir")
opcion5 = print("5. Salir")

while True:
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 5:
            break

        if opcion == 1:
            num1 = float(input("Ingrese su primer número: "))
            num2 = float(input("Ingrese su segundo número: "))
            operacion = "+"
        elif opcion == 2:
            num1 = float(input("Ingrese su primer número: "))
            num2 = float(input("Ingrese su segundo número: "))
            operacion = "-"
        elif opcion == 3:
            num1 = float(input("Ingrese su primer número: "))
            num2 = float(input("Ingrese su segundo número: "))
            operacion = "*"
        elif opcion == 4:
            num1 = float(input("Ingrese su primer número: "))
            num2 = float(input("Ingrese su segundo número: "))
            operacion = "/"
        else:
            print("Opción no válida. Intente de nuevo.")
            continue
        
        if operacion == "+":
            resultado = num1 + num2
            print("Su suma es: ", resultado)
        elif operacion == "-":
            resultado = num1 - num2
            print("Su resta es: ", resultado)
        elif operacion == "*":
            resultado = num1 * num2
            print("Su multiplicación es: ", resultado)
        elif operacion == "/":
            if num2 == 0:
                print("No se puede divir por 0")
                continue
            resultado = num1 / num2
            print("Su división es: ", resultado)
    except ValueError:
        print("Ingrese numeros validos.")            

