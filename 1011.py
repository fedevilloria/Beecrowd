"""
Haga un programa que calcule y muestre el volumen de una esfera mediante un radio (R) dado. La fórmula para calcular dicho volumen es: (4/3) * pi * R^3. Considere asignar a Pi el valor: 3.14159.

Tip: Use (4/3.0) ó (4.0/3) en su fórmula, algunos lenguajes (incluyendo C++) asumen que la división entre dos enteros es otro entero. :)

Entrada
La entrada consiste de un valor entero.

Salida
La salida será el mensaje "VOLUME" como en el siguiente ejempo con un espacio antes y luego del igual. El valor debe ser presentado con 3 dígitos decimales.
"""

R = int(input())

volumen = 4/3.0 * 3.14159 * R**3

print(f"VOLUME = {volumen:.3f}")