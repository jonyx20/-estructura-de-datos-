
def calcular_cambio(total_compra, dinero_recibido):
    if dinero_recibido < total_compra:
        return "Error: El dinero recibido es insuficiente."

    
    billetes = [500, 100, 50, 20, 10, 5, 1]
    vuelto = dinero_recibido - total_compra

    print(f"El total del vuelto es: ${vuelto}")
    
    
    for billete in billetes:
        cantidad_billetes = vuelto // billete  
        vuelto = vuelto % billete  
        if cantidad_billetes > 0:
            print(f"Billetes de ${billete}: {cantidad_billetes}")


print("=== Calculadora de Cambio ===")

total_compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))


calcular_cambio(total_compra, dinero_recibido)
