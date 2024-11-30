"""
La fórmula para calcular el Área de un Círculo se define como: area = pi . radio^2. Para este problema consideramos pi = 3.14159:

- Calcule el área usando la fórmula dada en la descripción del problema.

Entrada
La entrada consiste de un valor de punto flotante (doble precisión), que es la variable radio.

Salida
Mostrar el mensaje "A=" seguido del valor del área, como en los ejemplos siguientes, con cuatro lugares después del punto decimal. Use variables de doble precisión. Como con todos los problemas, no olvide imprimir un salto de línea luego del resultado, de otra manera Ud. recibirá un mensaje "Presentation Error".

"""
radio = float(input())

area = 3.14159 * radio**2

print(f"A={area:.4f}")
