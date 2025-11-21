from cuadrado import Cuadrado
from rectangulo import Rectangulo


# ---- FUNCIÓN 1: sumar_areas ----
def sumar_areas(figuras: list):
    total = 0
    for figura in figuras:
        total += figura.area()   # polimorfismo: no importa el tipo de figura
    return total


# ---- FUNCIÓN 2: sumar_perimetros ----
def sumar_perimetros(figuras: list):
    total = 0
    for figura in figuras:
        total += figura.perimetro()   # polimorfismo igual que arriba
    return total


# ---- PROGRAMA PRINCIPAL ----
if __name__ == "__main__":
    print("\n--- CREACIÓN DE FIGURAS ---")

    # 1. Crear dos cuadrados y dos rectángulos (valores válidos)
    cuadrado1 = Cuadrado(5)
    cuadrado2 = Cuadrado(10)

    rectangulo1 = Rectangulo(4, 8)
    rectangulo2 = Rectangulo(3, 6)

    figuras = [cuadrado1, cuadrado2, rectangulo1, rectangulo2]

    # 2 y 3. Mostrar área, perímetro, valores e impresión del objeto
    for f in figuras:
        print("\nObjeto:", f)           # __str__
        print("Alto:", f.alto)
        print("Ancho:", f.ancho)
        print("Área:", f.area())
        print("Perímetro:", f.perimetro())

    # 4. Modificación de valores
    print("\n--- MODIFICACIÓN DE VALORES (encapsulamiento) ---")
    print("Cuadrado 1 antes:", cuadrado1)
    cuadrado1.alto = 7
    cuadrado1.ancho = 7
    print("Cuadrado 1 después:", cuadrado1)
    print("rectangulo 1 antes:", rectangulo1)
    rectangulo1.alto = 5
    rectangulo1.ancho = 5
    print("Cuadrado 1 después:", cuadrado1)

    # 5. Prueba con valores inválidos (demostración del encapsulamiento)
    print("\n--- PRUEBA CON VALORES INVÁLIDOS ---")
    try:
        cuadrado_malo = Cuadrado(-5)
    except ValueError as e:
        print("ERROR DETECTADO:", e)

    try:
        rectangulo_malo = Rectangulo(0, 10)
    except ValueError as e:
        print("ERROR DETECTADO:", e)

    # 6. Sumas totales de áreas y perímetros
    print("\n--- SUMAS TOTALES ---")
    print("Suma total de áreas:", sumar_areas(figuras))
    print("Suma total de perímetros:", sumar_perimetros(figuras))

