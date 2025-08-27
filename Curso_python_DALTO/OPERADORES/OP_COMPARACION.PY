# Operadores de comparación (sirven para comparar valores → devuelven True o False)
# Operador	Descripción	Ejemplo	Resultado
# ==	Igual a	5 == 5	True
# !=	Diferente de	5 != 3	True
# >	Mayor que	7 > 3	True
# <	Menor que	2 < 5	True
# >=	Mayor o igual que	5 >= 5	True
# <=	Menor o igual que	4 <= 6	True


a = 10
b = 3

# Comparación
print(a > b)   # True
print(a == 10) # True
print(b != 3)  # False


# Verificar si un número está dentro de un rango
edad = 20

print(edad >= 18 and edad <= 30)   # True → está en el rango
# O en Python se puede encadenar:
print(18 <= edad <= 30)            # True



# Verificar si un número es potencia de 2
n = 64
potencia = 2 ** 6   # 2 elevado a 6
print(n == potencia)  # True porque 64 == 2**6



# Combinando aritméticos y comparación

# Verificar si un número es par y mayor que 10
num = 14

es_par = num % 2 == 0   # % y ==
es_mayor = num > 10     # >

if es_par and es_mayor:
    print(num, "es par y mayor que 10")
else:
    print(num, "no cumple la condición")
    
    
    
saldo = 150000
retiro = 40000

# Verificamos si el retiro es posible
if retiro <= saldo and retiro % 10000 == 0:
    saldo -= retiro  # equivalente a saldo = saldo - retiro
    print("Retiro exitoso. Nuevo saldo:", saldo)
else:
    print("Error: monto inválido o saldo insuficiente")