"""
✅Ejercicio A

Dado:

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}

Imprime solamente las claves usando un for.

Resultado esperado:

nombre
edad
ciudad


persona = {

    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogota"
}

for clave in persona:

    print(clave)"""



"""✅Ejercicio B

Dado:

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}

Imprime solamente los valores.

Resultado:

Ana
25
Bogotá

persona ={
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogota"
}

for valor in persona.values():
    print(valor)"""



"""✅Ejercicio C ⭐

Dado:

notas = {
    "Matemáticas": 4.5,
    "Programación": 5.0,
    "Bases de Datos": 4.2
}

Calcula el promedio de las notas usando un for.

Resultado:

Promedio: 4.56

notas = {

    "Matematicas": 4.5,
    "Programación": 5.0,
    "Bases de Datos": 4.2
}

lista =[]

for valor in notas.values():
  

  lista.append(valor)
  entre = len(lista)
  sumar = sum(lista)

  resultado = sumar / entre
  #sumar = sum(valor)
print("Promedio:",resultado)"""


## otra opcion de resolver el ejercicio C

notas = {

    "matematicas": 4.5,
    "programacion": 5.0,
    "base de datos": 4.2
}

suma = 0

for nota in notas.values():

    #tambien lo puedo hacer de esta forma SUMA = SUMA + NOTA
    suma += nota

    promedio = suma / len(notas)

print("El promedio es:", promedio)



