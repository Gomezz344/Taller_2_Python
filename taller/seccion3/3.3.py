# Dada una lista predefinida de nombres, crear un programa que permita al usuario buscar un nombre específico. El algoritmo debe recorrer la lista e indicar si el nombre se encuentra o no en ella, mostrando su posición en caso afirmativo.

lista = ["Emmanuel", "Astrid", "Jorge", "Andres", "Jennifer"]

nombre = input("Ingrese el nombre que desea buscar: ")
encontrado = False
for i in range(len(lista)):
    if lista[i].lower() == nombre.lower():
        print(f"el nombre '{nombre}' se encuentra en la posicion {i} de la lista.")
        encontrado = True
        break
    if not encontrado:
        print(f"El nombre '{nombre}' no se encuentra en la lista.")
        
