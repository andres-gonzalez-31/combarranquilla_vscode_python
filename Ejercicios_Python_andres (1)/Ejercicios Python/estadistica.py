# # Construye un programa que, al recibir como datos el peso, la altura y el genero de 
# # N personas que pertenecen a un estado de un pais, obtenga el promedio del peso y el
# # promedio de la altura, tanto la poblacion, masculina como de la femenina


# comprobar = True

# while comprobar == True:
#     n = int(input("Ingrese la cantidad de Personas a Evaluar: "))

#     if n > 0:

#         comprobar = False

#         peso_hombres = 0
#         edad_Hombres =0
#         altura_hombres = 0
#         peso_mujeres = 0
#         altura_mujeres = 0
#         edad_Mujeres = 0
#         cantidad_hombres = 0
#         cantidad_mujeres = 0

#         for i in range(n):

#             peso = float(input("Ingrese el peso en Kg: "))
#             altura = float(input("Ingrese la altura en Cm: "))
#             edad = int(input("ingresa tu edad: "))

#             comprobar_genero = True

#             while comprobar_genero == True:
#                 genero = input("Ingrese Genero M/F: ")

#                 if genero.upper() == "M":

#                     peso_hombres += peso
#                     altura_hombres += altura 
#                     edad_Hombres += edad
#                     cantidad_hombres += 1
#                     comprobar_genero = False

#                 elif genero.upper() == "F":

#                     peso_mujeres += peso
#                     altura_mujeres += altura
#                     cantidad_mujeres += 1
#                     comprobar_genero = False
#                     edad_Mujeres += edad

#                 else:
#                     print("Ingrese Genero Correcto")

#         promedio_altura_h = 0
#         promedio_peso_h = 0
#         promedio_edad_h = 0

#         if cantidad_hombres > 0:
#             promedio_edad_h = edad_Hombres / cantidad_hombres
#             promedio_peso_h = peso_hombres / cantidad_hombres
#             promedio_altura_h = altura_hombres / cantidad_hombres

#         else:
#             print("estas bien")

#         promedio_peso_m = 0
#         promedio_altura_m = 0
#         promedio_edad_m = 0

#         if cantidad_mujeres > 0:
#             promedio_edad_m = edad_Mujeres / cantidad_mujeres
#             promedio_peso_m = peso_mujeres / cantidad_mujeres
#             promedio_altura_m = altura_mujeres / cantidad_mujeres


#         print("\nDe los datos recogidos los promedios fueron: "
#             "\nPromedio peso Hombre:",promedio_peso_h,
#             "\nPromedio altura Hombres:",promedio_altura_h,
#             "\npromedio edad hombre: ", promedio_edad_h,
#             "\nPromedio peso Mujeres:",promedio_peso_m,
#             "\nPromedio altura Mujeres:",promedio_altura_m,
#             "\npromedio edad mujeres",promedio_edad_m)
        
#         if peso_hombres >= 90 and edad_Hombres == 20:
#             print ( "estan obesos para su edad muchachos")
#         else:
#             print("estas obeso a tu edad de : 20")

#     else:
#         print("El numero ingresado no es correcto intentelo nuevamente")

