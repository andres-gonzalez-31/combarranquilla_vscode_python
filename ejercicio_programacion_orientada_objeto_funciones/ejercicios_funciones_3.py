def precio_tarifa_horaria(precio, hora):
    if hora >= 22 or hora < 6:
        recargo = precio * 0.20
        return precio + recargo
    else:
        return precio

precio = float(input("Ingrese el precio base del servicio: "))
hora = int(input("Ingrese la hora (0 a 23): "))
if hora >= 22 or hora < 6:
    recargo = precio * 0.20
    print(f"por trabajar entre las 22 y las 6, tuviste un recargo del 20%. \nque son: ${recargo}")
    print("Precio con tarifa horaria:", precio_tarifa_horaria(precio, hora))
else:
    print("Precio sin tarifa horaria:", precio_tarifa_horaria(precio, hora))
