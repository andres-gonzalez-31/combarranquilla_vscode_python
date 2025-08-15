positivo= 0
negativo= 0
cero= 0

for i in range(0,10):
    numero = int(input("Introduce un número: "))
    
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    else:
        cero += 1
        
    if numero > 0:     
        print(f"Números positivos: {positivo}")
    elif numero < 0:     
        print(f"Números negativos: {negativo}")
    else:
        print(f"Números cero: {cero}")