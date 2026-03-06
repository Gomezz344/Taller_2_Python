# Implementar un algoritmo que permita al usuario ingresar números de manera continua. El programa debe sumar todos los números ingresados hasta que el usuario ingrese el valor 0, momento en el cual mostrará la suma total acumulada.

suma = 0

while True:
    try:
        numero = float(input("Ingrese un número (O para finalizar): "))
        if numero == 0:
            break
        suma += numero

    except ValueError:
        print("Error: Ingrese un número válido.")
        
print(f"La suma total acumulada es: {suma}")