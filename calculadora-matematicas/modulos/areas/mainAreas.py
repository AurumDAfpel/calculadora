from modulos.areas.cuadrado import area_cuadrado
from modulos.areas.triangulo import area_triangulo
from modulos.areas.circulo import area_circulo
from modulos.areas.rectangulo import area_rectangulo
from modulos.utils import clear_console, pause 

def menuAreas():
    while True:
        print("\n MENÚ DE CÁLCULO DE ÁREAS ")
        print("1. Cuadrado")
        print("2. Triángulo")
        print("3. Círculo")
        print("4. Rectángulo")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            area_cuadrado()
            pause()
            clear_console()
        elif opcion == "2":
            area_triangulo()
            pause()
            clear_console()
        elif opcion == "3":
            area_circulo()
            pause()
            clear_console()
        elif opcion == "4":
            area_rectangulo()
            pause()
            clear_console()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            pause()
            clear_console()
