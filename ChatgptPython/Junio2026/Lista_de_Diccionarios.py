"""✅
Ejercicio 1

Observa:

estudiantes = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Carlos", "edad": 22},
    {"nombre": "María", "edad": 19}
]

Imprime solamente:

Ana
Carlos
María

estudiantes =[
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19}

]

for estudiante in estudiantes:

 print(estudiante["nombre"])

"""





"""
✅Ejercicio 2

Con la misma lista:

estudiantes = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Carlos", "edad": 22},
    {"nombre": "María", "edad": 19}
]

Imprime:

Ana tiene 20 años
Carlos tiene 22 años
María tiene 19 años



estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19}
]

for estudiante in estudiantes:

 print(f"{estudiante['nombre']} tiene {estudiante['edad']} años")"""
"""


Ejercicio 3 ✅⭐

Calcula el promedio de edades.

Resultado:

Promedio: 20.33


estudiantes =[
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"maria","edad":19}
]

# estudinates diccionario
# estudiante lista

sumar = 0

for estudiante in estudiantes:

    sumar += estudiante["edad"]

promedio = sumar / len(estudiantes)

print("Promedio:",promedio)"""


"""
✅Ejercicio 4 ⭐⭐

Encuentra cuál es la edad mayor de la lista.

Resultado:

Edad mayor: 22


estudiantes =[
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19}
]


mayor = 0
for estudiante in estudiantes:
 if estudiante["edad"] > mayor:
  
  mayor = estudiante["edad"]  #AL FINAL SE ESCRIBRE DE ESTA FORMA PARA QUE EL VALOR MAYOR SE QUEDEDE GUARDADO EN LA VARIABLE MAYOR

print(mayor)"""
     


"""
✅Ejercicio 5 ⭐⭐⭐

Agrega un nuevo estudiante:

{"nombre":"Yule","edad":28}

a la lista y luego imprime toda la lista.



estudiantes =[
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19}

]

estudiantes.append({"nombre":"Yule","edad":28})

print(estudiantes)"""



"""
✅Ejercicio 6

Encuentra cuál es la edad mayor de la lista.

Resultado:

Edad mayor: 22


estudiantes =[
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19}
]

menor = estudiantes[0]["edad"]
for estudiante in estudiantes:

    if estudiante["edad"] < menor:
    
     menor = estudiante["edad"]

print("Edad menor", menor)


 """
#EJERCICIO 7✅
"""Encuentra el nombre del estudiante con la edad mayor.
Salida
Carlos tiene la edad mayor: 22


estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19}
]

mayor_edad = estudiantes[0]["edad"]
nombre_mayor = estudiantes[0]["nombre"]

#nombre_mayor = 0
for estudiante in estudiantes:
    if estudiante["edad"] > mayor_edad:
        mayor_edad = estudiante["edad"]
        nombre_mayor = estudiante["nombre"]
 
print(f"{nombre_mayor} tiene la edad mayor: {mayor_edad}")"""

#EJERCICIO 8✅
"""
Dada la lista:
estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19},
    {"nombre":"Yule","edad":28}
]

Haz un programa que muestre:

Cantidad de estudiantes: 4

Promedio de edades: 22.25

Edad mayor: 28
Nombre: Yule

Edad menor: 19
Nombre: Maria
"""
# ✅Cantidad de estudiantes: 4
"""
estudiantes =[
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19},
    {"nombre":"Yule","edad":28}
]
for estudiante in estudiantes:
  
 contar = len(estudiantes)
 
print(contar)
"""

#✅Promedio de edades: 22.25
"""
estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19},
    {"nombre":"Yule","edad":28}
]



sumar = 0
for estudiante in estudiantes:
    

    sumar += estudiante["edad"]

    promedio = sumar/len(estudiantes)

print(f"Promedio de edades:{promedio}")"""

#Edad mayor: 28✅
#Nombre: Yule
"""
estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19},
    {"nombre":"Yule","edad":28}
]

edad_mayor = estudiantes[0]["edad"]
nombre = estudiantes[0]["nombre"]

for estudiante in estudiantes:

    if estudiante["edad"] > edad_mayor:

        edad_mayor = estudiante["edad"]
        nombre = estudiante["nombre"]

print(f"Edad mayor:{edad_mayor}")
print(f"nombre:{nombre}")
"""



#Edad menor: 19✅
#Nombre: Maria

"""estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19},
    {"nombre":"Yule","edad":28}
]

edad_menor = estudiantes[0]["edad"]
nombre = estudiantes[0]["nombre"]

for estudiante in estudiantes:
    if estudiante["edad"] < edad_menor:

        edad_menor = estudiante["edad"]
        nombre = estudiante["nombre"]

print(f"Edad menor:{edad_menor}")
print(f"nombre:{nombre}")"""









