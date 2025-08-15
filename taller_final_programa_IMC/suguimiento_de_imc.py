"""
Feature

    Evaluar la cantidad de personas evaluadas dependiendo del genero
    Promedio de la edad:LISTO
    Mostrar el promedio global
"""


print("----- Calculadora de IMC -----")

# listas para almacenar información
nombres = []
nombres_hombres = []
nombres_mujeres = []
edad_total = []
edad_mujeres = []
edad_hombres = []
pesos = []
alturas = []
generos = []
imcs = []
clasificaciones = []
lista_bajo_peso = []

# listas separadas por género para promedios
imc_hombres = []
imc_mujeres = []

# contadores de clasificación
bajo_peso = 0
normal = 0
sobrepeso = 0
obesidad = 0


comprobar = True
while comprobar == True:
   ingresos = int(input("cuantas personas deseas calcular su IMC: "))
   if ingresos >0:
    comprobar= False
    # else:
    #     print('ingresa un numero positivo')
    #     continue    

    i = 0
    while i < ingresos:
        print("\n--- Nueva persona ---")
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))

        while True:
            peso = float(input("Ingrese su peso en kg: "))
            if peso > 0:
                break
            print("Ingresa un número positivo.")

        while True:
            altura_cm = float(input("Ingrese su altura en cm: "))
            if altura_cm > 0:
                break
            print("Ingresa un número positivo.")

        altura_m = altura_cm / 100

        while True:
            genero = input("Ingrese su género (HOMBRE / MUJERES): ").upper()
            if genero.upper() == "HOMBRE" :
                edad_hombres.append(edad)
                nombres_hombres.append(nombre)
                break
            elif genero.upper() == "MUJERES":
                edad_mujeres.append(edad)
                nombres_mujeres.append(nombre)
                break
            else:
               print("Género no válido.")
        i += 1

        imc = peso / (altura_m ** 2)


        # clasificación por IMC
        if imc < 18.5:
            clasificacion = "Bajo peso"
            bajo_peso += 1
        elif imc < 25:
            clasificacion = "Normal"
            normal += 1
        elif imc < 30:
            clasificacion = "Sobrepeso"
            sobrepeso += 1
        else:
            clasificacion = "Obesidad"
            obesidad += 1


        # guardar datos
        edad_total.append(edad)
        pesos.append(peso)
        alturas.append(altura_cm)
        generos.append(genero)
        imcs.append(imc)
        clasificaciones.append(clasificacion)

        if genero == "HOMBRE":
            imc_hombres.append(imc)
        else:
            imc_mujeres.append(imc)

        # menú de cambios o continuar
        while True:
            print("\n¿Desea ingresar otra persona o modificar los datos ingresados?")
            print("1. Cambiar género")
            print("2. Cambiar edad")
            print("3. Cambiar altura")
            print("4. Cambiar peso")
            print("5. No (terminar e imprimir resultados)")

            opcion = int(input("Ingrese su opción: "))
            indice_actual = len(nombres) - 1  # se modifica la última persona ingresada

            if opcion == 1:
                nuevo_genero = input("Nuevo género (HOMBRE / MUJER): ").upper()
                if nuevo_genero in ("HOMBRE", "MUJER"):
                    generos[indice_actual] = nuevo_genero
                    print("Género actualizado.")
                else:
                    print("Género no válido.")

            elif opcion == 2:
                nueva_edad = input("Nueva edad: ")
                edad_total[indice_actual] = nueva_edad
                print("Edad actualizada.")

            elif opcion == 3:
                nueva_altura = float(input("Nueva altura en cm: "))
                alturas[indice_actual] = nueva_altura
                altura_m = nueva_altura / 100
                imcs[indice_actual] = pesos[indice_actual] / (altura_m ** 2)
                print("Altura e IMC actualizados.")

            elif opcion == 4:
                nuevo_peso = float(input("Nuevo peso en kg: "))
                pesos[indice_actual] = nuevo_peso
                altura_m = alturas[indice_actual] / 100
                imcs[indice_actual] = nuevo_peso / (altura_m ** 2)
                print("Peso e IMC actualizados.")

            elif opcion == 5:
                break  # salir y mostrar resultados

            else:
                print("Opción inválida.")


        # --- MOSTRAR RESULTADOS DE CADA PERSONA ---
    print("\n----- RESULTADOS -----")
    for i in range(len(nombres)):
        print(f"\nNombre: {nombres[i]}")
        print(f"Edad: {edad_total[i]}")
        print(f"Peso: {pesos[i]} kg")
        print(f"Altura: {alturas[i]} cm")
        print(f"Género: {generos[i]}")
        print(f"IMC: {imcs[i]:.2f}")
        print(f"Clasificación: {clasificaciones[i]}")

    # --- PROMEDIOS ---
    promedio_mujeres = sum(imc_mujeres) / len(imc_mujeres) if len(imc_mujeres) > 0 else 0
    promedio_hombres = sum(imc_hombres) / len(imc_hombres) if len(imc_hombres) > 0 else 0
    promedio__edad_mujeres = sum(edad_mujeres) / len(edad_mujeres) if len(edad_mujeres) > 0 else 0
    promedio__edad_hombre = sum(edad_hombres) / len(edad_hombres) if len(edad_hombres) > 0 else 0



    # --- RESUMEN FINAL ---
    print("\n----- RESUMEN FINAL -----")
    print(f"Promedio de IMC en hombres: {promedio_hombres:.2f}")
    print(f"Promedio de IMC en mujeres: {promedio_mujeres:.2f}")
    print(f"Promedio de edad  en hombres:{promedio__edad_hombre}")
    print(f"Promedio de edad  en mujeres: {promedio__edad_mujeres}")
    print("\nCantidad de personas en cada grupo:")
    print(f"Bajo peso: {bajo_peso} ")
    print(f"Normal: {normal}")
    print(f"Sobrepeso: {sobrepeso} ")
    print(f"Obesidad: {obesidad} ")

   else:
    print('ingresa un numero positivo')