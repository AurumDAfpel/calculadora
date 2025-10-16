def mostrar_fibonacci():
    n = int(input("¿Cuántos términos de Fibonacci desea mostrar?: "))
    if n <= 0:
        print("Ingrese un número mayor que 0.")
        return
    
    a, b = 0, 1
    print("Secuencia Fibonacci:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
