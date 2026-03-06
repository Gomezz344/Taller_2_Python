calificacion = int(input("Ingrese su calificación: "))

if calificacion >= 90:
    print("Su calificacion es A.")
elif calificacion >= 80:
    print("Su calificacion es B.")
elif calificacion >= 70:
    print("Su calificacion es C.")
elif calificacion >= 60:
    print("Su calificacion es D.")
elif calificacion >= 0:
    print("Su calificacion es F.")
else:
    print("Calificación no válida.")
    