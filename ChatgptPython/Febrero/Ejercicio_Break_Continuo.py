####📅 Día 08 de febrero

"""Tema: break – romper un ciclo
⏱️ Tiempo: 15–20 minutos

🟡✅ Ejercicio 1 – Detener el ciclo (bajo)

Usa while para imprimir números del 1 al 10.

👉 Cuando el número sea 5, el ciclo debe detenerse.

Salida esperada:

1
2
3
4


💡 Pista:

if numero == 5:
    break

numero = 1

while numero < 11:

    if numero == 5:
     break
    print(numero)
    numero += 1
"""
    
       
"""✅🟡 Ejercicio 2 – Buscar un número (bajo–medio)

Pide al usuario un número.

Luego usa for para recorrer del 1 al 10:

Si el número aparece, imprime:

Número encontrado


Y rompe el ciclo

💡 Pista: range(1, 11)


a = int(input("Digite un numero"))


for i in range(1,11):


    if  i == a:

     print("Numero encontrado")

     break"""

"""✅🟡 Ejercicio 3 – break con listas (medio)

Usa esta lista:

frutas = ["manzana", "pera", "uva", "banano", "mango"]


Recorre la lista con for.

👉 Cuando encuentres "banano", imprime:

Banano encontrado


👉 Detén el ciclo.

frutas = ["manzana", "pera", "uva", "banano", "mango"]


for i in frutas:
  
  if i == "banano":
        print("Banano encontrado")
        break"""
    

###📅 Día 09 de febrero

"""Tema: continue – saltar una vuelta
⏱️ Tiempo: 15–20 minutos

✅🟡 Ejercicio 1 – Saltar un número 

Usa for para imprimir los números del 1 al 10.

👉 No debe imprimirse el número 5.

💡 Pista:

if numero == 5:
    continue


for i in range(1,11):


    if i == 5:
        continue
    print(i)"""


"""✅🟡 Ejercicio 2 – Saltar pares 

Usa for del 1 al 10.

👉 Imprime solo los números impares.

💡 Pista:

if numero % 2 == 0:
    continue

for i in range(1,11):

    if i % 2 == 0:
        continue
    print(i)"""



"""✅🟡 Ejercicio 3 – continue con texto 

Usa esta lista:

nombres = ["Ana", "", "Luis", "", "Carlos"]


Recorre la lista y:

Si el nombre está vacío ("") → sáltalo

Si tiene nombre → imprímelo

Salida esperada:

Ana
Luis
Carlos

nombres = ["Ana", "", "Luis", "", "Carlos"]

for i in nombres:

    if i == "":
     continue
    print(i)"""