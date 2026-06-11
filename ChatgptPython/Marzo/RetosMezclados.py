"""✅🟡 RETO 1 – Total de compra
🔹 Enunciado

Tienes este diccionario:

producto = {
    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 3
}

👉 Crea una función que:

reciba el diccionario
retorne el total (precio * cantidad)

Luego:

guarda el resultado
imprime:
Total a pagar: X 

producto = {
    "nombre": "arroz",
    "precio": 2500,
    "cantidad": 3
}

def calcular_total(prod):

    return prod["precio"] * prod["cantidad"]

resultado = calcular_total(producto)
print(f"El total a pagar es: {resultado}")"""







"""✅🟡 RETO 2 – Productos caros
🔹 Enunciado
productos = {
    "arroz": 2500,
    "leche": 3000,
    "huevos": 5000,
    "pan": 1500
}

👉 Crea una función que:

reciba el diccionario
recorra los productos
retorne una lista con los productos mayores a 2500

Luego imprime la lista. 

fdsfasdfadsfassssssssssssssssssssss
productos = {
    "arroz": 2500,
    "leche": 3000,
    "huevos": 5000,
    "pan": 1500
}

def productos_caros(prod):

    lista = []

    for nombre, precio in prod.items():

        if precio > 2500:
            lista.append(nombre)

    return lista


resultado = productos_caros(productos)

print(resultado)"""


"""✅🟡 RETO 3 – Contar productos
🔹 Enunciado

Usando el mismo diccionario:

👉 Crea una función que:

reciba el diccionario
retorne cuántos productos hay

productos = {
    "arroz": 2500,
    "leche": 3000,
    "huevos": 5000,
    "pan": 1500
}

def contar(prod):
        return len(prod)

resultado = contar(productos)

print(resultado)"""


"""RETO 3 (nuevo) – Promedio de precios
🔹 Enunciado

Usa este diccionario:

productos = {
    "arroz": 2500,
    "leche": 3000,
    "huevos": 5000,
    "pan": 1500
}
👉 Crea una función que:

reciba el diccionario
calcule el promedio de los precios
retorne ese promedio

Pistas (no solución)
necesitas sumar los precios
necesitas contar cuántos hay
promedio = suma / cantidad

Aquí mezclas:

diccionario
recorrido
acumulador
return
productos = {
    "arroz": 2500,
    "leche": 3000,
    "huevos": 5000,
    "pan": 1500
}

def promedio(prod):
   
   
   lista = []
   
   for precio in productos.values():
     lista.append(precio)


     sumar = sum(lista)
     cantidad = len(lista)
     pro = sumar / cantidad
   return pro
     
resultado = promedio(productos)
print(resultado)"""

"""✅🟡 RETO 4 – Buscar producto
🔹 Enunciado

👉 Crea una función que:

reciba:
diccionario
nombre del producto
retorne:
el precio si existe
"No encontrado" si no

"""
"""productos = {
    "arroz": 2500,
    "leche": 3000,
    "huevos": 5000,
    "pan": 1500
}

digite = input("Digite un producto")

def nom(pro):

 if digite in pro:
  
  return pro[digite]
 
 else:
  return "No encontrado"

resultado = nom(productos)
print(resultado)

#✅🟡 RETO 1 – Mostrar productos

productos = [
    {"nombre": "arroz", "precio": 2500},
    {"nombre": "leche", "precio": 3000},
    {"nombre": "pan", "precio": 1500}
]

for producto in productos:

    print(producto["nombre"])
"""

"""✅🟢 EJERCICIO 1 — Crear y mostrar

Crea un diccionario llamado estudiante con:

nombre
edad
carrera

Luego imprime todo el diccionario.


estudiante = {
"nombre":"yule",
"edad":28,
"carrera":"Ingenieria de sistema"
}
print(estudiante)"""



"""✅🟢 EJERCICIO 2 — Mostrar un valor específico

Con este diccionario:

Imprime solamente:

el nombre
la raza

💡 Usa las claves.


mascota = {
    "nombre": "Firulais",
    "edad": 5,
    "raza": "Labrador"
}

print(mascota["nombre"],"\n",mascota["raza"])"""


"""✅🟢 EJERCICIO 3 — Modificar valores

Tienes este diccionario:

Cambia:

el precio a 1800
el stock a 5

producto = {
    "nombre": "Laptop",
    "precio": 2000,
    "stock": 10
}

producto["precio"] = 1800
producto["stock"] = 5

print(producto)"""

"""✅🟡 EJERCICIO 4 — Agregar elementos

Crea este diccionario:

auto = {
    "marca": "Toyota",
    "modelo": "Corolla"
}

Agrega:

"año": 2022
"color": "rojo


auto = {

    "marca": "Toyota",
    "modelo": "corolla"
}


auto["año"] = 2022
auto["color"]="rojo"

print(auto)"""


"""✅🟡 EJERCICIO 5 — Eliminar elementos

Con este diccionario:

usuario = {
    "nombre": "Carlos",
    "edad": 30,
    "correo": "carlos@gmail.com"
}

Elimina la clave "correo" y luego imprime el diccionario.


usuario = {

        "nombre": "Carlos",
        "edad": 30,
        "correo": "carlos@gmail.com"

}

#del usuario["correo"]

eliminar_clave = usuario.pop("correo")   

print(usuario, eliminar_clave)"""

"""🟠 EJERCICIO 6 — Recorrer diccionarios

Con:

frutas = {
    "manzana": 3,
    "pera": 5,
    "uva": 10
}

Usa un for para imprimir:

manzana -> 3
pera -> 5
uva -> 10

frutas = {

    "manzana": 3,
    "pera": 5,
    "uva": 10
}

for frutas, clave in frutas.items():

    print(frutas, "->",clave)"""



"""🔴 EJERCICIO 7 — Mini reto

Haz un programa que:

Cree un diccionario con información de una película.
Debe tener:
nombre
género
año
protagonista
Luego imprime algo así:
La película Titanic es de género Romance

pelicula = {

    "Nombre": "En busca de la felicidad",
    "Género": "Drama",
    "año": 2006,
    "Protagonista": "Will Smith"

}

print(f"La película {pelicula['Nombre']} es de género {pelicula['Género']}")"""






