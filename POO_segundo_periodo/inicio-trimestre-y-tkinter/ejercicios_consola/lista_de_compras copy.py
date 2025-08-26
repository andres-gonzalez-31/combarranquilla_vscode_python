lista_de_compras = []

def agregar_producto(producto):
    print("\n lista de coompras")
    for  producto in lista_de_compras:
        print(f"- {producto}")
        
while True:
    producto = input("Introduce un producto (o 'salir' para terminar): ")
    
    if producto.lower() == 'salir':
        break
    
    lista_de_compras.append(producto)
    agregar_producto(producto)
    
    