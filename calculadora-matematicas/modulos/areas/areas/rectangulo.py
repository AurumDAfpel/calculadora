def area_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    if base <= 0 or altura <= 0:
        print("La base y la altura deben ser números positivos.")
        return
    
    area = base * altura
    print(f"El área del rectángulo con base {base} y altura {altura} es: {area}")