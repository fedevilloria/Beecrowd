"""
Leer dos valores de punto flotante de doble precisión A y B, correspondiente a dos notas de estudiantes. Luego de esto, calcular el promedio de los estudiantes, considerando que el peso de la nota A es 3.5 y el peso de la nota B es 7.5. Cada nota puede ser de cero a diez, siempre con un dígito después del punto decimal. No se olvide de imprimir el final de línea luego del resultado, de lo contrario recibirá “Presentation Error”. No se olvide del espacio antes y despues del signo igual.

Entrada
El archivo de entrada contiene dos valores de punto flotantes con un dígito después del punto decimal.

Salida
Imprimir el mensaje "MEDIA"(Promedio en Portugués) y el promedio de los estudiantes de acuerdo con los siguientes ejemplos, con 5 dígitos después del punto decimal y con el espacio en blanco antes y después del signo igual.
"""

A = float(input())
B = float(input())

peso_A = 3.5 
peso_B = 7.5

promedio = (A * peso_A + B * peso_B) / (peso_A + peso_B)

print(f"MEDIA = {promedio:.5f}")