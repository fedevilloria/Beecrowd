"""
La cata de té a ciegas consiste en identificar un té utilizando únicamente los sentidos del olfato y el gusto.

Como parte del Desafío Ideal de los Consumidores de Té Puro (ICPC), se organiza un programa de televisión local. Durante el programa, se prepara una tetera llena y se entrega a cinco concursantes una taza de té a cada uno. Los participantes deben oler, probar y evaluar la muestra para identificar el tipo de té, que puede ser: (1) té blanco; (2) té verde; (3) té negro; o (4) té de hierbas. Al final, se comprueban las respuestas para determinar el número de aciertos.

Teniendo en cuenta el tipo de té real y las respuestas proporcionadas, determine el número de concursantes que acertaron la respuesta correcta.

Entrada
La primera línea contiene un entero T que representa el tipo de té (1 ≤ T ≤ 4). La segunda línea contiene cinco enteros A, B, C, D y E, que indican la respuesta dada por cada concursante (1 ≤ A, B, C, D, E ≤ 4).

Salida
Da salida a una línea con un número entero que representa el número de concursantes que obtuvieron la respuesta correcta.
"""

bandera = True
contador = 0

while bandera:
    T = int(input())
    if T < 1 or T > 4:
        print("Fallo")
    else:
        bandera = False


A,B,C,D,E = map(int, input().split())

if A == T:
    contador += 1
if B == T:
    contador += 1
if C == T:
    contador += 1
if D == T:
    contador += 1
if E == T:
    contador += 1

print(contador)