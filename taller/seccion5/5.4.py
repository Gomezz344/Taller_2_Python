def es_palindromo(texto):
    limpio = ""
    for c in texto.lower():
        if c.isalpha():
            limpio += c
    return limpio == limpio[::-1]

texto = input("Ingresa un texto: ")
if es_palindromo(texto):
    print("Es palíndromo")
else:
    print("No es palíndromo")