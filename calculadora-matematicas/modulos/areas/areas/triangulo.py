def area_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    if base <= 0 or altura <= 0:
        print(" La base y la altura deben ser números positivos.")
        return
    
    area = (base * altura) / 2
    print(f"El área del triángulo con base {base} y altura {altura} es: {area}")