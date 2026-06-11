#COMO SE CREA UNA CLASE
class Myclase:

 x = 5


#COMO SE CREA UN OBJETO

p1 = Myclase()

print(p1.x) # Para eliminar el objeto se usa DEL, ejemplo: del p1

#Múltiples objetos

p1 = Myclase()
p2 = Myclase()

print(p1.x)
print(p2.x)



"""
Instrucciones
Dentro del editor, complete los siguientes pasos:
Crea una clase llamadaDog
Agregue un _init_método con parámetros namey age, y almacénelos como propiedades usandoself
Agrega un método barkque imprima el nombre del perro seguido de "¡dice Guau!".
Crea un objeto d1de la Dogclase con el nombre "Buddy" y edad 3
Llama al barkmétodo end1
"""




# Create the Dog class
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.name = age
  def bark(self):
      return f"{self.name} dice ¡Guau!"


# Create an object
d1 = Dog("Buddy", 3)

# Call the bark method
print(d1.bark())


class vehiculo:

  def __init__(self,marca, color):
    self.marca = marca
    self.color = color

  def bark(self):
    return f"{self.marca}, {self.color}, brum brum"
  

p1 = vehiculo("chevrole","red")
print(p1.bark())


