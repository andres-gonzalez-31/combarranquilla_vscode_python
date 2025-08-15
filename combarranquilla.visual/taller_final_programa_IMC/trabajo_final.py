print("----- Calculadora de IMC -----")

# listas para almacenar el imc de hombres y mujeres
imc_hombres = []
imc_mujeres = []

# contadores de clasificación
bajo_peso = 0
normal = 0
sobrepeso = 0
obesidad = 0

# listas para guardar información de cada persona
nombres = []
edades = []
pesos = []
alturas = []
generos = []
imcs = []
clasificaciones = []

salir = True
while salir:
    nombre = input("\nIngrese su nombre: ")
    edad =  input("Ingrese su edad: ") 

    
    while True:
        peso = float(input("Ingrese su peso en kg: "))
        if peso >0:
            break
        else:
            print("ingresa un numero positivo")

    
    while True:
        altura_cm = float(input("Ingrese su altura en cm: "))
        if altura_cm >0:
            break
        else:
            print("ingresa un numero positivo")

    altura_m = altura_cm / 100

    # el != hace referencia a "no es igual a"
    while True:
        genero = input("Ingrese su género (H / M): ").upper()
        if genero == "H" or genero == "M":
            break
        else:
            print("ingresa un genero valido")
    
    imc = peso / (altura_m * altura_m)

    
    if imc < 18.5:
        clasificacion = "Bajo peso"
        bajo_peso += 1
    elif imc >18.5 and imc < 25:
        clasificacion = "Normal"
        normal += 1
    elif imc > 25 and imc< 30:
        clasificacion = "Sobrepeso"
        sobrepeso += 1
    else:
        clasificacion = "Obesidad"
        obesidad += 1

    # se guardan los datos en las listas
    nombres.append(nombre)
    edades.append(edad)
    pesos.append(peso)
    alturas.append(altura_cm)
    generos.append(genero)
    imcs.append(imc)
    clasificaciones.append(clasificacion)


    if genero == "H":
        imc_hombres.append(imc)
    else:
        imc_mujeres.append(imc)
   
    indice_actual = len(nombres) - 1
    while True:
        print("\n¿Desea hacer alguna de estas opciones?:")
        print("1. Cambiar género")
        print("2. Cambiar edad")
        print("3. Cambiar altura")
        print("4. Ingresar otra persona")
        print("5. Salir")

        opcion = input("Ingrese su opción (1-5): ")

        if opcion == "1":
            nuevo_genero = input("Ingrese el nuevo género (H/M): ").upper()
            if nuevo_genero == "H" or nuevo_genero == "M":
                generos[indice_actual] = nuevo_genero
                # Mover el IMC al arreglo correcto
                if nuevo_genero == "H":
                    imc_mujeres.remove(imcs[indice_actual])
                    imc_hombres.append(imcs[indice_actual])
                else:
                    imc_hombres.remove(imcs[indice_actual])
                    imc_mujeres.append(imcs[indice_actual])
                print("Género actualizado correctamente.")
            else:
                print("Género inválido.")
        
        elif opcion == "2":
            nueva_edad = input("Ingrese la nueva edad: ")
            edades[indice_actual] = nueva_edad
            print("Edad actualizada correctamente.")

        elif opcion == "3":
            while True:
                nueva_altura = float(input("Ingrese la nueva altura en cm: "))
                if nueva_altura > 0:
                    alturas[indice_actual] = nueva_altura
                    altura_m = nueva_altura / 100
                    # Recalcular IMC y clasificación
                    imc_nuevo = pesos[indice_actual] / (altura_m ** 2)
                    imcs[indice_actual] = imc_nuevo
                    
                    # Eliminar conteo anterior
                    clasificacion_anterior = clasificaciones[indice_actual]
                    if clasificacion_anterior == "Bajo peso":
                        bajo_peso -= 1
                    elif clasificacion_anterior == "Normal":
                        normal -= 1
                    elif clasificacion_anterior == "Sobrepeso":
                        sobrepeso -= 1
                    else:
                        obesidad -= 1

                    # Nueva clasificación
                    if imc_nuevo < 18.5:
                        clasificacion_nueva = "Bajo peso"
                        bajo_peso += 1
                    elif imc_nuevo < 25:
                        clasificacion_nueva = "Normal"
                        normal += 1
                    elif imc_nuevo < 30:
                        clasificacion_nueva = "Sobrepeso"
                        sobrepeso += 1
                    else:
                        clasificacion_nueva = "Obesidad"
                        obesidad += 1

                    clasificaciones[indice_actual] = clasificacion_nueva
                    print("Altura, IMC y clasificación actualizados.")
                    break
                else:
                    print("Ingresa una altura válida.")
        
        elif opcion == "4":
            break  # Sale del bucle de edición y vuelve a pedir nueva persona
        elif opcion == "5":
            salir = False
            break
        
        else:
            print("Opción inválida.")


# resultados a cada persona ingresada
# .2f lo que hace es mostrar el numero como flotante con solo 2 decimales (para que la persona no se enrrede)
print("\n----- RESULTADOS -----")
for i in range(len(nombres)):
    print(f"\nNombre: {nombres[i]}")
    print(f"Edad: {edades[i]}")
    print(f"Peso: {pesos[i]} kg")
    print(f"Altura: {alturas[i]} cm")
    print(f"Género: {generos[i]}")
    print(f"IMC: {imcs[i]:.2f}")
    print(f"Clasificación: {clasificaciones[i]}")


promedio_hombres = sum(imc_hombres) / len(imc_hombres) if len(imc_hombres) > 0 else 0
promedio_mujeres = sum(imc_mujeres) / len(imc_mujeres) if len(imc_mujeres) > 0 else 0

# resumen ya en general
print("\n----- RESUMEN FINAL -----")
print(f"Promedio de IMC en hombres: {promedio_hombres:.2f}")
print(f"Promedio de IMC en mujeres: {promedio_mujeres:.2f}")
print("\nCantidad de personas en cada grupo:")
print(f"Bajo peso: {bajo_peso}")
print(f"Normal: {normal}")
print(f"Sobrepeso: {sobrepeso}")
print(f"Obesidad: {obesidad}")