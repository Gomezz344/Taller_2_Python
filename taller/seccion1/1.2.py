
while True:
    try:
        num1 = float(input("Ingrese su primer número: "))
        num2 = float(input("Ingrese su segundo número: "))
        operacion = input("Ingrese la operación (+,-,*,/): ")

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
        else:
            print("Operación no valida.")
    except ValueError:
        print("Ingrese numeros validos.")            

