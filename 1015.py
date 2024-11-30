"""
Leer los cuatro valores correspondientes a las coordenadas x e y de dos puntos en el plano, p1 (x1, y1) y p2 (x2, y2) y calcular la distancia entre ellos, mostrando cuatro decimales, de acuerdo a la fórmula:

Distancia = sqrt:((x2 - x1)^2 + (y2 - y1)^2)

Entrada
La entrada contiene dos líneas de datos, la primera contiene dos valores double: x1 y1, la segunda también contiene dos valores double con un dígito después del punto: x2 y2.

Salida
Calcular y mostrar el valor de la distancia usando la fórmula provista, con cuatro decimales.
"""

x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)

x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)

raiz_cuadrada = ( ((x2 - x1)**2) + ((y2 - y1)**2) ) ** 0.5

print(f"{raiz_cuadrada:.4f}")