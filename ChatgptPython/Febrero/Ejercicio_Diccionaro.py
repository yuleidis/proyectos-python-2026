

""" Día 1 – Diccionarios (introducción)
✅ 🟡 Ejercicio 1 – Crear un diccionario (bajo)

Crea un diccionario llamado persona con estos datos:

nombre

edad

ciudad

Luego imprime el diccionario completo.


persona = {"nombre":"Yuleidis","edad":28,"ciudad":"valledupar"}
print(persona)
"""


"""✅🟡 Ejercicio 2 – Acceder a un valor (bajo)

Usando el diccionario persona, imprime solo el nombre.

💡 Pista: usa la clave.

persona = {"nombre":"Yuleidis","edad":28,"ciudad":"valledupar"}

print(persona.get["nombre"])"""


"""🟡✅ Ejercicio 3 – Modificar un valor (bajo)

Cambia la edad de la persona por otro número.

Luego imprime el diccionario actualizado.

 Tiempo sugerido día 1: 10–15 minutos


persona = {"nombre":"Yuleidis","edad":28,"ciudad":"valledupar"}

persona["edad"] = 26

print(persona)"""



""" Día 2 – Diccionarios (uso básico)

🟡 ✅Ejercicio 1 – Agregar una nueva clave (bajo)

Agrega al diccionario persona una nueva clave:

"profesion"

Luego imprime el diccionario.


persona = {"nombre":"Yuleidis","edad":28,"ciudad":"valledupar"}

persona["profesion"]="Ingeniera de sistama y trader"

print(persona)"""


"""🟡 ✅Ejercicio 2 – Recorrer diccionario (bajo–medio)

Usa for para imprimir:

cada clave

luego cada valor

💡 Pista: for clave in diccionario:

persona = {"nombre":"Yuleidis","edad":28,"ciudad":"valledupar"}

for clave in persona:

    print(persona[clave])"""



"""✅🟡 Ejercicio 3 – Mostrar clave y valor (medio)

Usa for para imprimir así:

nombre : Yuleidis
edad : 25
ciudad : Cali

💡 Pista: diccionario.items()

⏱️ Tiempo sugerido día 2: 15–20 minutos

persona = {"nombre":"Yuleidis","edad":28,"ciudad":"valledupar"}

for clave, valor  in persona.items():


    print(clave,":",valor)"""

""" Día 3 – Diccionarios + if

🟡✅ Ejercicio 1 – Buscar una clave (bajo–medio)

Pregunta al usuario una clave (por ejemplo: nombre).

Si la clave existe en el diccionario, imprime:

La clave existe


Si no existe, imprime:

La clave no existe


💡 Pista: in

persona = {"nombre":"Yuleidis","edad":28,"ciudad":"valledupar"}


a = (input("Digite la clave"))

if a in persona:

    print("La clave  existe")

else:
    print("La clave no existe")"""


"""✅ 🟡 Ejercicio 2 – Mostrar valor si existe (medio)

Si la clave existe:

imprime su valor

Si no existe:

imprime "No encontrada



a = input(("Digite la clave"))

persona={"nombre":"Yuleidis", "Edad":28,"Ciudad":"Valledupar"}

if a in persona:

    print(persona[a])

else:
    print("No existe la clave")"""



"""🟡✅ Ejercicio 3 – Mini reto  

Crea un diccionario con 3 productos y sus precios.

Recorre el diccionario e imprime:

Producto: precio


persona = {"queso":20000,"arroz":40000,"aceite":10000}


for clave, valor in persona.items():

    

    print(clave,":",valor)"""




###🟡 Día 4 – Diccionarios (bajo → medio)
"""🟡 ✅Ejercicio 1 – Mostrar valor si existe 

Usa este diccionario:

persona = {
    "nombre": "Yuleidis",
    "edad": 28,
    "ciudad": "Valledupar"
}


Pide al usuario una clave.

Si la clave existe, imprime su valor

Si no existe, imprime:

Clave no encontrada


💡 Pista: if clave in diccionario


persona = {
    "nombre": "Yuleidis",
    "edad": 28,
    "ciudad": "Valledupar"
}

a = (input("Digite una clave"))

if a in persona:
  
  print(persona[a])

else:
  print("Clave no encontrada")"""



"""🧠✅ Mini reto
Problema

Tienes este diccionario:

productos = {
    "arroz": 2500,
    "leche": 3000,
    "huevos": 5000,
    "pan": 1500
}

Debes hacer un programa que:

1️⃣ Recorra el diccionario.

2️⃣ Si el precio es mayor a 2500, imprima:

Producto caro: nombre_del_producto


3️⃣ Si el precio es menor o igual a 2500, imprima:

Producto económico: nombre_del_producto

🎯 Ejemplo de salida esperada

Algo como:

Producto económico: arroz
Producto caro: leche
Producto caro: huevos
Producto económico: pan

productos = {
    "arroz": 2500,
    "leche": 3000,
    "huevos": 5000,
    "pan": 1500
}

for clave, valor in productos.items():

    if valor > 2500:
        print("produto caro:", clave)

    elif valor <= 2500:

        print("Producto económico:", clave)"""


"""🟡✅ Ejercicio 2 – Diccionario de notas 

Crea un diccionario con 3 materias y sus notas (números).

Ejemplo:

notas = {
    "matematicas": 4,
    "espanol": 3,
    "ingles": 5
}


Recorre el diccionario e imprime:

materia : nota

notas = {
    "matematicas": 4,
    "espanol": 3,
    "ingles": 5
}


for clave, valor in notas.items():

    print(clave,":",valor)"""


"""🟡✅ Ejercicio 3 – Mini reto 

Usa el mismo diccionario notas.

Imprime solo las materias que tengan nota mayor o igual a 4.

💡 Pista: for + if


notas = {
    "matematicas": 4,
    "espanol": 3,
    "ingles": 5
}

for clave, valor in notas.items():

    if valor >= 4:
     print(clave,":", valor )"""



###🟡 Día 05 – Diccionarios 
"""🟡✅ Ejercicio 1 – Diccionario + input (bajo)

Crea un diccionario con estos datos:

producto = {
    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 2
}
Imprime:

Producto: arroz
Precio: 2500
Cantidad: 2


💡 Pista: acceder por clave.

producto = {
    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 2
}

for clave,valor in producto.items():



    print(clave,":",valor)"""


"""🟡✅ Ejercicio 2 – Calcular total 

Usando el mismo diccionario producto:

Calcula el total a pagar:

total = precio * cantidad


Luego imprime:

Total a pagar: X


💡 Pista: los valores son números, no texto.

producto = {
    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 2
}

total = producto["precio"] * producto["cantidad"] 
    
print("total a pagar:", total)"""


"""🟡✅ Ejercicio 3 – Recorrer diccionario 

Usa for para imprimir:

clave : valor


Ejemplo:

nombre : arroz
precio : 2500
cantidad : 2


💡 Pista: .items()


producto = {

    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 2
    
}

for clave, valor in producto.items():


    print(clave,":",valor)"""


"""🟡✅ Ejercicio 4 – Mini reto 

Pide al usuario una clave del diccionario producto.

Si la clave existe, imprime su valor

Si no existe, imprime:

Dato no encontrado


💡 Pista: in


a = input("digite una clave")

producto = {

    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 2
    
}

if a in producto:

    print("Su valor es ", producto[a])

else:
        print("Dato no encontrado")"""



##📅 Día 06 de febrero

"""Tema: Diccionarios + cálculos + if
⏱️ Tiempo: 20 minutos

🟡 ✅Ejercicio 1 – Calcular total (bajo)

Usa este diccionario:

producto = {
    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 2
}


👉 Calcula el total (precio * cantidad)
👉 Imprime:

Producto: arroz
Total a pagar: 5000


💡 Pista:
total = producto["precio"] * producto["cantidad"]


producto = {
    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 2
}


for clave in producto.values():
 
 total = producto["precio"] * producto["cantidad"]

 print("producto:",producto["nombre"],"\n","Total a pagar",total)"""




"""🟡  ✅Ejercicio 2 – Cambiar cantidad con input 

Pide al usuario una nueva cantidad

Actualiza el valor "cantidad" del diccionario

Vuelve a calcular el total

Imprime el nuevo total

💡 Pista:

input() devuelve texto → usa int()



producto = {
    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 2
}

a = int(input("Digite una nueva cantidad"))

producto["cantidad"] = a

total = producto["cantidad"] * producto["precio"]

print("El total es:", total)"""


"""🟡✅ Ejercicio 3 – Validar existencia de clave 

Pregunta al usuario qué dato quiere ver (nombre, precio o cantidad).

Si la clave existe → imprime su valor

Si no existe → imprime:

Dato no disponible


💡 Pista:

if clave in producto:

producto = {
    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 2
}

a = input("Digite el dato que desea ver (nombre, precio o cantidad): ")




if a in producto:

        print(producto[a])

else:
    print("Dato no disponible")"""