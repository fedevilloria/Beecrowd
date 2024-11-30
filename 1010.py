"""
En este problema, la tarea consiste en leer un código de un producto 1, el número de unidades del producto 1, el precio de una unidad de producto 1, el código de un producto 2, el número de unidades del producto 2 y el precio de una unidad de producto 2. Después de esto, calcular y mostrar la cantidad a pagar.

Entrada
El archivo de entrada contiene dos líneas de datos. En cada línea habrá 3 valores: Dos enteros y un valor flotante con 2 dígitos después del punto decimal.

Salida
El archivo de salida debe ser un mensaje como en el siguiente ejemplo. Recuerde el espacio antes de ":" y antes del símbolo "R$". El valor debe ser presentado con 2 dígitos después del punto.
"""
# Leer la primera linea de entrada
cod_producto1, num_unidades1, precio_producto1 = input().split()
cod_producto1 = int(cod_producto1)
num_unidades1 = int(num_unidades1)
precio_producto1 = float(precio_producto1)

# Leer la segunda linea de entrada
cod_producto2, num_unidades2, precio_producto2 = input().split()
cod_producto2 = int(cod_producto2)
num_unidades2 = int(num_unidades2)
precio_producto2 = float(precio_producto2)

valor_total = (num_unidades1 * precio_producto1) + (num_unidades2 * precio_producto2)

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")