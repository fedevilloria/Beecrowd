"""
Leer 3 números de punto flotante. Luego, imprimir las raíces de la fórmula de Bhaskara. Si es imposible calcular las raíces debido a una división por cero ó a la raíz cuadrad de un número negativo, presentar el mensaje “Impossivel calcular”.

Entrada
Leer 3 números de punto flotante (double) A, B y C.

Salida
Mostrar el resultado con 5 dígitos luego del punto decimal ó el mensaje si es imposible de calcular.
"""

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

#Calcular discriminante
discriminante = (b**2) - (4 * a * c)


if a == 0 or discriminante < 0:
    print("Impossivel calcular")
else:
    #Calcular las raices
    R1 = (-b + discriminante ** 0.5) / (2 * a)
    R2 = (-b - discriminante ** 0.5) / (2 * a)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")