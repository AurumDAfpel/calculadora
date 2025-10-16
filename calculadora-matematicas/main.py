from modulos.perimetro import mainPerimetro

def mostrar_menu_principal():
    print("\n===== CALCULADORA MATEMÁTICA =====")
    print("1. Cálculo de áreas")
    print("2. Cálculo de perimetro")
    print("3. Análisis numérico")
    print("4. [Pendiente de implementar]")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")
def main():
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            print("Módulo de áreas aún no implementado")
        elif opcion == "2":
                mainPerimetro()
        elif opcion == "3":
                print("Módulo de análisis numérico aún no implementado")
        elif opcion == "4":
                print("Esta funcionalidad está pendiente de implementar")
        elif opcion == "5":
                print("¡Gracias por usar la calculadora matemática!")
                break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()