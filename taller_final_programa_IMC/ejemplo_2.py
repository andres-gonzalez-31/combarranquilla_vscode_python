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

# listas separadas por género para promedios
imc_hombres = []
imc_mujeres = []

# listas por clasificación y género
clasificacion_genero = {
    "Bajo peso": {"HOMBRE": [], "MUJERES": []},
    "Normal": {"HOMBRE": [], "MUJERES": []},
    "Sobrepeso": {"HOMBRE": [], "MUJERES": []},
    "Obesidad": {"HOMBRE": [], "MUJERES": []}
}

comprobar = True
while comprobar:
    ingresos = int(input("¿Cuántas personas deseas calcular su IMC?: "))
    if ingresos > 0:
        comprobar = False
    else:
        print("Ingresa un número positivo.")
        continue

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
            if genero == "HOMBRE":
                edad_hombres.append(edad)
                nombres_hombres.append(nombre)
                break
            elif genero == "MUJERES":
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
        elif imc > 18.5 and imc < 24.9:
            clasificacion = "normal"
        elif imc > 25.0 and imc < 29.9:
            clasificacion = "sobrepeso"
        else:
            clasificacion = "Obesidad"

        # guardar datos
        nombres.append(nombre)
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

        # guardar nombre en su grupo correspondiente
        clasificacion_genero[clasificacion][genero].append(nombre)
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
    promedio_mujeres = sum(imc_mujeres) / len(imc_mujeres) if imc_mujeres else 0
    promedio_hombres = sum(imc_hombres) / len(imc_hombres) if imc_hombres else 0
    promedio_edad_mujeres = sum(edad_mujeres) / len(edad_mujeres) if edad_mujeres else 0
    promedio_edad_hombres = sum(edad_hombres) / len(edad_hombres) if edad_hombres else 0

    # --- RESUMEN FINAL ---
    print("\n----- RESUMEN FINAL -----")
    print(f"Promedio de IMC en hombres: {promedio_hombres:.2f}")
    print(f"Promedio de IMC en mujeres: {promedio_mujeres:.2f}")
    print(f"Promedio de edad en hombres: {promedio_edad_hombres:.0f}")
    print(f"Promedio de edad en mujeres: {promedio_edad_mujeres:.0f}")

    print("\nCantidad de personas en cada grupo:")
    total_personas = len(nombres)
    for clasificacion, generos_dict in clasificacion_genero.items():
        total_clasificacion = len(generos_dict["HOMBRE"]) + len(generos_dict["MUJERES"])
        print(f"\n{clasificacion}: {total_clasificacion} personas de {total_personas}")
        print(f"  Hombres ({len(generos_dict['HOMBRE'])}): {', '.join(generos_dict['HOMBRE']) if generos_dict['HOMBRE'] else 'Ninguno'}")
        print(f"  Mujeres ({len(generos_dict['MUJERES'])}): {', '.join(generos_dict['MUJERES']) if generos_dict['MUJERES'] else 'Ninguna'}")

    # --- ANÁLISIS DE TENDENCIA GENERAL ---
    def obtener_mayoria(diccionario):
        return max(diccionario, key=lambda k: len(diccionario[k]))

    mayoria_hombres = obtener_mayoria({k: v["HOMBRE"] for k, v in clasificacion_genero.items()})
    mayoria_mujeres = obtener_mayoria({k: v["MUJERES"] for k, v in clasificacion_genero.items()})

    print("\n----- ANÁLISIS GENERAL -----")
    print(f"La mayoría de los hombres están en: {mayoria_hombres}")
    print(f"La mayoría de las mujeres están en: {mayoria_mujeres}")