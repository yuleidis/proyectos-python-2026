"""🟡 Ejercicio 1 – Positivo o no

Pide un número al usuario.

Si el número es mayor que 0, imprime:
El número es positivo

Si no, imprime:
El número no es positivo


a = int(input("Digite un numero"))

if a > 0:
    print("El numero es positivo")

else:
    print("El numero es negativo")"""


"""🟡 Ejercicio 2 – Mayor o menor

Pide un número al usuario.

Si el número es mayor o igual a 10, imprime:
Número grande

Si es menor, imprime:
Número pequeño

a = int(input("Digite un numero"))


if a >= 10:
    print("Número grande")

else:
    print("Número pequeño")"""


"""🟡 Ejercicio 3 – Par o impar

Pide un número al usuario.

Si el número es par, imprime:
El número es par

Si no, imprime:
El número es impar

💡 Pista: piensa en el residuo.

a = int(input("Digite un numero"))

if a % 2:
    print("El numero es impar")

else:
    print("El numero es par")"""


"""🟡 Ejercicio 4 – Comparar dos números

Pide dos números al usuario.

Si el primero es mayor que el segundo, imprime:
El primer número es mayor

Si no, imprime:
El segundo número es mayor o igual

a = int(input("Digite el primer numero"))
b = int(input("Digite el segundo numero"))

if a > b:
    print("El primer número es mayor")

else:
    print("El segundo número es mayor o igual")"""





"""🟡 Ejercicio 1 – Positivo, negativo o cero

Pide un número al usuario.

Si es mayor que 0 → Positivo

Si es menor que 0 → Negativo

Si es 0 → Es cero

💡 Aquí sí necesitas elif.

a = int(input("Digite un numero"))

if a > 0:
    print("Pisitivo")

elif a < 0:
    print("Negativo")

else:
    print("Es cero")"""


"""🟡 Ejercicio 2 – Nota simple

Pide una nota (0 a 5).

Si es mayor o igual a 4 → Excelente

Si es mayor o igual a 3 → Aprobado

Si es menor a 3 → Reprobado

a = int(input("Digite la nota de 0 a 5: "))

if a >= 4:
    print("Excelente")
elif a >= 3:
    print("Aprobado")

else:
    print("Reprobado")"""



"""🟡 Ejercicio 3 – Edad

Pide la edad al usuario.

Si es menor de 18 → Menor de edad

Si es 18 o más → Mayor de edad

(Sí, este se puede sin elif, es para afianzar).

a = int(input("Digite su edad"))

if a < 18:
    print("Menos de edad")
else:
    print("Mayor de edad")"""


"""🟡 Ejercicio de repetición – Condicional simple

Pide un número al usuario.

Si el número es mayor que 100, imprime:
Número grande

Si es entre 1 y 100, imprime:
Número normal

Si es 0 o negativo, imprime:
Número no válido


a = int(input("Digite un numero"))

if a > 100:
    print("Numero Grande")

elif a < 100 and a > 1:
    print("Numero normal")

else:
    print("Numero no valido")"""


"""🟡 Ejercicio 1 – Número válido

Pide un número al usuario.

Si el número es mayor que 0 y menor que 100, imprime:
Número válido

Si no, imprime:
Número fuera de rango

💡 Pista: hay dos condiciones en el if.

a = int(input("Digite un numero"))

if a > 0 and a < 100:
     print("Numero valido")

else:
     print("Fuera de rango")"""


"""🟡 Ejercicio 2 – Acceso por edad

Pide la edad al usuario.

Si la edad es mayor o igual a 18 y menor o igual a 65, imprime:
Acceso permitido

Si no, imprime:
Acceso denegado

a = int(input("Digite su edad"))

if a >=18 and a <= 65:
    print("Acceso permitido")

else:
    print("Acceso denegado")"""


"""🟡 Ejercicio 3 (opcional) – Usuario simple

Pide un nombre al usuario.

Si el nombre es "admin", imprime:
Bienvenido administrador

Si no, imprime:
Usuario común

a = input("Digite su nombre")
if a == "admin":
    print("Bienvenido administrador")

else:
    print("Usuario comun")"""


"""🟡 Ejercicios para HOY (haz 1 o 2, no todos)
🟡 Ejercicio 1 – Clasificación de número

Pide un número al usuario.

Si el número es positivo y par, imprime:
Positivo y par

Si es positivo e impar, imprime:
Positivo e impar

Si es 0, imprime:
Es cero

Si es negativo, imprime:
Número negativo

💡 Pista: el orden de las condiciones importa.

""" 

"""a = int(input("Digite un numero"))

if a == 0:
    print("Es cero")

elif a < 0:
    print("Número negativo")

elif a % 2 != 0:
    print("Es positivo e impar")

elif a % 2 == 0:
    print("Es positivo y par")"""

#### PENDIENTEEEEEEEEEEEEEEEEEEE

"""🟡 Ejercicio 2 – Nota con rangos

Pide una nota de 0 a 5.

Si es 5, imprime: Excelente

Si es entre 4 y menor que 5, imprime: Muy bien

Si es entre 3 y menor que 4, imprime: Aprobado

Si es menor que 3, imprime: Reprobado


a = int(input("Digite su nota"))"""

"""🟡 Ejercicio 3 (opcional) – Login simple

Pide un usuario y una contraseña.

Si el usuario es "admin" y la contraseña es "1234" →
Acceso concedido

Si no →
Acceso denegado"""


##############################################24 de enero#################################################


"""Pide un número al usuario.

Si el número es mayor que 50, imprime:
Mayor que 50

Si es entre 1 y 50, imprime:
Entre 1 y 50

Si es 0 o negativo, imprime:
Número no válido

a = int(input("Digite un numero"))

if a > 50:
    print("Mayor que 50")

elif a > 1:
    print("Entre 1 y 50")

else:
    print("Número no válido")"""

##############################################25 de enero#################################################
"""Pide un número al usuario.

Si el número es divisible entre 3, imprime:
Divisible entre 3

Si no, imprime:
No divisible entre 3"""

a = int(input("Digite un numero"))

if a % 3 ==0:
    print("Es divisible por 3")

else:
    print("No es divisible por 3")

