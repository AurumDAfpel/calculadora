def area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))

    if radio <= 0:
        print("El radio debe ser un número positivo.")
        return
    
    pi = 3.1416
    area = pi * (radio ** 2)
    print(f"El área del círculo con radio {radio} es: {area:.2f}")
