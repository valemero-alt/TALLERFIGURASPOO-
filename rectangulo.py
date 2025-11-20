from Figurageometrica import Figurageometrica


class Rectangulo(Figurageometrica):
    """
    Clase rectángulo que  hereda de Figurageometrica.
    """

    def __init__(self, ancho: float, alto: float):
        super().__init__(ancho=ancho, alto=alto)

    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)

    def __str__(self) -> str:
        return f"Rectángulo(ancho={self.ancho:.2f}, alto={self.alto:.2f})"

