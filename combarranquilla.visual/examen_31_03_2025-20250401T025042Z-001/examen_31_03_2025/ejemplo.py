comprobar = True

while comprobar:
    n = int(input("Ingrese la cantidad de personas a liquidar: "))

    if n >= 0:
        comprobar = False

        # Variables para el total de horas y conteo de cargos
        horas_gere = horas_ad = horas_ope = 0
        cantidad_gere = cantidad_ope = cantidad_ad = 0

        # Lista para almacenar los detalles de cada persona
        empleados = []

        for i in range(n):
            while True:  
                try:
                    horas = int(input("Ingrese horas trabajadas: "))
                    if horas >= 0:  # Validación para evitar números negativos
                        break  # Si la conversión es exitosa, salimos del bucle
                    else:
                        print("Error: Ingrese un número positivo.")
                except ValueError:
                        print("Error: Debe ingresar un número válido.")
            while True:
                cargo = input("Ingrese el cargo al que pertenece (Gerente/Administrativo/Operario): ").upper()
                
                if cargo == "GERENTE":
                    pago = 65000
                    horas_gere += horas
                    cantidad_gere += 1
                    break
                elif cargo == "ADMINISTRATIVO":
                    pago = 45000
                    horas_ad += horas
                    cantidad_ad += 1
                    break
                elif cargo == "OPERARIO":
                    pago = 25000
                    horas_ope += horas
                    cantidad_ope += 1
                    break
                else:
                    print("Ingrese un cargo correcto.")

            # Calcular la liquidación de la persona y almacenarla
            liquidacion = horas * pago
            empleados.append({"cargo": cargo, "horas": horas, "liquidacion": liquidacion})

        # Calcular los promedios de liquidación por cargo
        total_liquidacion_gere = horas_gere * 65000 if cantidad_gere > 0 else 0
        total_liquidacion_ad = horas_ad * 45000 if cantidad_ad > 0 else 0
        total_liquidacion_ope = horas_ope * 25000 if cantidad_ope > 0 else 0

        # Mostrar el detalle de cada empleado
        print("\nDetalles de liquidación de cada empleado:")
        for empleado in empleados:
            print(f"{empleado['cargo']} trabajó {empleado['horas']} horas = ${empleado['liquidacion']:,.0f}")

        # Mostrar los totales y promedios por cargo
        print("\nResumen general de liquidaciones:")
        print(f"Total liquidación Gerentes: ${total_liquidacion_gere:,.0f}")
        print(f"Total liquidación Administrativos: ${total_liquidacion_ad:,.0f}")
        print(f"Total liquidación Operarios: ${total_liquidacion_ope:,.0f}")

        print("\nCantidad de empleados por cargo:")
        print(f"Gerentes: {cantidad_gere}, Total horas trabajadas: {horas_gere}")
        print(f"Administrativos: {cantidad_ad}, Total horas trabajadas: {horas_ad}")
        print(f"Operarios: {cantidad_ope}, Total horas trabajadas: {horas_ope}")

    else:
        print("Número incorrecto, intente de nuevo.")