print("Ingrese su categoria y monto de compra.")
opcion1 = print("1. A")
opcion2 = print("2. B")
opcion3 = print("3. C")
compra = float(input("Monto de compra: "))
while True:
    try:
        if compra < 0:
            print("Monto de compra no válido. Intente de nuevo.")
            continue
        categoria = int(input("Categoría (A, B o C): "))
        if categoria == 1:
            descuento = compra * 0.20
            total = compra - descuento
            print(f"Su total a pagar es: {round(total, 2)}")
            break
        elif categoria == 2:
            descuento = compra * 0.15
            total = compra - descuento
            print(f"Su total a pagar es: {round(total, 2)}")
            break
        elif categoria == 3:
            descuento = compra * 0.10
            total = compra - descuento
            print(f"Su total a pagar es: {round(total, 2)}")
            break
    except ValueError:
        print("Error: Ingrese un número válido.")
        