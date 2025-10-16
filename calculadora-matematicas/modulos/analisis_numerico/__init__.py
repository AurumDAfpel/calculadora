from . import pi, factorial, fibonacci, numeros_amigos, numeros_perfectos
from modulos.utils import clear_console, pause 

def mostrar_menu_analisis():
    while True:
        print("\n=== ANÁLISIS NUMÉRICO ===")
        print("1. Calcular valor aproximado de π")
        print("2. Calcular factorial de un número")
        print("3. Mostrar secuencia de Fibonacci")
        print("4. Verificar si dos números son amigos")
        print("5. Verificar si un número es perfecto")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            pi.calcular_pi()
            pause()
            clear_console()
        elif opcion == "2":
            factorial.calcular_factorial()
            pause()
            clear_console()
        elif opcion == "3":
            fibonacci.mostrar_fibonacci()
            pause()
            clear_console()
        elif opcion == "4":
            numeros_amigos.verificar_numeros_amigos()
            pause()     
            clear_console()
        elif opcion == "5":
            numeros_perfectos.verificar_numero_perfecto()
            pause()
            clear_console()
        elif opcion == "6":
            print("Volviendo al menú principal...")
            pause()
            clear_console()
            return
        else:
            print("Opción no válida, intente de nuevo.")
            pause()
            clear_console()
