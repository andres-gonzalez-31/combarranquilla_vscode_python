producto = []
precios = []

while True:
    usuario = input("Ingresa el nombre del producto: ")

    while True:
        try:
            precio = float(input("Ingresa el valor del producto: "))
            break
        except ValueError:
            print("Error: El valor debe ser un número. Intenta de nuevo.")

    producto.append(usuario)
    precios.append(precio)

    continuar = input("¿Deseas agregar otro producto? (s/n): ").lower()
    if continuar != "s":
        break

print("\nProductos ingresados:")
for i in range(len(producto)):
    print(f"{producto[i]} - ${precios[i]:,.0f}")