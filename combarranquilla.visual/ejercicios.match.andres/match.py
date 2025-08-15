MERCADO = "bienvenido al mejor super mercado de la ciudad."
TITULO="                    el pasillo                  "
USUARIO ="Que deseas comprar"
categorias = ("las categorias que se manejan en el mejor SM son: carnes, lacteos ")
print(MERCADO)
print(TITULO)
print(USUARIO)
print(categorias)
while   True:
    comprar = str(input("categoria: "))
    match comprar:
        case "carnes" :
           while True:
            print("CARNES")
            print("pollo")
            print("cerdo")
            print("carne molida")
            valor = input("Que deseas: ")
            if valor == "pollo" :
                    print("la libra vale 13.600.")
                    libras_pollo=int(input("cuantas quieres: "))
                    pollo = 13600
                    final = libras_pollo * pollo
                    print("vas a pagar: ", final)
                    break

            elif valor == "cerdo" :
                    print("la libra vale 10.500.")
                    libras_cerdo=float(input("cuantas quieres: "))
                    cerdo = 10500
                    final2 = libras_cerdo * cerdo
                    print("vas a pagar: ", final2)
                    break

            elif valor == "carne molida" :
                    print("la libra vale 12.400.")
                    libras_molida=float(input("cuantas quieres: "))
                    molida = 12400
                    final3 = libras_molida * molida
                    print("vas a pagar: ", final3)
                    break
            else:
                    print("no se encuentra por el momento")

        case "lacteos" :
            comprobar = True
            while comprobar == True:
             print("LACTEOS")
             print("leche entera")
             print("leche de almendra")
             print("leche delastosada")
             valor = input("Que deseas: ")
             compro = False
             if valor == "leche entera" :
                    while True:
                        MEDIO = 2500  
                        LITRO =  5000   
                        print("valor del litro:",LITRO)  
                        print("valor del medio",MEDIO)  
                        leche_entera=input("de que tamaño la quieres: ").lower()
                        match  leche_entera :
                            case "litro":
                                cuantas = int(input("cuantas vas a llevar: "))
                                pago = LITRO * cuantas
                                print("tu valor a pagar es de: ", pago)
                                break

                            case "medio":
                                cuantas = int(input("cuantas vas a llevar: "))
                                pago= MEDIO * cuantas
                                print("tu valor a pagar es de: ", pago)
                                break

                            case _:
                                print("no se encuentra por el momento")

             elif valor == "leche de almendra" :
                      while  True:
                        LITRO =  7000   
                        MEDIO = 4000  
                        print("valor del litro:",LITRO)  
                        print("valor del medio",MEDIO)  
                        leche_de_almendra=input("de que tamaño la quieres: ").lower()

                        match  leche_de_almendra :
                            case "litro":
                                cuantas = int(input("cuantas vas a llevar: "))
                                pago = LITRO * cuantas
                                print("tu valor a pagar es de: ", pago)
                                break
                            
                            case "medio":
                                cuantas = int(input("cuantas vas a llevar: "))
                                pago= MEDIO * cuantas
                                print("tu valor a pagar es de: ", pago)
                                break
                            
                            case _:
                                print("no se encuentra por el momento")

             elif valor == "leche delastosada" :
                      while  True:
                        LITRO =  5500   
                        MEDIO = 3500    
                        print("valor del litro:",LITRO)  
                        print("valor del medio",MEDIO)  
                        leche_delastosada=input("de que tamaño la quieres: ").lower()
                        match  leche_delastosada :
                            case "litro":
                                cuantas = int(input("cuantas vas a llevar: "))
                                pago = LITRO * cuantas
                                print("tu valor a pagar es de: ", pago)
                                break
                            
                            case "medio":
                                cuantas = int(input("cuantas vas a llevar: "))
                                pago= MEDIO * cuantas
                                print("tu valor a pagar es de: ", pago)
                                break
                            
                            case _:
                                print("no se encuentra por el momento")
                    

             else:
                                print("no se encuentra por el momento")
        case _:
            print("no hay en la tienda")
