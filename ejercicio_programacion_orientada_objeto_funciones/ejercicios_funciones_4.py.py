def verificar_inventario(productos):
    for cantidad in productos:
        if cantidad == 0:
            print("Producto agotado")

cantidades = input("Ingrese las cantidades de productos separadas por comas (ej: 5,3,0,7): ")
lista_cantidades = [int(c.strip()) for c in cantidades.split(",")]
verificar_inventario(lista_cantidades)
if cantidades != 0:
    print(":).'tu lista de cantidades a sido guardad exitosamente'.(:")