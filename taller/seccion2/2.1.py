edad = int(input("Ingrese su edad: "))

if edad <= 12: 
    print("Usted es un niño.")
elif edad <= 17:
    print("Usted es un adolescente.")
elif edad <= 64:
    print("Usted es un adulto.")
else:
    print("Usted es un adulto mayor.")