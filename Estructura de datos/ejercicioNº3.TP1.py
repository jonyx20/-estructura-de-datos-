


print("=== Asignación de Aulas ===")
dia = int(input("Ingrese el número del día (1 es lunes, 6 es sábado): "))

if dia < 1 or dia > 6:
    print("Número de día inválido.")
else:
    if dia % 2 == 0:
        print("Los alumnos cursan en el aula A-300.")
    else:
        print("Los alumnos cursan en el aula A-315.")


print("\n=== Cálculo de Descuento de la Cuota ===")
turno = input("Ingrese el turno en el que desea cursar (Mañana/Tarde): ").lower()
materias = int(input("Ingrese el número de materias a inscribir: "))
cuota = float(input("Ingrese el valor de la cuota: $"))

if turno == "tarde" and materias > 3:
    descuento = 0.25  # Descuento del 25%
else:
    descuento = 0.05  # Descuento del 5%

cuota_descuento = cuota * (1 - descuento)
print(f"El valor de la cuota con el descuento aplicado es: ${cuota_descuento:.2f}")


print("\n=== Costo de Estacionamiento ===")
transporte = input("Ingrese el medio de transporte (Auto/Moto/Bicicleta): ").lower()

if transporte in ["auto", "moto"]:
    costo_estacionamiento = 300
elif transporte == "bicicleta":
    costo_estacionamiento = 50
else:
    costo_estacionamiento = 0
    print("Transporte no reconocido. No se aplicará costo de estacionamiento.")

if costo_estacionamiento > 0:
    print(f"El costo diario de estacionamiento es: ${costo_estacionamiento}")


