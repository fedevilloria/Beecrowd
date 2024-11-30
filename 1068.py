"""
Considerando una expresión con paréntesis, imprima un mensaje informando si la cantidad de paréntesis es correcta o incorrecta, sin considerar el resto de la expresión. Ejemplo:

a+(b*c)-2-a        es correcto
(a+b*(2-c)-2+a)*2  es correcto

donde:
(a*b-(2+c)         es incorrecto
2*(3-a))           es incorrecto
)3+b*(2-c)(        es incorrecto

Resumiendo, todos los paréntesis cerrados debe tener un paréntesis abierto y no es posible un paréntesis de cierre sin un paréntesis abierto previamente, y la cantidad de paréntesis cerrados y abiertos deben ser iguales.

Entrada
El archivo de entrada contiene N expresiones (1 <= N <= 10000), cada una con hasta 1000 caracteres. 

Salida
La salida debe mostrar correct or incorrect para cada caso de prueba de acuerdo con la reglas anteriores.
"""

while True:
    try:
        n = input()
        contadorAbiertos = 0
        
        bandera = True
        
        # Lo que hago a continuacion es contar los parentesis abiertos y sumarlos al contador, si encuentro un parentesis que cierra y el contador de los abiertos esta en 0, quiere decir que se esta cerrando un parentesis sin abrirlo.
        for i in n:
            if i == "(":
                contadorAbiertos += 1
            elif i == ")":
                if contadorAbiertos == 0:
                    bandera = False
                    break
                # Si contador de los parentesis abiertos es > 0 quiere decir que todavia quedan parentesis por cerrar, por lo que si encuentro un parentesis de cierre mientras este esa condicion, le voy a restar 1 al contador.
                else:
                    contadorAbiertos -= 1
        
        if bandera == True and contadorAbiertos == 0:
            print("correct")
        else:
            print("incorrect")
            
    except EOFError: # Finaliza cuando lee End of file.
        break