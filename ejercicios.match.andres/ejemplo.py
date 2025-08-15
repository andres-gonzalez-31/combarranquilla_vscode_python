MERCADO = "Bienvenido al mejor supermercado de la ciudad."
TITULO = "                    El Pasillo                  "
USUARIO = "¿Qué deseas comprar?"
categorias = ("Las categorías que se manejan en el mejor SM son: carnes, lácteos.")

print(MERCADO)
print(TITULO)
print(USUARIO)
print(categorias)

while True:
    comprar = input("Categoría (escribe 'salir' para terminar): ").lower()

    if comprar == "salir":
        print("Gracias por tu compra. ¡Vuelve pronto!")
        break  # Sale completamente del bucle

    match comprar:
        case "carnes":
            while True:
                print("\nCARNES DISPONIBLES:")
                print("1. Pollo - $13,600 por libra")
                print("2. Cerdo - $10,500 por libra")
                print("3. Carne molida - $12,400 por libra")
                print("4. Volver al menú principal")
                
                opcion = input("¿Qué deseas comprar? (1/2/3/4): ")

                if opcion == "1":
                    precio = 13600
                    producto = "Pollo"
                elif opcion == "2":
                    precio = 10500
                    producto = "Cerdo"
                elif opcion == "3":
                    precio = 12400
                    producto = "Carne molida"
                elif opcion == "4":
                    break  # Sale del bucle de carnes y vuelve al menú principal
                else:
                    print("Opción inválida. Inténtalo de nuevo.")
                    continue  # Repite el bucle sin continuar el código debajo

                while True:
                    try:
                        libras = float(input(f"¿Cuántas libras de {producto} deseas comprar? "))
                        if libras > 0:
                            total = libras * precio
                            print(f"Vas a pagar: ${total:,.0f}")
                            break  # Sale del bucle de libras
                        else:
                            print("Error: Ingresa una cantidad válida.")
                    except ValueError:
                        print("Error: Ingresa un número válido.")

                break  # Sale del bucle de carnes

        case "lacteos":
            while True:
                print("\nLÁCTEOS DISPONIBLES:")
                print("1. Leche entera")
                print("2. Leche de almendra")
                print("3. Leche deslactosada")
                print("4. Volver al menú principal")

                opcion = input("¿Qué deseas comprar? (1/2/3/4) ingresa un numero: ")

                if opcion == "1":
                    producto = "Leche entera"
                elif opcion == "2":
                    producto = "Leche de almendra"
                elif opcion == "3":
                    producto = "Leche deslactosada"
                elif opcion == "4":
                    break  # Sale del bucle de lácteos y vuelve al menú principal
                else:
                    print("Opción inválida. Inténtalo de nuevo.")
                    continue  

                while True:
                    print("\nTamaños disponibles:")
                    print("1. Litro - $5,000 (Leche entera) / $7,000 (Leche de almendra) / $5,500 (Leche deslactosada)")
                    print("2. Medio litro - $2,500 (Leche entera) / $4,000 (Leche de almendra) / $3,500 (Leche deslactosada)")

                    tamano = input("Elige el tamaño (1 = Litro, 2 = Medio litro)ingresa un numero: ")

                    if tamano == "1":
                        precio = 5000 if opcion == "1" else 7000 if opcion == "2" else 5500
                        tamano_txt = "Litro"
                    elif tamano == "2":
                        precio = 2500 if opcion == "1" else 4000 if opcion == "2" else 3500
                        tamano_txt = "Medio litro"
                    else:
                        print("Opción inválida, intenta de nuevo.")
                        continue  # Vuelve a pedir el tamaño sin avanzar

                    while True:
                        try:
                            cantidad = int(input(f"¿Cuántos {tamano_txt}s de {producto} deseas comprar? "))
                            if cantidad > 0:
                                total = cantidad * precio
                                print(f"Tu total a pagar es: ${total:,.0f}")
                                break  # Sale del bucle de cantidad
                            else:
                                print("Error: Ingresa una cantidad válida.")
                        except ValueError:
                            print("Error: Ingresa un número válido.")

                    break  # Sale del bucle de tamaños

                break  # Sale del bucle de lácteos

        case _:
            print("Categoría no disponible. Inténtalo de nuevo.")