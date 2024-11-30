"""
Escriba un programa que lea tres valores de punto flotante: A, B y C. Luego, calcular y mostrar:
a) El área del triángulo rectángulo de base A y altura C.
b) El área del círculo de radio C (Pi = 3.14159).
c) El área del trapecio el cual tiene A y B como bases, y C como altura.
d) El área del cuadrado de lado B.
e) El área del rectángulo de lados A y B.

Entrada
La entrada contiene tres valores de doble precisión con un dígito luego del punto decimal.

Salida
La salida contiene 5 renglones. Cada uno de los renglones corresponde a las áreas descriptas anteriormente, siempre con el mensaje correspondiente (en portugués) y un espacio entre los dos puntos y el valor. El valor calculado debe ser presentado con 3 dígitos luego del punto decimal.
"""

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

area_triangulo = (A * C) / 2
area_circulo = pi * (C**2)
area_trapecio = ((A + B) * C) / 2
area_cuadrado = B**2
area_rectangulo = A * B

print(f"TRIANGULO: {area_triangulo:.3f}\nCIRCULO: {area_circulo:.3f}\nTRAPEZIO: {area_trapecio:.3f}\nQUADRADO: {area_cuadrado:.3f}\nRETANGULO: {area_rectangulo:.3f}")