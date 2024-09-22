"""
John hizo una búsqueda en su buscador favorito y encontró la respuesta que buscaba en el tercer enlace de la lista. Es más, vio en el sitio que t personas ya habían hecho clic en este enlace anteriormente. John había leído anteriormente, también en Internet, que el número de personas que hacen clic en el segundo enlace de la lista es el doble del número de personas que hacen clic en el tercer enlace de la lista. En esta lectura, también descubrió que el número de personas que hacen clic en el segundo enlace es la mitad del número de personas que hacen clic en el primer enlace.

John está intrigado por saber cuántas personas hicieron clic en el primer enlace de la búsqueda y, como tú eres su amigo, quiere que le ayudes con esta tarea.

Entrada
Cada caso de prueba tiene un único número, t (1 ≤ t ≤ 1000), que representa el número de personas que han hecho clic en el tercer enlace de la búsqueda.

Salida
Para cada caso de prueba, imprima sólo una línea, que contenga sólo un número entero, indicando cuántas personas hicieron clic en el primer enlace de esta búsqueda.

"""

t = int(input()) #third link

second_link = t*2 # Second Link is the double of the third
first_link = second_link*2 # First link is the double of the second
print(first_link)