def calcular_promedio(lista):
    if len(lista) == 0:
        return "Error: la lista está vacía"
    suma = 0
    for n in lista:
        suma += n
    return suma / len(lista)

numeros = []
while True:
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
    if entrada == 'fin':
        break
    numeros.append(float(entrada))

print("Promedio:", calcular_promedio(numeros))