

print("=== Inscripción de Alumnos ===")


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")


posee_titulo_secundario = True  


matricula = float(input("Ingrese el monto de la matrícula: $"))


cuota = matricula + 1000
print(f"\nLa cuota (matrícula + $1000) es: ${cuota}")


arancel_python_i = 12000
costo_mensual_python_i = arancel_python_i / 4  

print(f"\nEl costo mensual de la materia 'Python I' es: ${costo_mensual_python_i}")


paga_en_efectivo = input("\n¿Paga en efectivo? (si/no): ").lower()

if paga_en_efectivo == "si":
    descuento = cuota * 0.15
    cuota_con_descuento = cuota - descuento
    print(f"\nSe ha aplicado un 15% de descuento por pago en efectivo.")
    print(f"El monto a pagar con descuento es: ${cuota_con_descuento}")
else:
    print(f"\nNo se aplica descuento. El monto a pagar es: ${cuota}")


print("\n=== Datos del Alumno ===")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Fecha de Nacimiento: {fecha_nacimiento}")
print(f"Posee título secundario: {posee_titulo_secundario}")
print(f"Monto de la matrícula: ${matricula}")
print(f"Cuota (matrícula + $1000): ${cuota}")
if paga_en_efectivo == "si":
    print(f"Monto final con descuento: ${cuota_con_descuento}")
else:
    print(f"Monto final sin descuento: ${cuota}")
print(f"El costo mensual de 'Python I' es: ${costo_mensual_python_i}")