"""
Hacer un programa que lea 3 valores enteros y presente el mas grande seguido del mensaje "eh o maior". Usando la siguiente fórmula.

MaiorAB = (a+b+abs(a-b)) / 2

Entrada
El archivo de entrada contiene 3 valores enteros.

Salida
Imprimir el mas grande de los 3 valores seguido por un espacio y el mensaje "eh o maior".
"""

def mayorAB(a, b):
    return (a+b+abs(a-b)) // 2


a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

# Primero comparo entre a y b, despues comparo el mayor de esos dos con la otra variable restante
mayor = mayorAB(a, b)
mayor = mayorAB(mayor, c)

print(f"{mayor} eh o maior")