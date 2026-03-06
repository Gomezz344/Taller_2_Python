biblioteca = []
ultimo_id = 0


def agregar_libro():
    global ultimo_id
    titulo = input("Título: ")
    autor = input("Autor: ")
    while True:
        anio = input("Año de publicación: ")
        if anio.isdigit() and int(anio) > 1900:
            break
        print("⚠️  El año debe ser numérico y mayor a 1900.")
    ultimo_id += 1
    biblioteca.append({
        "id": ultimo_id,
        "titulo": titulo,
        "autor": autor,
        "anio": int(anio),
        "disponible": True
    })
    print(f"✅ Libro agregado con ID {ultimo_id}.")


def mostrar_libros():
    if not biblioteca:
        print("No hay libros registrados.")
        return
    for libro in biblioteca:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['anio']}) [{estado}]")


def buscar_libro():
    termino = input("Buscar por título o autor: ").lower()
    resultados = []
    for libro in biblioteca:
        if termino in libro["titulo"].lower() or termino in libro["autor"].lower():
            resultados.append(libro)
    if not resultados:
        print("No se encontraron coincidencias.")
    for libro in resultados:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['anio']}) [{estado}]")


def prestar_libro():
    id_libro = int(input("ID del libro a prestar: "))
    for libro in biblioteca:
        if libro["id"] == id_libro:
            if libro["disponible"]:
                libro["disponible"] = False
                print("✅ Libro prestado exitosamente.")
            else:
                print("⚠️  El libro ya está prestado.")
            return
    print("❌ No se encontró el libro.")


def devolver_libro():
    id_libro = int(input("ID del libro a devolver: "))
    for libro in biblioteca:
        if libro["id"] == id_libro:
            libro["disponible"] = True
            print("✅ Libro devuelto exitosamente.")
            return
    print("❌ No se encontró el libro.")


def eliminar_libro():
    id_libro = int(input("ID del libro a eliminar: "))
    for libro in biblioteca:
        if libro["id"] == id_libro:
            if not libro["disponible"]:
                print("⚠️  No se puede eliminar un libro prestado.")
                return
            biblioteca.remove(libro)
            print("✅ Libro eliminado.")
            return
    print("❌ No se encontró el libro.")


def libros_por_autor():
    autor = input("Nombre del autor: ").lower()
    encontrados = False
    for libro in biblioteca:
        if autor in libro["autor"].lower():
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"ID: {libro['id']} - '{libro['titulo']}' ({libro['anio']}) [{estado}]")
            encontrados = True
    if not encontrados:
        print("No se encontraron libros de ese autor.")


def estadisticas():
    total = len(biblioteca)
    disponibles = sum(1 for libro in biblioteca if libro["disponible"])
    prestados = total - disponibles
    print(f"📚 Total de libros  : {total}")
    print(f"✅ Disponibles      : {disponibles}")
    print(f"📤 Prestados        : {prestados}")


def exportar_a_txt():
    with open("biblioteca.txt", "w", encoding="utf-8") as f:
        for libro in biblioteca:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            f.write(f"ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['anio']}) [{estado}]\n")
    print("✅ Biblioteca exportada a 'biblioteca.txt'.")


def menu_principal():
    while True:
        print("""
=== BIBLIOTECA ===
1. Agregar libro
2. Mostrar libros
3. Buscar libro
4. Prestar libro
5. Devolver libro
6. Eliminar libro
7. Libros por autor
8. Estadísticas
9. Exportar a TXT
0. Salir""")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            mostrar_libros()
        elif opcion == '3':
            buscar_libro()
        elif opcion == '4':
            prestar_libro()
        elif opcion == '5':
            devolver_libro()
        elif opcion == '6':
            eliminar_libro()
        elif opcion == '7':
            libros_por_autor()
        elif opcion == '8':
            estadisticas()
        elif opcion == '9':
            exportar_a_txt()
        elif opcion == '0':
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción inválida.")


menu_principal()