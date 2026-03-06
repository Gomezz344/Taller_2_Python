numeros = []
sin_dup = []

for i in range(10):
    n = int(input(f"Número {i+1}: "))
    numeros.append(n)

for n in numeros:
    encontrado = False
    for x in sin_dup:
        if x == n:
            encontrado = True
    if not encontrado:
        sin_dup.append(n)

print("Lista original:      ", numeros)
print("Sin duplicados:", sin_dup)