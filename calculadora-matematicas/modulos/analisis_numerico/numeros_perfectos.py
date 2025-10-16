def es_perfecto(num):
    suma = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            suma += i
    return suma == num

def verificar_numero_perfecto():
    n = int(input("Ingrese un número: "))
    if es_perfecto(n):
        print(f"{n} es un número perfecto 💯")
    else:
        print(f"{n} no es un número perfecto.")
