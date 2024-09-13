

print("=== Registro de Notas de Exámenes ===")


nota1 = float(input("Ingrese la nota del primer parcial: "))
nota2 = float(input("Ingrese la nota del segundo parcial: "))


promedio = (nota1 + nota2) / 2


if nota2 >= 7:
    print("\nAprobó el último examen (segundo parcial).")
else:
    print("\nDesaprobó el último examen (segundo parcial).")


if nota2 > nota1:
    print("Mejoró su desempeño en el segundo parcial.")
elif nota2 == nota1:
    print("Mantuvo la nota entre ambos parciales.")
else:
    print("Empeoró su desempeño en el segundo parcial.")


if promedio >= 7:
    print("\nPromocionó la materia (promedio mayor o igual a 7).")
elif promedio >= 4:
    print("\nDebe rendir final (promedio mayor o igual a 4, pero menor a 7).")
else:
    print("\nDebe recursar la materia (promedio menor a 4).")


print(f"\n=== Resultados ===")
print(f"Nota del primer parcial: {nota1}")
print(f"Nota del segundo parcial: {nota2}")
print(f"Promedio de las dos notas: {promedio:.2f}")