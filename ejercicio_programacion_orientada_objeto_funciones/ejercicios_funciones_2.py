def precio_con_envio(precio_base, envio_incluido):
    if envio_incluido== "si":
        return precio_base + 10000
    else:
        return precio_base

precio_base = float(input("Ingrese el precio base del producto: "))
envio_incluido = input("¿Incluye envío? (si/no): ").lower() 
if envio_incluido == "si":
    print("Precio con envío:", precio_con_envio(precio_base, envio_incluido))
elif envio_incluido == "no":
    print("Precio sin  envío:", precio_con_envio(precio_base, envio_incluido))
else:
    print("ERROR! ingresa de nuevo el valor correcto.")
    envio_incluido = input("¿Incluye envío? (si/no): ").lower()                                   