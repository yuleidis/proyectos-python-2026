

"""🟢 NIVEL 1 – Entender return
✅Ejercicio 1

Crea una función que:

reciba un número
retorne el doble

Luego:

guarda el resultado en una variable
imprímelo


def numero(n):
    return n * 2

resultado = numero(3)

print(f"el resultado es {resultado}")"""



"""✅Ejercicio 2

Crea una función que:

reciba dos números
retorne la suma

Luego imprime el resultado.

def numero(a, b):

    return a + b

resultado = numero(2,1)

print(f"El resultado es: {resultado}")"""



"""🟡 NIVEL 2 – return + lógica"""

"""✅Ejercicio 3

Crea una función que:

reciba un número
retorne:
"Par"
"Impar

def numero(n):

    if n % 2 == 0:

        return "par"

    else:

        return "impar"
    
resultado = numero(2)
print(resultado)"""

    
"""✅Ejercicio 4

Crea una función que:

reciba un número
retorne:
"Positivo"
"Negativo"
"Cero

def numero(n):

    if n > 0:

        return "pisitivo"
    
    elif n < 0:
        return "negativo"
    
    else:

        return "cero"
    
resultado = numero(-2)

print(resultado)"""


"""🟡 NIVEL 3 – Mini reto (clave)"""

"""Ejercicio 5

Crea una función que:

reciba precio y cantidad
retorne el total

Luego:

guarda el resultado
imprime:
Total a pagar: X"""

def numero(a,b):

    return a * b

resultado = numero(2,300)

print(f"Total a pagar es: {resultado}")