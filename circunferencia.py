from Figurageometrica import Figurageometrica
import math

class Circunferencia(Figurageometrica):
    """
    Clase Circunferencia que hereda de FiguraGeometrica.
    """

    def __init__(self, radio: float):
        super().__init__(radio, radio)  # usamos ancho=alto=radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor: float):
        self.ancho = valor
        self.alto = valor

    def area(self) -> float:
        return math.pi * (self.ancho ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.ancho

    def __str__(self) -> str:
        return f"Circunferencia [radio={self.radio}]"