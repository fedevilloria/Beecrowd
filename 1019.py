"""
Leer un valor entero, que es la duración en segundos de un evento realizado en una fábrica, e informarlo expresado en horas:minutos:segundos.

Entrada
El archivo de entrada contiene al entero N.

Salida
Imprimir el tiempo leído del archivo de entrada (segundos) convertido en horas:minutos:segundos como el ejemplo siguiente.
"""

n = int(input())

#Numero entero de horas (division entera)
horas = n // 3600

#Resto luego de sacar las horas
resto = n % 3600

#Minutos completos de lo que queda (division entera)
minutos = resto // 60

#Segundos que quedan despues de calcular los minutos
segundos = resto % 60



print(f"{horas}:{minutos}:{segundos}")