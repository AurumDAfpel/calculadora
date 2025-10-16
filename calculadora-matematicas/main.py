from modulos.perimetro.mainPerimetro import elegirFigura
from modulos.areas.mainAreas import menuAreas
from modulos.analisis_numerico import mostrar_menu_analisis  

def mostrar_menu_principal():
    print("\n===== CALCULADORA MATEMÁTICA =====")
    print("1. Cálculo de áreas")
    print("2. Cálculo de perimetro")
    print("3. Análisis numérico")
    print("4. Salir")
    return input("Seleccione una opción (1-5): ")
def main():
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
                menuAreas()
        elif opcion == "2":
                elegirFigura()
        elif opcion == "3":
                mostrar_menu_analisis()
        elif opcion == "4":
                print("¡Gracias por usar la calculadora matemática!")
                break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()