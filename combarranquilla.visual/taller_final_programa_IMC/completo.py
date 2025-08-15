import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from tabulate import tabulate
from tqdm import tqdm
import time

# Cconsola Rich
console = Console()

# Limpiar pantalla al inicio
os.system("cls")

# Logo ASCII (American Standard Code for Information Interchange)
logo = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ██╗███╗   ███╗ ██████╗    ██████╗ █████╗ ██╗      ██████╗   ║
║   ██║████╗ ████║██╔════╝   ██╔════╝██╔══██╗██║     ██╔════╝   ║
║   ██║██╔████╔██║██║        ██║     ███████║██║     ██║        ║
║   ██║██║╚██╔╝██║██║        ██║     ██╔══██║██║     ██║        ║
║   ██║██║ ╚═╝ ██║╚██████╗   ╚██████╗██║  ██║███████╗╚██████╗   ║
║   ╚═╝╚═╝     ╚═╝ ╚═════╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ║
║                                                               ║
║              CALCULADORA DE ÍNDICE DE MASA CORPORAL           ║
╚═══════════════════════════════════════════════════════════════╝
"""

# Mostrar logo
console.print(Panel(logo, border_style="cyan", width=70))

# Título principal
console.print(
    Panel("CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC)", style="yellow bold", width=70)
)

# Listas para almacenar información
nombres = []
edades = []
pesos = []
alturas = []
generos = []
imcs = []
clasificaciones = []

# Listas por clasificación
bajo_peso_hombres = []
bajo_peso_mujeres = []
normal_hombres = []
normal_mujeres = []
sobrepeso_hombres = []
sobrepeso_mujeres = []
obesidad_hombres = []
obesidad_mujeres = []

# Listas para promedios
edad_hombres = []
edad_mujeres = []
imc_hombres = []
imc_mujeres = []

# pedir cuántas personas se evaluarán
while True:
    console.rule("", style="cyan")
    total_texto = console.input("[bold]¿Cuántas personas deseas evaluar?: [/bold]")

    if total_texto.isdigit() and int(total_texto) > 0:
        total = int(total_texto)
        break

    else:
        console.print(
            "[bold red]⚠ Por favor, ingresa un número positivo válido.[/bold red]"
        )

# Mostrar barra de progreso para inicialización
with Progress(
    SpinnerColumn(),  # Elegir la barra como spinner
    TextColumn("[bold green]Preparando sistema...[/bold green]"),
    transient=True,  # La barra desaparecerá al finalizar
) as progress:
    task = progress.add_task("", total=100)
    for i in range(100):
        time.sleep(0.01)  # Simular trabajo
        progress.update(task, advance=1)  # Actualiza la barra avanzando 1 paso

# recolección de datos
for i in range(total):
    os.system("cls")  # Limpiar pantalla para cada persona

    # Título de registro
    console.print(Panel(f"REGISTRO DE DATOS", style="magenta bold", width=70))
    console.print(
        f"[bold yellow]★ PERSONA {i+1} DE {total} ★[/bold yellow]", justify="center"
    )

    # Crear tabla para entrada de datos
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Campo", style="bold")
    table.add_column("Valor")

    nombre = console.input("[bold]Nombre: [/bold]")

    # Validación de edad
    while True:
        edad_texto = console.input("[bold]Edad: [/bold]")

        if edad_texto.isdigit() and 0 < int(edad_texto) < 120:
            edad = int(edad_texto)
            break

        console.print(
            "[bold red]⚠ Edad no válida. Debe estar entre 1 y 120.[/bold red]"
        )

    # Validación de peso
    while True:
        peso_texto = console.input("[bold]Peso en kg: [/bold]")

        # Verificar si es un número válido
        if peso_texto.replace(".", "", 1).isdigit() and "." in peso_texto:
            peso = float(peso_texto)

            if 0 < peso < 500:
                break

        elif peso_texto.isdigit():
            peso = float(peso_texto)

            if 0 < peso < 500:
                break

        console.print(
            "[bold red]⚠ Peso no válido. Debe estar entre 1 y 500 kg.[/bold red]"
        )

    # Validación de altura
    while True:
        altura_texto = console.input("[bold]Altura en cm: [/bold]")

        # Verificar si es un número válido

        if altura_texto.replace(".", "", 1).isdigit() and "." in altura_texto:
            altura_cm = float(altura_texto)

            if 50 < altura_cm < 250:
                break

        elif altura_texto.isdigit():
            altura_cm = float(altura_texto)

            if 50 < altura_cm < 250:
                break

        console.print(
            "[bold red]⚠ Altura no válida. Debe estar entre 50 y 250 cm.[/bold red]"
        )

    altura_m = altura_cm / 100

    while True:
        genero = console.input(
            "[bold]Género ([blue]HOMBRE[/blue]/[magenta]MUJER[/magenta]): [/bold]"
        ).upper()

        if genero in ["HOMBRE", "MUJER"]:
            break

        console.print("[bold red]⚠ Género inválido. Usa HOMBRE o MUJER.[/bold red]")

    # calcular IMC con barra de progreso
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Calculando IMC...[/bold green]"),
        transient=True,
    ) as progress:
        task = progress.add_task("", total=100)
        for j in range(100):
            time.sleep(0.01)  # Simular cálculo
            progress.update(task, advance=1)

        imc = peso / (altura_m**2)

    # clasificar en base a su peso
    if imc < 18.5:
        clasificacion = "Bajo peso"
        color_clasificacion = "blue"

        if genero == "HOMBRE":
            bajo_peso_hombres.append(nombre)
        else:
            bajo_peso_mujeres.append(nombre)

    elif imc < 25:
        clasificacion = "Normal"
        color_clasificacion = "green"

        if genero == "HOMBRE":
            normal_hombres.append(nombre)
        else:
            normal_mujeres.append(nombre)

    elif imc < 30:
        clasificacion = "Sobrepeso"
        color_clasificacion = "yellow"

        if genero == "HOMBRE":
            sobrepeso_hombres.append(nombre)
        else:
            sobrepeso_mujeres.append(nombre)

    else:
        clasificacion = "Obesidad"
        color_clasificacion = "red"

        if genero == "HOMBRE":
            obesidad_hombres.append(nombre)
        else:
            obesidad_mujeres.append(nombre)

    # Agregar datos en las listas
    nombres.append(nombre)
    edades.append(edad)
    pesos.append(peso)
    alturas.append(altura_cm)
    generos.append(genero)
    imcs.append(imc)
    clasificaciones.append(clasificacion)

    # Guardar datos en las listas de promedios si el género es el correcto para ese promedio
    if genero == "HOMBRE":
        edad_hombres.append(edad)
        imc_hombres.append(imc)
    else:
        edad_mujeres.append(edad)
        imc_mujeres.append(imc)

    # Mostrar resultados inmediatos en tabla
    result_table = Table(title="Resultados", show_header=False)
    result_table.add_column("Campo", style="bold")
    result_table.add_column("Valor")

    result_table.add_row("Nombre", nombre)
    result_table.add_row("Edad", str(edad))
    result_table.add_row("Peso", f"{peso} kg")
    result_table.add_row("Altura", f"{altura_cm} cm")
    result_table.add_row(
        "Género", f"[{'blue' if genero=='HOMBRE' else 'magenta'}]{genero}[/]"
    )
    result_table.add_row("IMC", f"{imc:.2f}")
    result_table.add_row("Clasificación", f"[{color_clasificacion}]{clasificacion}[/]")

    console.print(result_table)

    # Mejorar la captura de opciones para evitar errores con entradas vacías
    while True:
        console.rule(style="yellow")
        console.print(
            "[bold]¿Deseas continuar con tus datos o modificar los datos ingresados?[/bold]"
        )
        console.print("[green]1. ✓ Continuar[/green]")
        console.print("[yellow]2. ⟲ Modificar dato[/yellow]")

        opcion_texto = console.input("[bold]Ingrese su opción: [/bold]")

        # Verificar si la entrada está vacía
        if not opcion_texto.strip():
            console.print(
                "[bold red]⚠ Por favor, ingresa una opción válida.[/bold red]"
            )
            continue

        if opcion_texto.isdigit():
            opcion = int(opcion_texto)

            if opcion == 1:
                break

            elif opcion == 2:
                console.rule(style="cyan")
                console.print("[bold]¿Qué deseas cambiar?[/bold]")
                console.print("[blue]1. Cambiar género[/blue]")
                console.print("[blue]2. Cambiar edad[/blue]")
                console.print("[blue]3. Cambiar altura[/blue]")
                console.print("[blue]4. Cambiar peso[/blue]")
                console.print("[green]5. ✓ Terminar[/green]")

                opcion_2_texto = console.input("[bold]Ingrese su opción: [/bold]")

                # Verificar si la entrada está vacía
                if not opcion_2_texto.strip():
                    console.print(
                        "[bold red]⚠ Por favor, ingresa una opción válida.[/bold red]"
                    )
                    continue

                if opcion_2_texto.isdigit():
                    opcion_2 = int(opcion_2_texto)
                    indice_actual = (
                        len(nombres) - 1
                    )  # se modifica la última persona ingresada

                    if opcion_2 == 1:
                        nuevo_genero = console.input(
                            "[bold]Nuevo género ([blue]H[/blue]/[magenta]M[/magenta]): [/bold]"
                        ).upper()
                        if nuevo_genero in ("H", "M"):
                            genero_completo = (
                                "HOMBRE" if nuevo_genero == "H" else "MUJER"
                            )
                            generos[indice_actual] = genero_completo
                            console.print(
                                "[bold green]✓ Género actualizado.[/bold green]"
                            )
                        else:
                            console.print("[bold red]⚠ Género no válido.[/bold red]")

                    elif opcion_2 == 2:
                        nueva_edad_texto = console.input("[bold]Nueva edad: [/bold]")

                        if nueva_edad_texto.isdigit():
                            nueva_edad = int(nueva_edad_texto)

                            if nueva_edad > 0 and nueva_edad < 120:
                                edades[indice_actual] = nueva_edad
                                console.print(
                                    "[bold green]✓ Edad actualizada.[/bold green]"
                                )
                            else:
                                console.print(
                                    "[bold red]⚠ Edad no válida. Debe estar entre 1 y 120.[/bold red]"
                                )

                        else:
                            console.print(
                                "[bold red]⚠ Por favor, ingresa un número válido.[/bold red]"
                            )

                    elif opcion_2 == 3:
                        nueva_altura_texto = console.input(
                            "[bold]Nueva altura en cm: [/bold]"
                        )
                        if nueva_altura_texto.replace(".", "", 1).isdigit():
                            nueva_altura = float(nueva_altura_texto)

                            if nueva_altura > 50 and nueva_altura < 250:
                                alturas[indice_actual] = nueva_altura
                                altura_m = nueva_altura / 100
                                imcs[indice_actual] = pesos[indice_actual] / (
                                    altura_m**2
                                )
                                console.print(
                                    "[bold green]✓ Altura e IMC actualizados.[/bold green]"
                                )

                            else:
                                console.print(
                                    "[bold red]⚠ Altura no válida. Debe estar entre 50 y 250 cm.[/bold red]"
                                )

                        else:
                            console.print(
                                "[bold red]⚠ Por favor, ingresa un número válido.[/bold red]"
                            )

                    elif opcion_2 == 4:
                        nuevo_peso_texto = console.input(
                            "[bold]Nuevo peso en kg: [/bold]"
                        )
                        if nuevo_peso_texto.replace(".", "", 1).isdigit():
                            nuevo_peso = float(nuevo_peso_texto)

                            if nuevo_peso > 0 and nuevo_peso < 500:
                                pesos[indice_actual] = nuevo_peso
                                altura_m = alturas[indice_actual] / 100
                                imcs[indice_actual] = nuevo_peso / (altura_m**2)
                                console.print(
                                    "[bold green]✓ Peso e IMC actualizados.[/bold green]"
                                )
                            else:
                                console.print(
                                    "[bold red]⚠ Peso no válido. Debe estar entre 1 y 500 kg.[/bold red]"
                                )

                        else:
                            console.print(
                                "[bold red]⚠ Por favor, ingresa un número válido.[/bold red]"
                            )

                    elif opcion_2 == 5:
                        break  # salir y mostrar resultados

                    else:
                        console.print("[bold red]⚠ Opción inválida.[/bold red]")
                else:
                    console.print(
                        "[bold red]⚠ Por favor, ingresa un número válido.[/bold red]"
                    )
            else:
                console.print("[bold red]⚠ Opción inválida.[/bold red]")
        else:
            console.print("[bold red]⚠ Por favor, ingresa un número válido.[/bold red]")

# Limpiar pantalla antes de mostrar resultados
os.system("cls")

# Mostrar barra de progreso para procesamiento final
with Progress(
    SpinnerColumn(),
    TextColumn("[bold green]Procesando resultados...[/bold green]"),
    transient=True,
) as progress:
    task = progress.add_task("", total=100)
    for i in range(100):
        time.sleep(0.02)  # Simular trabajo
        progress.update(task, advance=1)

# Menú de opciones para ver información
while True:
    os.system("cls")
    console.print(Panel("MENÚ DE RESULTADOS", style="cyan bold", width=70))
    console.print("[bold yellow]Seleccione qué información desea ver:[/bold yellow]")
    console.print("[blue]1. Ver resultados individuales[/blue]")
    console.print("[green]2. Ver promedios[/green]")
    console.print("[magenta]3. Ver resumen por clasificación[/magenta]")
    console.print("[cyan]4. Ver análisis final[/cyan]")
    console.print("[yellow]5. Ver toda la información[/yellow]")
    console.print("[red]6. Salir del programa[/red]")

    opcion_menu = console.input("[bold]Ingrese su opción: [/bold]")

    if opcion_menu.isdigit():
        opcion = int(opcion_menu)

        if opcion == 1:
            # Mostrar resultados individuales
            os.system("cls")
            console.print(
                Panel("RESULTADOS INDIVIDUALES", style="green bold", width=70)
            )

            # Crear tabla para resultados individuales
            for i in range(total):

                # Determinar color para clasificación
                if "Bajo peso" in clasificaciones[i]:
                    color_clasificacion = "blue"
                elif "Normal" in clasificaciones[i]:
                    color_clasificacion = "green"
                elif "Sobrepeso" in clasificaciones[i]:
                    color_clasificacion = "yellow"
                else:
                    color_clasificacion = "red"

                # Crear tabla para cada persona
                person_table = Table(title=f"Persona {i+1}: {nombres[i]}")
                person_table.add_column("Atributo", style="bold")
                person_table.add_column("Valor")

                person_table.add_row("Nombre", nombres[i])
                person_table.add_row("Edad", f"{edades[i]} años")
                person_table.add_row("Peso", f"{pesos[i]} kg")
                person_table.add_row("Altura", f"{alturas[i]} cm")
                person_table.add_row(
                    "Género",
                    f"[{'blue' if generos[i]=='HOMBRE' else 'magenta'}]{generos[i]}[/]",
                )
                person_table.add_row("IMC", f"{imcs[i]:.2f}")
                person_table.add_row(
                    "Clasificación", f"[{color_clasificacion}]{clasificaciones[i]}[/]"
                )

                console.print(person_table)

            console.input(
                "[bold yellow]Presione Enter para volver al menú...[/bold yellow]"
            )

        elif opcion == 2:

            # Mostrar promedios
            os.system("cls")
            console.print(Panel("PROMEDIOS", style="yellow bold", width=70))

            # Tabla para promedios
            promedio_table = Table()
            promedio_table.add_column("Género", style="bold")
            promedio_table.add_column("Promedio de Edad")
            promedio_table.add_column("Promedio de IMC")

            if edad_hombres:
                promedio_table.add_row(
                    "[blue]Hombres[/]",
                    f"{sum(edad_hombres)/len(edad_hombres):.1f} años",
                    f"{sum(imc_hombres)/len(imc_hombres):.2f}",
                )
            else:
                promedio_table.add_row(
                    "[blue]Hombres[/]", "No hay datos", "No hay datos"
                )

            if edad_mujeres:
                promedio_table.add_row(
                    "[magenta]Mujeres[/]",
                    f"{sum(edad_mujeres)/len(edad_mujeres):.1f} años",
                    f"{sum(imc_mujeres)/len(imc_mujeres):.2f}",
                )
            else:
                promedio_table.add_row(
                    "[magenta]Mujeres[/]", "No hay datos", "No hay datos"
                )

            console.print(promedio_table)

            console.input(
                "[bold yellow]Presione Enter para volver al menú...[/bold yellow]"
            )

        elif opcion == 3:
            # Mostrar resumen por clasificación
            os.system("cls")
            console.print(
                Panel("RESUMEN POR CLASIFICACIÓN", style="magenta bold", width=70)
            )

            # Tabla para bajo peso
            total_bajo = len(bajo_peso_hombres) + len(bajo_peso_mujeres)
            bajo_peso_table = Table(
                title=f"[blue]BAJO PESO: {total_bajo} personas ({(total_bajo/total*100):.1f}%)[/]",
            )
            bajo_peso_table.add_column("Género", style="bold")
            bajo_peso_table.add_column("Cantidad")
            bajo_peso_table.add_column("Personas")

            bajo_peso_table.add_row(
                "[blue]Hombres[/]",
                str(len(bajo_peso_hombres)),
                ", ".join(bajo_peso_hombres) if bajo_peso_hombres else "Ninguno",
            )
            bajo_peso_table.add_row(
                "[magenta]Mujeres[/]",
                str(len(bajo_peso_mujeres)),
                ", ".join(bajo_peso_mujeres) if bajo_peso_mujeres else "Ninguna",
            )

            console.print(bajo_peso_table)

            # Tabla para normal
            total_normal = len(normal_hombres) + len(normal_mujeres)
            normal_table = Table(
                title=f"[green]NORMAL: {total_normal} personas ({(total_normal/total*100):.1f}%)[/]",
            )
            normal_table.add_column("Género", style="bold")
            normal_table.add_column("Cantidad")
            normal_table.add_column("Personas")

            normal_table.add_row(
                "[blue]Hombres[/]",
                str(len(normal_hombres)),
                ", ".join(normal_hombres) if normal_hombres else "Ninguno",
            )
            normal_table.add_row(
                "[magenta]Mujeres[/]",
                str(len(normal_mujeres)),
                ", ".join(normal_mujeres) if normal_mujeres else "Ninguna",
            )

            console.print(normal_table)

            # Tabla para sobrepeso
            total_sobrepeso = len(sobrepeso_hombres) + len(sobrepeso_mujeres)
            sobrepeso_table = Table(
                title=f"[yellow]SOBREPESO: {total_sobrepeso} personas ({(total_sobrepeso/total*100):.1f}%)[/]",
            )
            sobrepeso_table.add_column("Género", style="bold")
            sobrepeso_table.add_column("Cantidad")
            sobrepeso_table.add_column("Personas")

            sobrepeso_table.add_row(
                "[blue]Hombres[/]",
                str(len(sobrepeso_hombres)),
                ", ".join(sobrepeso_hombres) if sobrepeso_hombres else "Ninguno",
            )
            sobrepeso_table.add_row(
                "[magenta]Mujeres[/]",
                str(len(sobrepeso_mujeres)),
                ", ".join(sobrepeso_mujeres) if sobrepeso_mujeres else "Ninguna",
            )

            console.print(sobrepeso_table)

            # Tabla para obesidad
            total_obesidad = len(obesidad_hombres) + len(obesidad_mujeres)
            obesidad_table = Table(
                title=f"[red]OBESIDAD: {total_obesidad} personas ({(total_obesidad/total*100):.1f}%)[/]",
            )
            obesidad_table.add_column("Género", style="bold")
            obesidad_table.add_column("Cantidad")
            obesidad_table.add_column("Personas")

            obesidad_table.add_row(
                "[blue]Hombres[/]",
                str(len(obesidad_hombres)),
                ", ".join(obesidad_hombres) if obesidad_hombres else "Ninguno",
            )
            obesidad_table.add_row(
                "[magenta]Mujeres[/]",
                str(len(obesidad_mujeres)),
                ", ".join(obesidad_mujeres) if obesidad_mujeres else "Ninguna",
            )

            console.print(obesidad_table)

            console.input(
                "[bold yellow]Presione Enter para volver al menú...[/bold yellow]"
            )

        elif opcion == 4:

            # Mostrar análisis final
            os.system("cls")
            console.print(Panel("ANÁLISIS FINAL", style="cyan bold", width=70))

            # hombres
            mayoria_hombres = ""
            mayor_cantidad_hombres = max(
                len(bajo_peso_hombres),
                len(normal_hombres),
                len(sobrepeso_hombres),
                len(obesidad_hombres),
            )

            if mayor_cantidad_hombres == len(bajo_peso_hombres):
                mayoria_hombres = "[blue]Bajo peso[/]"
            elif mayor_cantidad_hombres == len(normal_hombres):
                mayoria_hombres = "[green]Normal[/]"
            elif mayor_cantidad_hombres == len(sobrepeso_hombres):
                mayoria_hombres = "[yellow]Sobrepeso[/]"
            else:
                mayoria_hombres = "[red]Obesidad[/]"

            # mujeres
            mayoria_mujeres = ""
            mayor_cantidad_mujeres = max(
                len(bajo_peso_mujeres),
                len(normal_mujeres),
                len(sobrepeso_mujeres),
                len(obesidad_mujeres),
            )

            if mayor_cantidad_mujeres == len(bajo_peso_mujeres):
                mayoria_mujeres = "[blue]Bajo peso[/]"
            elif mayor_cantidad_mujeres == len(normal_mujeres):
                mayoria_mujeres = "[green]Normal[/]"
            elif mayor_cantidad_mujeres == len(sobrepeso_mujeres):
                mayoria_mujeres = "[yellow]Sobrepeso[/]"
            else:
                mayoria_mujeres = "[red]Obesidad[/]"

            # Tabla para análisis final
            analisis_table = Table()
            analisis_table.add_column("Género", style="bold")
            analisis_table.add_column("Tendencia Mayoritaria")

            analisis_table.add_row("[blue]Hombres[/]", mayoria_hombres)
            analisis_table.add_row("[magenta]Mujeres[/]", mayoria_mujeres)

            console.print(analisis_table)

            console.input(
                "[bold yellow]Presione Enter para volver al menú...[/bold yellow]"
            )

        elif opcion == 5:

            # Mostrar toda la información
            os.system("cls")

            # Resultados individuales
            console.print(
                Panel("RESULTADOS INDIVIDUALES", style="green bold", width=70)
            )

            for i in range(total):
                if "Bajo peso" in clasificaciones[i]:
                    color_clasificacion = "blue"
                elif "Normal" in clasificaciones[i]:
                    color_clasificacion = "green"
                elif "Sobrepeso" in clasificaciones[i]:
                    color_clasificacion = "yellow"
                else:
                    color_clasificacion = "red"

                person_table = Table(title=f"Persona {i+1}: {nombres[i]}")
                person_table.add_column("Atributo", style="bold")
                person_table.add_column("Valor")

                person_table.add_row("Nombre", nombres[i])
                person_table.add_row("Edad", f"{edades[i]} años")
                person_table.add_row("Peso", f"{pesos[i]} kg")
                person_table.add_row("Altura", f"{alturas[i]} cm")
                person_table.add_row(
                    "Género",
                    f"[{'blue' if generos[i]=='HOMBRE' else 'magenta'}]{generos[i]}[/]",
                )
                person_table.add_row("IMC", f"{imcs[i]:.2f}")
                person_table.add_row(
                    "Clasificación", f"[{color_clasificacion}]{clasificaciones[i]}[/]"
                )

                console.print(person_table)

            # Promedios
            console.print(Panel("PROMEDIOS", style="yellow bold", width=70))

            promedio_table = Table()
            promedio_table.add_column("Género", style="bold")
            promedio_table.add_column("Promedio de Edad")
            promedio_table.add_column("Promedio de IMC")

            if edad_hombres:
                promedio_table.add_row(
                    "[blue]Hombres[/]",
                    f"{sum(edad_hombres)/len(edad_hombres):.1f} años",
                    f"{sum(imc_hombres)/len(imc_hombres):.2f}",
                )
            else:
                promedio_table.add_row(
                    "[blue]Hombres[/]", "No hay datos", "No hay datos"
                )

            if edad_mujeres:
                promedio_table.add_row(
                    "[magenta]Mujeres[/]",
                    f"{sum(edad_mujeres)/len(edad_mujeres):.1f} años",
                    f"{sum(imc_mujeres)/len(imc_mujeres):.2f}",
                )
            else:
                promedio_table.add_row(
                    "[magenta]Mujeres[/]", "No hay datos", "No hay datos"
                )

            console.print(promedio_table)

            # Resumen por clasificación
            console.print(
                Panel("RESUMEN POR CLASIFICACIÓN", style="magenta bold", width=70)
            )

            # Resto del código para mostrar todas las tablas de clasificación...
            # Tabla para bajo peso
            total_bajo = len(bajo_peso_hombres) + len(bajo_peso_mujeres)
            bajo_peso_table = Table(
                title=f"[blue]BAJO PESO: {total_bajo} personas ({(total_bajo/total*100):.1f}%)[/]",
            )
            bajo_peso_table.add_column("Género", style="bold")
            bajo_peso_table.add_column("Cantidad")
            bajo_peso_table.add_column("Personas")

            bajo_peso_table.add_row(
                "[blue]Hombres[/]",
                str(len(bajo_peso_hombres)),
                ", ".join(bajo_peso_hombres) if bajo_peso_hombres else "Ninguno",
            )
            bajo_peso_table.add_row(
                "[magenta]Mujeres[/]",
                str(len(bajo_peso_mujeres)),
                ", ".join(bajo_peso_mujeres) if bajo_peso_mujeres else "Ninguna",
            )

            console.print(bajo_peso_table)

            # Tabla para normal
            total_normal = len(normal_hombres) + len(normal_mujeres)
            normal_table = Table(
                title=f"[green]NORMAL: {total_normal} personas ({(total_normal/total*100):.1f}%)[/]",
            )
            normal_table.add_column("Género", style="bold")
            normal_table.add_column("Cantidad")
            normal_table.add_column("Personas")

            normal_table.add_row(
                "[blue]Hombres[/]",
                str(len(normal_hombres)),
                ", ".join(normal_hombres) if normal_hombres else "Ninguno",
            )
            normal_table.add_row(
                "[magenta]Mujeres[/]",
                str(len(normal_mujeres)),
                ", ".join(normal_mujeres) if normal_mujeres else "Ninguna",
            )

            console.print(normal_table)

            # Tabla para sobrepeso
            total_sobrepeso = len(sobrepeso_hombres) + len(sobrepeso_mujeres)
            sobrepeso_table = Table(
                title=f"[yellow]SOBREPESO: {total_sobrepeso} personas ({(total_sobrepeso/total*100):.1f}%)[/]",
            )
            sobrepeso_table.add_column("Género", style="bold")
            sobrepeso_table.add_column("Cantidad")
            sobrepeso_table.add_column("Personas")

            sobrepeso_table.add_row(
                "[blue]Hombres[/]",
                str(len(sobrepeso_hombres)),
                ", ".join(sobrepeso_hombres) if sobrepeso_hombres else "Ninguno",
            )
            sobrepeso_table.add_row(
                "[magenta]Mujeres[/]",
                str(len(sobrepeso_mujeres)),
                ", ".join(sobrepeso_mujeres) if sobrepeso_mujeres else "Ninguna",
            )

            console.print(sobrepeso_table)

            # Tabla para obesidad
            total_obesidad = len(obesidad_hombres) + len(obesidad_mujeres)
            obesidad_table = Table(
                title=f"[red]OBESIDAD: {total_obesidad} personas ({(total_obesidad/total*100):.1f}%)[/]",
            )
            obesidad_table.add_column("Género", style="bold")
            obesidad_table.add_column("Cantidad")
            obesidad_table.add_column("Personas")

            obesidad_table.add_row(
                "[blue]Hombres[/]",
                str(len(obesidad_hombres)),
                ", ".join(obesidad_hombres) if obesidad_hombres else "Ninguno",
            )
            obesidad_table.add_row(
                "[magenta]Mujeres[/]",
                str(len(obesidad_mujeres)),
                ", ".join(obesidad_mujeres) if obesidad_mujeres else "Ninguna",
            )

            console.print(obesidad_table)

            # Análisis final
            console.print(Panel("ANÁLISIS FINAL", style="cyan bold", width=70))

            # hombres
            mayoria_hombres = ""
            mayor_cantidad_hombres = max(
                len(bajo_peso_hombres),
                len(normal_hombres),
                len(sobrepeso_hombres),
                len(obesidad_hombres),
            )
            if mayor_cantidad_hombres == len(bajo_peso_hombres):
                mayoria_hombres = "[blue]Bajo peso[/]"
            elif mayor_cantidad_hombres == len(normal_hombres):
                mayoria_hombres = "[green]Normal[/]"
            elif mayor_cantidad_hombres == len(sobrepeso_hombres):
                mayoria_hombres = "[yellow]Sobrepeso[/]"
            else:
                mayoria_hombres = "[red]Obesidad[/]"

            # mujeres
            mayoria_mujeres = ""
            mayor_cantidad_mujeres = max(
                len(bajo_peso_mujeres),
                len(normal_mujeres),
                len(sobrepeso_mujeres),
                len(obesidad_mujeres),
            )
            if mayor_cantidad_mujeres == len(bajo_peso_mujeres):
                mayoria_mujeres = "[blue]Bajo peso[/]"
            elif mayor_cantidad_mujeres == len(normal_mujeres):
                mayoria_mujeres = "[green]Normal[/]"
            elif mayor_cantidad_mujeres == len(sobrepeso_mujeres):
                mayoria_mujeres = "[yellow]Sobrepeso[/]"
            else:
                mayoria_mujeres = "[red]Obesidad[/]"

            # Tabla para análisis final
            analisis_table = Table()
            analisis_table.add_column("Género", style="bold")
            analisis_table.add_column("Tendencia Mayoritaria")

            analisis_table.add_row("[blue]Hombres[/]", mayoria_hombres)
            analisis_table.add_row("[magenta]Mujeres[/]", mayoria_mujeres)

            console.print(analisis_table)

            console.input(
                "[bold yellow]Presione Enter para volver al menú...[/bold yellow]"
            )

        elif opcion == 6:
            # Salir del programa
            os.system("cls")
            console.print(Panel("PROGRAMA FINALIZADO", style="green bold", width=70))
            break

        else:
            console.print(
                "[bold red]⚠ Opción inválida. Por favor, ingrese un número del 1 al 6.[/bold red]"
            )
            time.sleep(2)
    else:
        console.print("[bold red]⚠ Por favor, ingresa un número válido.[/bold red]")
        time.sleep(2)