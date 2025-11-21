DESCRIPCION DEL EJERCICIO 
Este taller tiene como objetivo practicar los conceptos fundamentales de PPO  en Python mediante la implementación de una jerarquía de clases que representan figuras geométrica
Se aplican los siguientes conceptos:
- Encapsulamiento con atributos privados y uso de `@property` / `@setter`
- Herencia entre clases
- Sobrescritura de métodos (`area`, `perimetro`, `__str__`)
- Validaciones internas (valores mayores que cero)
- Polimorfismo al procesar listas de figuras sin conocer su tipo exacto
- Además, se debe crear un programa principal (`main.py`) que:
- Cree varias figuras.
- Muestre sus valores, áreas, perímetros y modificaciones.
- Demuestre validaciones con errores (`ValueError`).
- Calcule la suma total de áreas y perímetros.
EXPLICACION DE CADA CLASE
BASE PRINCIPAL FIGURAGEOMETRICA
Esta es la clase padre de todas las figuras.  
Incluye:
- Atributos privados: `_alto`, `_ancho`
- Encapsulamiento con `@property` y `@setter`
- Validación: alto y ancho deben ser > 0  
- Métodos:
 - `area()` → ancho × alto  
- `perimetro()` → se deja sin implementar (obliga a las hijas a sobrescribirlo)
- `__str__()` → muestra dimensiones
Es la base sobre la cual heredan todas las figuras.


CLASE RECTANGULO
Hereda de `FiguraGeometrica`.
- Recibe un solo parámetro `lado` y lo asigna a `ancho` y `alto`.
- Sobrescribe:
- `area()` → calcula `lado ** 2`.
- `perimetro()` → calcula `4 * lado`.
- Método `__str__()` que muestra el valor del lado


CLASE CUADRADO
Hereda de `FiguraGeometrica`.
- Recibe dos parámetros: `ancho` y `alto`.
- Sobrescribe:
 - `area()` → calcula `ancho * alto`.
- `perimetro()` → calcula `2 * (ancho + alto)`.
- Método `__str__()` que muestra ancho y alto.


CLASE CIRCUNFERENCIA
Hereda de FIGURA GEOMETRICA .
- Recibe un solo valor: RADIO 
- Para mantener compatibilidad con la clase base:
  - alto = ancho = diámetro = 2 × radio
- Atributo adicional privado: `_radio`
- Sobrescribe:
 - `area()` → π × radio²
- `perimetro()` → 2 × π × radio
 - `__str__()` → muestra el radio


captura de pantalla 
   
 <img width="1918" height="1036" alt="Captura de pantalla 2025-11-20 194712" src="https://github.com/user-attachments/assets/ce73e2a1-6233-4623-b7ba-c92d993ec799" />
<img width="1679" height="990" alt="Captura de pantalla 2025-11-20 194733" src="https://github.com/user-attachments/assets/12813383-100b-4a52-8447-48b690faa6a4" />
<img width="1918" height="1028" alt="Captura de pantalla 2025-11-20 194812" src="https://github.com/user-attachments/assets/afe25406-3e40-4d8f-b0a6-d0416a070726" />


  
