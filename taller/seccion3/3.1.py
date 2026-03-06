# Crear un programa que solicite al usuario un número entero positivo N y muestre todos los números pares desde 1 hasta N utilizando un ciclo for.

Natural = int(input("Ingrese un número natural: "))

for i in range(1, Natural + 1):
    if i % 2 == 0:
        print(i)