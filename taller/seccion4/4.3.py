productos = [
    {"nombre": "Manzana", "precio": 1.5, "stock": 50},
    {"nombre": "Pan", "precio": 2.0, "stock": 30},
    {"nombre": "Leche", "precio": 1.8, "stock": 20}
]

nombre_buscar = input("Ingrese el nombre del producto a actualizar: ")

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        producto["precio"] = nuevo_precio
        print("Precio actualizado correctamente.")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")

print("\nLista actualizada de productos:")
for p in productos:
    print(p)