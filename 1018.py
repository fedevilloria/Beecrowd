"""
En este problema tienes que leer un valor entero y calcular el menor número posible de billetes en que puede ser descompuesto. Los billetes posibles son 100, 50, 20, 10, 5, 2 y 1. Imprimir el valor leído y la lista de billetes.

Entrada
La entrada contiene un valor entero N (0 < N < 1000000).

Salida
Imprimir el número leído y la cantidad mínima necesaria de billetes en lenguaje 
portugués, como muestra el ejemplo. No olvides imprimir el final de línea luego de cada línea, de otra forma recibirás “Presentation Error”.
"""

N = int(input())

billetes = [100, 50, 20, 10, 5, 2, 1]
cantidades = []

print(N)

for billete in billetes:
    cantidades.append(N // billete)
    N %= billete

for i in range(len(billetes)):
    valor_billete = f"{billetes[i]:.2f}".replace(".", ",")
    print(f"{cantidades[i]} nota(s) de R$ {valor_billete}")