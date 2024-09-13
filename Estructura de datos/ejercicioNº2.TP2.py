import calendar


def fecha_valida(dia, mes, año):
    
    if mes < 1 or mes > 12:
        return False
    
    
    dias_en_mes = calendar.monthrange(año, mes)[1]
    
    
    if dia < 1 or dia > dias_en_mes:
        return False
    
    return True


print("=== Verificación de Fecha ===")


dia = int(input("Ingrese el día (1-31): "))
mes = int(input("Ingrese el mes (1-12): "))
año = int(input("Ingrese el año: "))


if fecha_valida(dia, mes, año):
    print(f"La fecha {dia}/{mes}/{año} es válida.")
else:
    print(f"La fecha {dia}/{mes}/{año} no es válida.")
