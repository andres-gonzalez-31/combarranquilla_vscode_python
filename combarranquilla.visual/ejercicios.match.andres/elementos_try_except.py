while True:
    try:
        numero = int(input("Ingresa un número: "))
        print(f"El número ingresado es: {numero}")
        break  # Sale del bucle si la entrada es correcta
    except ValueError:
        print("Error: Debes ingresar un número válido. Inténtalo de nuevo.")


# Manejo de múltiples errores
# Puedes manejar diferentes tipos de errores con múltiples except:
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero  # Puede causar división por cero
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número entero.")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")


# Uso de finally (Opcional)
# finally se ejecuta siempre, haya error o no. Se usa para liberar recursos, cerrar archivos, etc.
try:
    archivo = open("datos.txt", "r")  # Abre un archivo
    contenido = archivo.txt()
    print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")
finally:
    print("Cerrando programa...")