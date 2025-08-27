# Listas (list) → ordenadas, modificables, permiten repetidos
numeros = [1, 2, 3, 4, 5]
mezcla = [10, "hola", True, 3.5]

# Tuplas (tuple) → ordenadas, no modificables, permiten repetidos
coordenada = (10.5, 20.3)
colores = ("rojo", "verde", "azul")

# Conjuntos (set) → no ordenados, no permiten duplicados
frutas = {"manzana", "pera", "uva", "manzana"}  
# Resultado: {"manzana", "pera", "uva"}

# Diccionarios (dict) → clave : valor, no ordenados (en Python 3.7+ mantienen orden de inserción)
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Bogotá"
}