# +	Suma	5 + 3	8
# -	Resta	10 - 4	6
# *	Multiplicación	7 * 2	14
# /	División (resultado flotante)	10 / 3	3.333...
# //	División entera (descarta decimales)	10 // 3	3
# %	Módulo (residuo)	10 % 3	1
# **	Potencia	2 ** 3	8


a = 10
b = 3

# Aritméticos
print(a + b)   # 13
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000


# Calcular el promedio de tres notas y verificar si aprueba
nota1 = 4.2
nota2 = 3.8
nota3 = 4.5

promedio = (nota1 + nota2 + nota3) / 3  # uso de + y /
print("Promedio:", promedio)

# Redondear promedio con // (entero)
entero = promedio // 1
print("Promedio redondeado hacia abajo:", entero)

# Calcular diferencia con la nota máxima (5.0)
faltante = 5.0 - promedio  # uso de -
print("Te faltaron:", round(faltante, 2), "para la máxima nota")


# Combinando aritméticos y comparación

# Verificar si un número es par y mayor que 10
num = 14

es_par = num % 2 == 0   # % y ==
es_mayor = num > 10     # >

if es_par and es_mayor:
    print(num, "es par y mayor que 10")
else:
    print(num, "no cumple la condición")