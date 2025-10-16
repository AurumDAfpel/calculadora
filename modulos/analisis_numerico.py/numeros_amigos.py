def suma_divisores_propios(num):
    suma = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            suma += i
    return suma

def verificar_numeros_amigos():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    if suma_divisores_propios(a) == b and suma_divisores_propios(b) == a:
        print(f"{a} y {b} son números amigos 😎")
    else:
        print(f"{a} y {b} no son números amigos.")
