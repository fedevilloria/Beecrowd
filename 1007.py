"""
Leer cuatro valores enteros A, B, C y D. Calcular e imprimir la diferencia entre el producto de A y B, y el producto de C y D (A * B - C * D).

Entrada
La entrada contiene 4 valores enteros.

Salida
Imprimir DIFERENCA (DIFERENCIA en portugués) con letras mayúsculas, de acuerdo a los ejemplos, con un espacio en blanco antes y después del signo igual.
"""

A = int(input())
B = int(input())
C = int(input())
D = int(input())

dif = (A*B - C*D)

print(f"DIFERENCA = {dif}")