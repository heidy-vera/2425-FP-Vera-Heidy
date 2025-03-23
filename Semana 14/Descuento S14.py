#Creación de una función para el calculo de descuentos

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento en función del monto total de la compra y el porcentaje de descuento.
    :param monto_total: float - Monto total de la compra.
    :param porcentaje_descuento: float - Porcentaje de descuento (por defecto 15%).
    :return: float - Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Solicitar al usuario el monto total de la compra
monto = float(input("Ingrese el monto total de la compra: "))

# Primera llamada a la función (usando el valor predeterminado del descuento)
descuento1 = calcular_descuento(monto)
monto_final1 = monto - descuento1
print(f"\nCon el descuento del 15%, el monto del descuento es: {descuento1:.2f}")
print(f" El Monto final a pagar: {monto_final1:.2f}\n")

# Segunda llamada a la función (con un porcentaje de descuento personalizado)
porcentaje = float(input("Ingrese el porcentaje del descuento a aplicar: "))
descuento2 = calcular_descuento(monto, porcentaje)
monto_final2 = monto - descuento2
print(f"\nCon un descuento del {porcentaje}%, el monto del descuento es: {descuento2:.2f}")
print(f" El Monto final a pagar: {monto_final2:.2f}")