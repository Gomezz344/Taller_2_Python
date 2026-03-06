while True:
    n = int(input("¿Qué tabla deseas ver? (1-10): "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    if input("¿Ver otra? (s/n): ") != 's':
        break