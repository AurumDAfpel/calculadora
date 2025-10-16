def calcular_pi():
    try:
        n = int(input("Ingrese la cantidad de términos para aproximar π: "))
        if n <= 0:
            print("Por favor ingrese un número entero positivo.")
            return
        
        pi_aprox = 0
        for k in range(n):
            pi_aprox += (-1) ** k / (2 * k + 1)
        
        pi_aprox *= 4
        print(f"\nEl valor aproximado de π con {n} términos es: {pi_aprox:.10f}")
        print(f"Diferencia con el valor real de π: {abs(3.1415926536 - pi_aprox):.10f}")
    
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")