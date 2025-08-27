# El if evalúa una condición y solo ejecuta el bloque si la condición es verdadera.
# Si la condición no se cumple, simplemente no hace nada.
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
    

# 2. IF - ELSE (si... sino)
# El else sirve para ejecutar un bloque alternativo cuando el if no se cumple.

edad = 15

if edad >= 18:
    print("Puedes entrar a la fiesta 🎉")
else:
    print("No puedes entrar, eres menor 🚫")
    
    
# 3. IF - ELIF - ELSE (si... sino si... sino)
# Cuando hay varias condiciones que queremos evaluar en orden, usamos elif (else if).

nota = 3.7

if nota >= 4.5:
    print("Excelente 🏆")
elif nota >= 3.0:
    print("Aprobado 👍")
else:
    print("Reprobado ❌")


# 👉 Se ejecuta solo el primer bloque que sea verdadero, y se ignoran los demás.