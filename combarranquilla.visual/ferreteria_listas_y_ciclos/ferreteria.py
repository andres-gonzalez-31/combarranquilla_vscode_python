producto = []
precios = []

while True:
    usuario = input("Ingresa el nombre del producto: ")

    
    while True:
            precio = float(input("Ingresa el valor del producto: "))
            if precio > 0:

               break
            else:
                print("error: ingresa numero positivo")

    producto.append(usuario)
    precios.append(precio)

    continuar = input("¿Deseas agregar otro producto? solo ingresa alguna de estas dos letras(s/n): ").lower()
    if continuar != "s":
        break

print("\nProductos ingresados:")
for i in range(len(producto)):
    print(f"{producto[i]} - ${precios[i]:,.0f}")