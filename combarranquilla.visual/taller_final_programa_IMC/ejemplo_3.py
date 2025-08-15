print("----- Calculadora de IMC -----")

# listas para almacenar información
nombres = []
edades = []
pesos = []
alturas = []
generos = []
imcs = []
clasificaciones = []

# listas por clasificación
bajo_peso_hombres = []
bajo_peso_mujeres = []
normal_hombres = []
normal_mujeres = []
sobrepeso_hombres = []
sobrepeso_mujeres = []
obesidad_hombres = []
obesidad_mujeres = []

# listas para promedios
edad_hombres = []
edad_mujeres = []
imc_hombres = []
imc_mujeres = []

# pedir cuántas personas se evaluarán
while True:
    total = int(input("Cuántas personas deseas evaluar: "))
    if total > 0:
        break
    else:
        print("Por favor, ingresa un número positivo.")

# recolección de datos
for i in range(total):
    print(f"\n--- Persona {i+1} ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    peso = float(input("Peso en kg: "))
    altura_cm = float(input("Altura en cm: "))
    altura_m = altura_cm / 100

    while True:
        genero = input("Género (HOMBRE / MUJER): ").upper()
        if genero in ["HOMBRE", "MUJER"]:
            break
        print("Género inválido. Usa HOMBRE o MUJER.")

    # calcular IMC
    imc = peso / (altura_m ** 2)

    # clasificar
    if imc < 18.5:
        clasificacion = "Bajo peso"
        if genero == "HOMBRE":
            bajo_peso_hombres.append(nombre)
        else:
            bajo_peso_mujeres.append(nombre)
    elif imc < 25:
        clasificacion = "Normal"    
        if genero == "HOMBRE":
            normal_hombres.append(nombre)
        else:
            normal_mujeres.append(nombre)
    elif imc < 30:
        clasificacion = "Sobrepeso"
        if genero == "HOMBRE":
            sobrepeso_hombres.append(nombre)
        else:
            sobrepeso_mujeres.append(nombre)
    else:
        clasificacion = "Obesidad"
        if genero == "HOMBRE":
            obesidad_hombres.append(nombre)
        else:
            obesidad_mujeres.append(nombre)

    # guardar datos
    nombres.append(nombre)
    edades.append(edad)
    pesos.append(peso)
    alturas.append(altura_cm)
    generos.append(genero)
    imcs.append(imc)
    clasificaciones.append(clasificacion)

    # para promedios
    if genero == "HOMBRE":
        edad_hombres.append(edad)
        imc_hombres.append(imc)
    else:
        edad_mujeres.append(edad)
        imc_mujeres.append(imc)

    while True:
        print("\n¿Deseas continuar con tus datos  o modificar los datos ingresados?")
        print("1. continuar")
        print("2. modificar dato")

        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            break  # salir del menú y agregar nueva persona
        
        elif opcion == 2:
            print("que deseas cambiar: ")
            print("1. Cambiar género")
            print("2. Cambiar edad")
            print("3. Cambiar altura")
            print("4. Cambiar peso")
            print("5. (terminar)")
            opcion_2 = int(input("Ingrese su opción: "))      
            indice_actual = len(nombres) - 1  # se modifica la última persona ingresada
            if opcion_2 == 1:

                nuevo_genero = input("Nuevo género (H / M): ").upper()
                if nuevo_genero in ("H", "M"):
                    generos[indice_actual] = nuevo_genero
                    print("Género actualizado.")
                else:
                    print("Género no válido.")

            elif opcion_2 == 2:
                nueva_edad = input("Nueva edad: ")
                edades[indice_actual] = nueva_edad
                print("Edad actualizada.")

            elif opcion_2 == 3:
                nueva_altura = float(input("Nueva altura en cm: "))
                alturas[indice_actual] = nueva_altura
                altura_m = nueva_altura / 100
                imcs[indice_actual] = pesos[indice_actual] / (altura_m ** 2)
                print("Altura e IMC actualizados.")

            elif opcion_2 == 4:
                nuevo_peso = float(input("Nuevo peso en kg: "))
                pesos[indice_actual] = nuevo_peso
                altura_m = alturas[indice_actual] / 100
                imcs[indice_actual] = nuevo_peso / (altura_m ** 2)
                print("Peso e IMC actualizados.")


            elif opcion_2 == 5:
                break  # salir y mostrar resultados

        else:
            print("Opción inválida.")

# mostrar resultados individuales
print("\n----- RESULTADOS INDIVIDUALES -----")
for i in range(total):
    print(f"\nNombre: {nombres[i]}")
    print(f"Edad: {edades[i]}")
    print(f"Peso: {pesos[i]} kg")
    print(f"Altura: {alturas[i]} cm")
    print(f"Género: {generos[i]}")
    print(f"IMC: {imcs[i]:.2f}")
    print(f"Clasificación: {clasificaciones[i]}")

# mostrar promedios
print("\n----- PROMEDIOS -----")
if edad_hombres:
    print(f"Promedio de edad en hombres: {sum(edad_hombres)/len(edad_hombres):.1f}")
    print(f"Promedio de IMC en hombres: {sum(imc_hombres)/len(imc_hombres):.2f}")
else:
    print("No se ingresaron hombres.")

if edad_mujeres:
    print(f"Promedio de edad en mujeres: {sum(edad_mujeres)/len(edad_mujeres):.1f}")
    print(f"Promedio de IMC en mujeres: {sum(imc_mujeres)/len(imc_mujeres):.2f}")
else:
    print("No se ingresaron mujeres.")

# mostrar resumen de clasificaciones
print("\n----- RESUMEN POR CLASIFICACIÓN -----")

# bajo peso
total_bajo = len(bajo_peso_hombres) + len(bajo_peso_mujeres)
print(f"\nBajo peso: {total_bajo} personas de {total}")
print(f"Hombres ({len(bajo_peso_hombres)}): {', '.join(bajo_peso_hombres) if bajo_peso_hombres else 'Ninguno'}")
print(f"Mujeres ({len(bajo_peso_mujeres)}): {', '.join(bajo_peso_mujeres) if bajo_peso_mujeres else 'Ninguna'}")

# normal
total_normal = len(normal_hombres) + len(normal_mujeres)
print(f"\nNormal: {total_normal} personas de {total}")
print(f"Hombres ({len(normal_hombres)}): {', '.join(normal_hombres) if normal_hombres else 'Ninguno'}")
print(f"Mujeres ({len(normal_mujeres)}): {', '.join(normal_mujeres) if normal_mujeres else 'Ninguna'}")

# sobrepeso
total_sobrepeso = len(sobrepeso_hombres) + len(sobrepeso_mujeres)
print(f"\nSobrepeso: {total_sobrepeso} personas de {total}")
print(f"Hombres ({len(sobrepeso_hombres)}): {', '.join(sobrepeso_hombres) if sobrepeso_hombres else 'Ninguno'}")
print(f"Mujeres ({len(sobrepeso_mujeres)}): {', '.join(sobrepeso_mujeres) if sobrepeso_mujeres else 'Ninguna'}")

# obesidad
total_obesidad = len(obesidad_hombres) + len(obesidad_mujeres)
print(f"\nObesidad: {total_obesidad} personas de {total}")
print(f"Hombres ({len(obesidad_hombres)}): {', '.join(obesidad_hombres) if obesidad_hombres else 'Ninguno'}")
print(f"Mujeres ({len(obesidad_mujeres)}): {', '.join(obesidad_mujeres) if obesidad_mujeres else 'Ninguna'}")

# mostrar cuál es la tendencia de cada género
print("\n----- ANÁLISIS FINAL -----")

# hombres
mayoria_hombres = ""
mayor_cantidad_hombres = max(len(bajo_peso_hombres), len(normal_hombres), len(sobrepeso_hombres), len(obesidad_hombres))
if mayor_cantidad_hombres == len(bajo_peso_hombres):
    mayoria_hombres = "Bajo peso"
elif mayor_cantidad_hombres == len(normal_hombres):
    mayoria_hombres = "Normal"
elif mayor_cantidad_hombres == len(sobrepeso_hombres):
    mayoria_hombres = "Sobrepeso"
else:
    mayoria_hombres = "Obesidad"

# mujeres
mayoria_mujeres = ""
mayor_cantidad_mujeres = max(len(bajo_peso_mujeres), len(normal_mujeres), len(sobrepeso_mujeres), len(obesidad_mujeres))
if mayor_cantidad_mujeres == len(bajo_peso_mujeres):
    mayoria_mujeres = "Bajo peso"
elif mayor_cantidad_mujeres == len(normal_mujeres):
    mayoria_mujeres = "Normal"
elif mayor_cantidad_mujeres == len(sobrepeso_mujeres):
    mayoria_mujeres = "Sobrepeso"
else:
    mayoria_mujeres = "Obesidad"

print(f"La mayoría de los hombres están en: {mayoria_hombres}")
print(f"La mayoría de las mujeres están en: {mayoria_mujeres}")
