def area_cuadrado():
    """Pide al usuario el lado de un cuadrado y calcula su área."""
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))

    if lado <= 0:
        print(" El valor del lado debe ser un número positivo.")
        return
    
    area = lado ** 2
    print(f" El área del cuadrado con lado {lado} es: {area}")