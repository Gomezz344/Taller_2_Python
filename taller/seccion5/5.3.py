def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

while True:
    print("\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == '5':
        break

    a = float(input("Número 1: "))
    b = float(input("Número 2: "))

    if opcion == '1':
        print("Resultado:", sumar(a, b))
    elif opcion == '2':
        print("Resultado:", restar(a, b))
    elif opcion == '3':
        print("Resultado:", multiplicar(a, b))
    elif opcion == '4':
        print("Resultado:", dividir(a, b))
    else:
        print("Opción inválida")