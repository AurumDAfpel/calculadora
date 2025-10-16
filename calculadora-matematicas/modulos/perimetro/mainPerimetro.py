from modulos.perimetro.cuadrado import perimetroCuadrado
from modulos.perimetro.circulo import perimetroCirculo
from modulos.perimetro.rectangulo import perimetroRectangulo
from modulos.perimetro.triangulo import perimetroTriangulo

def elegirFigura():
    """bienvenido al menu de perimetros
elije una figura:
1. cuadrado
2. triangulo
3. circulo
4. rectangulo
0. salir
"""
    opcion = input(" ")

    if opcion <0 or opcion >4:
        print("opcion invalida intenta denuevo")
    if opcion == 1:
        perimetroCuadrado()
    elif opcion == 2:
        perimetroTriangulo()
    elif opcion == 3:
        perimetroCirculo()
    elif opcion == 4:
        perimetroRectangulo()
    else:
        return