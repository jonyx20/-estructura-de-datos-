
def mayor_estricto(a, b, c):
    
    if a > b:
        if a > c:
            if b != a and c != a:
                return a
    if b > a:
        if b > c:
            if a != b and c != b:
                return b
    if c > a:
        if c > b:
            if a != c and b != c:
                return c

    
    return None


print("=== Encontrar el mayor estricto entre tres números ===")


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))


mayor = mayor_estricto(num1, num2, num3)


if mayor is not None:
    print(f"El mayor estricto es: {mayor}")
else:
    print("No existe un mayor estricto entre los números ingresados.")
