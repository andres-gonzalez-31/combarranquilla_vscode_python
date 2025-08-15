numero = int(input("Ingrese un número para su tabla de multiplicar: "))
tabla = []

for i in range(1, 11):
    resultado = numero * i
    tabla.append(f"{numero} x {i} = {resultado}")

print("\nTabla de multiplicar:")
for linea in tabla:
    print(linea)