
print("=== Listado de Aulas ===")
print("Día  Aula")


for dia in range(1, 7):
    if dia % 2 == 0:
        aula = "A-300"
    else:
        aula = "A-315"
    print(f"{dia}    {aula}")


print("\n=== Carga de Edades ===")
errores = 0  
while True:
    try:
        edad = int(input("Ingrese una edad (mayor o igual a 18, ingrese -1 para terminar): "))
        if edad == -1:
            break
        if edad >= 18:
            print(f"Edad válida ingresada: {edad}")
        else:
            print("Error: la edad ingresada es menor a 18.")
            errores += 1
    except ValueError:
        print("Error: debe ingresar un número válido.")
        errores += 1

print(f"\nNúmero de errores cometidos: {errores}")


print("\n=== Promedio de Notas de 5 Alumnos ===")
total_notas = 0


for i in range(1, 6):
    while True:
        try:
            nota = float(input(f"Ingrese la nota del alumno {i}: "))
            if 0 <= nota <= 10:
                total_notas += nota
                break
            else:
                print("Error: la nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: debe ingresar un número válido.")

promedio = total_notas / 5
print(f"El promedio de las notas es: {promedio:.2f}")


print("\n=== Costo del Comedor ===")
costo_diario = 1250  


for dias in range(1, 7):
    costo_total = dias * costo_diario
    print(f"{dias} día(s) cuesta(n): ${costo_total}")
