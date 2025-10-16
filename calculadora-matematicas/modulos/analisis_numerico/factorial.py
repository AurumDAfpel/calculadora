def calcular_factorial():
    n = int(input("Ingrese un número entero: "))
    if n < 0:
        print("No existe el factorial de un número negativo.")
        return
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    print(f"El factorial de {n} es: {resultado}")
