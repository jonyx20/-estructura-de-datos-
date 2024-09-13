
def calcular_precio(moneda, cantidad):
    precio_unitario = 1000
    total_sin_descuento = precio_unitario * cantidad
    descuento = 0
    incremento = 0

    
    if moneda == "dolares":
        descuento = 0.05
        print("Descuento del 5% por pago en dólares.")
    elif moneda == "yenes":
        descuento = 0.15
        print("Descuento del 15% por pago en yenes.")
    elif moneda == "guaranies":
        descuento = 0.20
        print("Descuento del 20% por pago en guaraníes.")
    elif moneda == "pesos":
        descuento = 0.10
        print("Descuento del 10% por pago en pesos.")
    else:
        incremento = 0.10
        print("Aumento del 10% por pago con otra moneda.")

    
    if descuento > 0:
        total_final = total_sin_descuento * (1 - descuento)
    else:
        total_final = total_sin_descuento * (1 + incremento)

    return total_final, descuento, incremento


def emitir_recibo(nombre_comprador, nombre_empresa, moneda, cantidad, total_final, descuento, incremento):
    print("\n=== Recibo de Compra ===")
    print(f"Nombre del comprador: {nombre_comprador}")
    print(f"Nombre de la empresa: {nombre_empresa}")
    print(f"Tipo de moneda utilizada: {moneda}")
    if descuento > 0:
        print(f"Descuento aplicado: {descuento * 100}%")
    elif incremento > 0:
        print(f"Incremento aplicado: {incremento * 100}%")
    print(f"Cantidad de zapallos: {cantidad}")
    print(f"Precio total en pesos: ${total_final:.2f}")
    print("=========================")

print("=== Venta de Zapallos ===")


nombre_comprador = input("Ingrese su nombre: ")
nombre_empresa = input("Ingrese nombre de la empresa: ")


print("\nTipos de monedas disponibles y sus descuentos:")
print("- Dólares: 5% de descuento")
print("- Yenes: 15% de descuento")
print("- Guaraníes: 20% de descuento")
print("- Pesos: 10% de descuento")
print("- Otras monedas: 10% de aumento")


moneda = input("Ingrese la moneda de pago (dolares, yenes, guaranies, pesos u otra): ").lower()
cantidad = int(input("Ingrese la cantidad de zapallos: "))


total_final, descuento, incremento = calcular_precio(moneda, cantidad)


emitir_recibo(nombre_comprador, nombre_empresa, moneda, cantidad, total_final, descuento, incremento)
