"""
Leer un entero, que corresponde a la edad de una persona (en días) e imprimirlo en años, meses y días, seguido del respectivo mensaje “ano(s)”, “mes(es)”, “dia(s)”.

Nota: Para facilitar el cálculo, considere al año con 365 días y al mes con 30. En los casos de prueba nunca habrá una situacion que permita 12 meses y algunos días, como 360, 363 ó 364. Este es sólo un ejercicio para plantear un simple razonamiento matemático.

Entrada
La entrada consiste en un solo valor entero.

Salida
Mostrar el resultado, como se muestra a continuación.
"""

n = int(input())

#Numero entero de años (division entera)
anio = n // 365

#Resto luego de sacar los años
resto = n % 365

#Meses completos de lo que queda (division entera)
meses = resto // 30

#Dias que quedan despues de calcular los meses
dias = resto % 30

print(f"{anio} ano(s)\n{meses} mes(es)\n{dias} dia(s)")