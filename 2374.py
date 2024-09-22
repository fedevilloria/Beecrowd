"""
Inflar neumáticos de coche debería ser una tarea diaria para todos los conductores. Para ello, las gasolineras cuentan con una bomba de aire. La mayoría de las bombas actuales son electrónicas, lo que permite al conductor indicar la presión deseada en un teclado. Cuando se conecta al neumático, la bomba primero lee la presión actual y calcula la diferencia de presión entre la presión deseada y la leída. Con esta diferencia, desinfla o infla el neumático para alcanzar la presión correcta.

Se solicitó su ayuda para desarrollar el programa de la próxima bomba de SBC: sistemas de bombas computarizados.

Escriba un programa que, dada la presión deseada ingresada por el conductor y la presión de los neumáticos leída por la bomba, indique la diferencia entre la presión deseada y la presión leída.

Entrada
La primera línea de la entrada contiene un número entero N que indica la presión deseada por el conductor (1 ≤ N ≤ 40). La segunda línea contiene un número entero M que indica la presión leída por la bomba (1 ≤ M ≤ 40).

Salida
Su programa debe imprimir una sola línea que contenga la diferencia entre la presión deseada y la presión leída.
"""


flag = True

while flag:
    n = int(input())
    if 1 <= n <= 40:
        m = int(input())
        if 1 <= m <= 40:
            preasure = n - m
            print(preasure)
            flag = False
        else:
            print("Intente de nuevo.")
    else:
        print("Intente de nuevo.")




