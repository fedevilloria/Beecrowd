"""
Escribe un programa que lea un número de empleado, su número de horas trabajadas en el mes y el monto recibido por hora. Imprimir el número de empleado y el salario que él/ella recibirá a fin de mes, con dos lugares decimales.

    No se olvide de imprimir los saltos de líneas después del resultado, de lo contrario, recibirá “Presentation Error”.
    No se olvide del espacio en blanco antes y después del signo igual y después de U$.

Entrada
El archivo de entrada contiene 2 números enteros y 1 valor de punto flotante, representando el número, cantidad de horas trabajadas y el monto recibido del empleado por hora trabajada.

Salida
Imprimir el número y salario del empleado, acorde al siguiente ejemplo, con los espacios en blanco antes y después del signo igual.

"""

num_empleado = int(input())
hs_trabajadasxmes = int(input())
salario = float(input())

sueldo = hs_trabajadasxmes * salario

print(f"NUMBER = {num_empleado}\nSALARY = U$ {sueldo:.2f}")