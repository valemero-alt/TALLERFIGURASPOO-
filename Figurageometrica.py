class Figurageometrica:
    """Clase base para figurageométricas."""

    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    # Encapsulamiento con property
    @property
    def ancho(self) -> float:
        return self._ancho

    @ancho.setter
    def ancho(self, value: float):
        if value <= 0:
            raise ValueError("El ancho debe ser mayor que 0.")
        self._ancho = value

    @property
    def alto(self) -> float:
        return self._alto

    @alto.setter
    def alto(self, value: float):
        if value <= 0:
            raise ValueError("El alto debe ser mayor que 0.")
        self._alto = value

    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self) -> float:
        # Método abstracto (se sobrescribe en subclases)
        pass

    def __str__(self) -> str:
        return f"FiguraGeometrica [ancho={self.ancho}, alto={self.alto}]"