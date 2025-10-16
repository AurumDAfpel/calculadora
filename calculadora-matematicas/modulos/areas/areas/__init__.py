from areas import area_cuadrado, area_triangulo

def menu():
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
        elif opcion == "2":
            area_triangulo()
        elif opcion == "3":
            area_circulo()
        elif opcion == "4":
            area_rectangulo()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()