def calcular_precio_final(precio, metodo_pago):
    if metodo_pago == "tarjeta":
        agregado = precio * 0.05
        return precio + agregado
    elif metodo_pago == "efectivo":
        descuento = precio * 0.10
        return precio - descuento
    else:
        return precio
precio = float(input("Ingrese el precio del producto: "))
metodo_pago = input("Ingrese el método de pago ('tarjeta' o 'efectivo'): ")
if metodo_pago == "tarjeta":
    valor_agregado =precio* 0.05
    print("tiene un agregado realizado del 5% por pagar con trajeta. su agregado seria de:",valor_agregado)
    print("Precio final con pago por tarjeta:", calcular_precio_final(precio, metodo_pago))
elif metodo_pago == "efectivo":
    valor_agregado =precio* 0.10
    print("tiene un descuento realizado del 10% por pagar en efecitvo. su descuento seria de:",valor_agregado)
    print("Precio final con efectivo:", calcular_precio_final(precio, metodo_pago))
else:
        print("Precio final sin descuento, ni valor agregado:", calcular_precio_final(precio, metodo_pago))
