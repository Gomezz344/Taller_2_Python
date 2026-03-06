# Ingresar listas
lista1 = input("Ingresa los elementos de la primera lista separados por comas: ").split(",")
lista2 = input("Ingresa los elementos de la segunda lista separados por comas: ").split(",")

# Quitar espacios extra
for i in range(len(lista1)):
    lista1[i] = lista1[i].strip()

for i in range(len(lista2)):
    lista2[i] = lista2[i].strip()

comunes = []
unicos_lista1 = []
unicos_lista2 = []

# Buscar elementos comunes y únicos de la primera lista
for elemento in lista1:
    if elemento in lista2:
        if elemento not in comunes:
            comunes.append(elemento)
    else:
        unicos_lista1.append(elemento)

# Buscar elementos únicos de la segunda lista
for elemento in lista2:
    if elemento not in lista1:
        unicos_lista2.append(elemento)

# Mostrar resultados
print("\nElementos comunes:", comunes)
print("Elementos únicos de la primera lista:", unicos_lista1)
print("Elementos únicos de la segunda lista:", unicos_lista2)