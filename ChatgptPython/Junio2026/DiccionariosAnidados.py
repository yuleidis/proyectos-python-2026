"""

✅Ejercicio 1

Observa este diccionario:

estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "direccion": {
        "ciudad": "Bogotá",
        "barrio": "Centro"
    }
}
Pregunta

Imprime solamente:

Bogotá


##Desarrollo

estudiante ={
    "nombre": "Ana",
    "edad": 22,
    "direccion":{
    "ciudad": "Bogota",
    "barrio": "centro"

    }
}

print(estudiante["direccion"]["ciudad"])

"""


"""
✅Ejercicio 2

Con el mismo diccionario imprime:

Centro

#DESARROLLO
estudiante = {

    "nombre": "Ana",
    "edad": 22,
    "direccion":{
     "ciudad": "Bogota",
     "barrio": "centro"
    }
}

print(estudiante["direccion"]["barrio"])"""


"""
✅Ejercicio 3

Modifica la ciudad para que sea:

Medellín

Luego imprime todo el diccionario.



estudiante ={

    "nombre": "Ana",
    "edad": 22,
    "direccion":{
        "ciudad": "bogota",
        "barrio": "centro"
    }

}

estudiante["direccion"]["ciudad"] = "Medellin"

print(estudiante)

"""




"""

✅Ejercicio 4 ⭐

Crea este diccionario:

empresa = {
    "nombre": "TechSoft",
    "empleado": {
        "nombre": "Carlos",
        "cargo": "Desarrollador",
        "salario": 3000
    }
}

Imprime:

Carlos trabaja como Desarrollador

usando los datos del diccionario.



empresa = {
    "nombre": "Techsoft",
    "empleado":{

        "nombre":"Carlos",
        "cargo":"Desarrollador",
        "salario": 3000
    }
}

print(empresa["empleado"]["nombre"],"trabaja como",empresa["empleado"]["cargo"])
"""

"""
✅Ejercicio 5 ⭐⭐

Crea un diccionario que almacene:

persona = {
    "nombre": "Yule",
    "estudios": {
        "carrera": "Ingeniería de Sistemas",
        "semestre": 10
    }
}

Y muestra:

Yule estudia Ingeniería de Sistemas y está en el semestre 10


persona = {
    "nombre": "Yule",
    "Estudio": {
        "carrera": "Ingenieria de Sistema",
        "Semestre": 10
    }
}
print(persona["nombre"],"Estudia",persona["Estudio"]["carrera"], "y esta en el semestre", persona["Estudio"]["Semestre"])
"""
