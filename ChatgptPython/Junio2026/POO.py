"""
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        

libro1 = Libro("Python basico","Juan")

print(libro1.titulo)
print(libro1.autor)
"""

#Ejercicio
"""

class Persona:

 def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

 def mostrar_datos(self):
     print("Nombre:", self.nombre)
     print("Edad:", self.edad)


persona1 = Persona("Yule",28)

persona1.mostrar_datos()"""

#Ejercicio
"""

class Estudiante:

    def __init__(self,nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
        print("Carrera:", self.carrera)

estudiante1 = Estudiante("Yule", 28, "Ingenieria de Sistema")

estudiante1.mostrar_informacion() """

#Ejercicio
"""class Mascota:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

mascota1 = Mascota("Firulai",5)

print(mascota1.edad)

mascota1.edad = 6

print(mascota1.edad)"""

class Cuenta:
    
    def __init__(self, titular, saldo):

        self.titular = titular
        self.saldo = saldo
        

    def depositar(self, monto):        

        self.saldo += monto
       
         
cuenta1 = Cuenta("Yule",100)

cuenta1.depositar(50)

print(cuenta1.saldo)


#150


        
        
        
        



        
        