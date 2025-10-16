def perimetroTriangulo():
    lado = float(input("ingesa el primer lado lado del triangulo: "))
    lado2 = float(input("ingresa el segundo lado del triangulo: "))
    lado3 = float(input("ingresa el tercer lado del triangulo: "))
    perimetro = lado + lado2 + lado3
    print(f"el perimetro de este triangulo es {perimetro}")
    return