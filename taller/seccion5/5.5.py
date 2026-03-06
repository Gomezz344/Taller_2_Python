def factorial(n):
    if n < 0:
        return "Error: no existe factorial de números negativos"
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Ingresa un número: "))
print(f"{n}! =", factorial(n))