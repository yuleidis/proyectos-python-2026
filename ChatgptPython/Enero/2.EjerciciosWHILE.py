""" 🟡 EJERCICIO 1
Haz un programa que imprima los números del 1 al 3 usando while. """

""" numero = 0

while numero <= 2:

    numero += 1

    print(numero) """

"""🟡 Ejercicio 2

Haz un programa que imprima la palabra “Python” 2 veces usando while.

letra = 0

while letra < 2 :

    letra += 1

    print("Python")"""

"""🟡 Ejercicio 3

Pide un número al usuario y réstale 1 hasta llegar a 1.
Ejemplo si escribe 3, debe mostrar:
3
2
1


digitar = int(input("Digite un numero"))

while digitar > 0:
    print(digitar)
    digitar -= 1"""

    


"""🟡 Ejercicio 4

Haz un programa que sume solo dos números que el usuario escriba, sin ciclo.
(Este es para que practiques la suma básica)

digite1 = int(input("Digite un primer numero"))
digite2 = int(input("Digite un segundo numero"))

sumas = digite1 + digite2

print(sumas)"""


"""🟡 Ejercicio 5

Crea una variable llamada nombre con tu nombre y luego imprímela.

nombre = "Yuleidis Sanchez"

print(nombre)"""

"""🟡 Ejercicio 6

Crea un programa que imprima:
1
2
pero sin pedir datos al usuario y sin ciclo, solo print.

print(1,"\n",2)
"""

"""🟡 Ejercicio 7

Haz un programa que pida un solo número y lo imprima.

numero = int(input("Digite un numero"))

print(numero)"""


"""🟡 Ejercicio 8

Haz un programa con while que imprima la palabra “OK” 3 veces.

letra = 0

while letra < 3:
    print("Ok")
    letra += 1"""


"""🟡 Ejercicio 9

Crea dos variables:

a = 5
b = 2


Y muestra el resultado de multiplicarlas.

a = 5
b = 2

r = a * b
print(r)"""


"""🟡 Ejercicio 10

Haz un while que imprima los números del 5 al 3 (sin pedir datos al usuario)

Salida esperada:

5
4
3

a = 5

while a >= 3:
    print(a)
    a -= 1"""


"""🟡 Ejercicio 11

Crea un programa que imprima el siguiente texto exactamente igual:

Me gusta Python
Voy paso a paso

print("Me gusta Python")
print("Voy paso a paso")"""


"""🟡 Ejercicio 14

Haz un programa que imprima tu frase favorita del momento 1 vez, por ejemplo:

Voy a lograrlo
(la que tú quieras, solo 1 print)


print("VOY A LOGRARLOOOOOOOOOOOOOOOO....")"""

"""🟡 Ejercicio 15

Crea un programa que imprima tu ciudad (sin pedir datos al usuario).

print("Valldupar")"""

"""🟡 Ejercicio 16

Pídele al usuario su nombre y muéstralo con un mensaje así:

Tu nombre es: Ana

(el nombre que la persona escriba debe aparecer en el mensaje)

nombre= "Yuleidis"

print("Tu nombre es", nombre)"""

"""🟡 Ejercicio 17

Usa while para imprimir los números:

1
2

(sin pedir datos al usuario)

nu = 1

while nu < 3:
    print(nu)
    nu += 1"""

"""🟡 Ejercicio 18

Haz un programa que calcule e imprima el resultado de:

8 + 2


(sin input, solo la operación y print)

a = 8
b = 2

sumarr = a + b
print(sumarr)"""

######################################################EJERCICIO BAJO-MEDIO WHILE###########################33333

"""🟡 Ejercicio 1 – Contador de práctica 

Haz un programa que:

Cree una variable minutos = 0

Use while para sumar 5 minutos por vuelta

Se detenga cuando llegue a 15 minutos

Imprima cada avance así:

Has estudiado: 5 minutos
Has estudiado: 10 minutos
Has estudiado: 15 minutos

🧠 Pistas (por si las necesitas cuando lo hagas):

El while debe continuar mientras minutos < 15

En cada vuelta haces minutos += 5

Luego imprimes el mensaje


minutos = 0

while minutos < 15:
    minutos += 5
    print(f"Has estudiado:{minutos}minutos")"""


"""🟡 Ejercicio 2 – Comparación básica con input

Haz un programa que:

Pida 2 números al usuario

Guarde cada uno en variables

Imprima cuál es mayor con este formato:

El mayor es: 9


(No necesitas ciclo para este)

nu1 = 0
nu2 = 0

nu1 = int(input("Digite el primer numero"))
nu2 = int(input("Didite el segundo numero"))

resultado = nu1 
resultado = nu2



print("El mayor es", resultado)

"""


"""🟡 Ejercicio 3 – While con texto

Haz un programa que:

Cree una variable veces = 1

Use while para imprimir esta frase 3 veces:

Estoy retomando Python


Pero debe enumerar así:

1 Estoy retomando Python
2 Estoy retomando Python
3 Estoy retomando Python

veces = 1

while veces <= 3:

    print(veces,"Estoy retomando python")
    veces += 1"""


"""🟡 Ejercicio 4 – Suma acumulativa

Haz un programa que:

Cree dos variables: a = 6 y b = 4

Cree una tercera variable resultado que sume a + b

Imprima:

La suma es: 10

a = 6 
b = 4

resultado = a + b

print("La suma es:", resultado)"""



"""🟡 Ejercicio 19

Haz un programa que imprima los números del 1 al 5 usando while.

a = 1

while a <= 5:
    print(a)
    a += 1"""



"""🟡 Ejercicio 20

Crea 3 variables:

a = 2
b = 3
c = 4


Multiplica las 3 y guarda el resultado en una variable r, luego imprime:

Resultado: 24
a = 2
b = 3
c = 4
r = 0

r = a * b * c

print("Resultado:",r)"""



"""🟡 Ejercicio 21

Haz un while que imprima “Sigo practicando” 4 veces, numerado así:

1 Sigo practicando
2 Sigo practicando
3 Sigo practicando
4 Sigo practicando

a = 1

while a <= 4:
    print(a,"Sigo practicando")
    a += 1"""


"""🟡 Ejercicio 22

Pide un número al usuario y haz que el programa imprima:

Tu número + 10 es: X


Ejemplo si digitan 5, debe mostrar:

Tu número + 10 es: 15

a = 10

n = int(input("Dijete un numero"))

while a != n:
  resultado = a + n
  print(n ,"+", a, "es:",resultado)
  break"""


"""🟡 Ejercicio 23

Crea una variable energia = 3
y usa while para restarle 1 hasta llegar a 0, imprimiendo cada paso:

Salida esperada:

Energía actual: 3
Energía actual: 2
Energía actual: 1
Energía actual: 0

energia = 3

while energia >= 0:
    
    print("Energia acual:",energia)
    energia -= 1"""

#######################################PENDIENTE POR DESARROLLAR###########################################################3

"""🔥 WHILE – INTENSIDAD ALTA (Nivel controlado)

Estos ejercicios ya trabajan lógica real, no solo repetición.
Hazlos uno por uno, no todos de golpe.

🔴 Ejercicio A – Validador de contraseña (alto)

Haz un programa que:

Pida una contraseña al usuario

Mientras la contraseña no sea "python2026", siga pidiéndola

Cuente cuántos intentos hizo el usuario

Al final imprima:

Acceso concedido
Intentos: X
"""

intentos = 0
clave = ""

while clave != "python2026":
    clave = input("Digite la contraseña: ")
    intentos += 1

print("Acceso concedido")
print("Intentos:", intentos)

 
 

"""🔴 Ejercicio B – Suma con condición (alto)

Haz un programa que:

Pida números al usuario

Vaya sumándolos

Se detenga cuando la suma sea mayor o igual a 100

Imprima:

La suma total fue: X"""

"""🔴 Ejercicio C – Menú simple (alto)

Crea un programa que:

Muestre este menú repetidamente:

1. Saludar
2. Mostrar hora (solo texto, no hora real)
3. Salir


Si el usuario elige:

1 → imprime "Hola Yuleidis"

2 → imprime "Son las 10:00"

3 → termina el programa con "Fin del programa"

💡 Usa while para mantener el menú activo."""

"""🔴 Ejercicio D – Contador inteligente (alto)

Haz un programa que:

Empiece con numero = 1

Imprima solo los números pares

Se detenga cuando llegue a 20

Salida esperada (ejemplo parcial):

2
4
6
...
20"""

#########################################B#########################################################



 

    
