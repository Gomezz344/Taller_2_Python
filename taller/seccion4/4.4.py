# Solicitar números separados por comas
entrada = input("Ingresa una lista de números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = [float(num) for num in entrada.split(",")]

# Calcular resultados
maximo = max(numeros)
minimo = min(numeros)
suma = sum(numeros)
promedio = suma / len(numeros)

# Mostrar resultados
print("\nResultados:")
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)
print("Suma total:", suma)
print("Promedio:", promedio)