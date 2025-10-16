def calcular_pi():
    n = int(input("Ingrese la cantidad de términos para aproximar π: "))
    pi_aprox = 0
    for k in range(n):
        pi_aprox += ((-1)**k) / (2*k + 1)
    pi_aprox *= 4
    print(f"El valor aproximado de π con {n} términos es: {pi_aprox}")
