



def menuPerimetros():
    """bienvenido al menu de perimetros
1. elije la figura que le quieras sacar perimetro
2. salir """

opcion = input(" ")
 
if opcion <1 or opcion >2:
    print("opcion invalida intenta denuevo")

def perimetroCuadrado():
    lado = float(input("ingresa el lado de tu cuadrado: "))
    perimetro = lado + lado + lado + lado
    print(f"el perimetor de este cuadrado es {perimetro}")
    return 

def perimetroTriangulo():
    lado = float(input("ingesa el primer lado lado del triangulo: "))
    lado2 = float(input("ingresa el segundo lado del triangulo: "))
    lado3 = float(input("ingresa el tercer lado del triangulo: "))
    perimetro = lado + lado2 + lado3
    print(f"el perimetro de este triangulo es {perimetro}")
    return

def perimetroCirculo():
    radio = float(input("ingresa el radio del circulo: "))
    perimetro = 2 * 3.14159 * radio
    print(f"el periemtro de este circulo es {perimetro}")
    return

def perimetroRectangulo():
    lado = float(input("ingresa la base del rectangulo: "))
    lado2 = float(input("ingresa la altura del rectangulo: "))
    perimetro = 2(lado) + 2(lado2)
    print(f"el perimetro de el rectangulo es {perimetro}")
    return