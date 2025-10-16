from modulos.perimetro.cuadrado import perimetroCuadrado
from modulos.perimetro.circulo import perimetroCirculo
from modulos.perimetro.rectangulo import perimetroRectangulo
from modulos.perimetro.triangulo import perimetroTriangulo
from modulos.utils import clear_console, pause  

def elegirFigura():
    print("bienvenido al menu de perimetros")
    print("elije una figura:")
    print("1. Cuadrado")
    print("2. Triangulo")  
    print("3. Circulo")
    print("4. Rectangulo")
    print("5. Salir")

    opcion = input(" ")

    if opcion <"0" or opcion >"4":
        print("opcion invalida intenta denuevo")
    if opcion == "1":
        perimetroCuadrado()
        pause()
        clear_console()
    elif opcion == "2":
        perimetroTriangulo()
        pause()
        clear_console()
    elif opcion == "3":
        perimetroCirculo()
        pause()
        clear_console()
    elif opcion == "4":
        perimetroRectangulo()
        pause()
        clear_console()
    else:
        return