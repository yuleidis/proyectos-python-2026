#Ejercicio 1
"""
estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19},
    {"nombre":"Yule","edad":28}
]

def contar_estudiantes(estudiantes):

    return len(estudiantes)

resultado = contar_estudiantes(estudiantes)

print(resultado)"""
#Ejercicio 2

"""
estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19},
    {"nombre":"Yule","edad":28}
]


def obtener_edad_mayor(estudiantes):
        
        edad_mayor = estudiantes[0]["edad"]

        for estudiante in estudiantes:
                
            if estudiante["edad"] > edad_mayor: 
           
                edad_mayor = estudiante["edad"]

        return edad_mayor

                       
resultado = obtener_edad_mayor(estudiantes)

print(resultado)
"""

#Ejercicio 3
"""
estudiantes = [
    {"nombre":"Ana","edad":20},
    {"nombre":"Carlos","edad":22},
    {"nombre":"Maria","edad":19},
    {"nombre":"Yule","edad":28}
]

def obtener_nombre_mayor(estudiantes):

    nombre_mayor = estudiantes[0]["nombre"]

    edad_mayor = estudiantes[0]["edad"]

    for estudiante in estudiantes:

        if estudiante["edad"] > edad_mayor:

            edad_mayor = estudiante["edad"]

            nombre_mayor = estudiante["nombre"]

    return nombre_mayor

resultado = obtener_nombre_mayor(estudiantes)

print(resultado)"""



#ejercicio 1

"""def estudiante():

    return "Ana", 20

nombre, edad = estudiante()

print(nombre)
print(edad)"""

#ejercicio 2

"""def mostrar_ciudad(ciudad="Valledupar"):
    print(f"De que ciudad eres: {ciudad}")

mostrar_ciudad("Bogota")"""
#Ejercicio 3

"""def multiplicar(a,b):
    return a* b

def mostrar_resultado(a,b):
    resultado = multiplicar(a,b)
    print(resultado)

mostrar_resultado(3,4)"""

#ejercicio

"""nombre = "Yule"

def mostrar():

    nombre = "Ana"

    print(nombre)

mostrar()
print(nombre)"""












