import math

class Circulo:
    """
    Representa un círculo con un radio dado.
    """

    def __init__(self, radio):
        """
        Inicializa un nuevo círculo.
        Args:
            radio (float o int): El radio del círculo. Debe ser un valor positivo.
        """
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radio = radio

    def area(self):
        """
        Calcula el área del círculo.
        Returns:
            float: El área del círculo.
        """
        return math.pi * self.radio**2

    def perimetro(self):
        """
        Calcula el perímetro (circunferencia) del círculo.
        Returns:
            float: El perímetro del círculo.
        """
        return 2 * math.pi * self.radio

# Crear instancias de la clase Círculo
circulo1 = Circulo(5)
circulo2 = Circulo(12.5)

# Mostrar áreas y perímetros de las instancias
print(f"Círculo 1 - Radio: {circulo1.radio}")
print(f"  Área: {circulo1.area():.2f}")
print(f"  Perímetro: {circulo1.perimetro():.2f}\n")

print(f"Círculo 2 - Radio: {circulo2.radio}")
print(f"  Área: {circulo2.area():.2f}")
print(f"  Perímetro: {circulo2.perimetro():.2f}")