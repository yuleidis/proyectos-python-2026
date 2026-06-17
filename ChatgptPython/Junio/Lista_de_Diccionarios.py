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
#EJERCICIO 7
"""Encuentra el nombre del estudiante con la edad mayor.

estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19}
]"""



