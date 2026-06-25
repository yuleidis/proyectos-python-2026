#Para agregar un elemento a un conjunto, utilice el add() método.
thisset = { "apple","banana","cherry"}

thisset.add("orange")

print(thisset)

# Para agregar elementos de otro conjunto al conjunto actual, utilice el update() método.
#El objeto en el update()método no tiene por qué ser un conjunto, puede ser cualquier objeto iterable (tuplas, listas, diccionarios, etc.).

thisset = {"apple","banana","cherry"}
tropical = {"pineable","mango", "papaya"}

thisset.update(tropical)

print(thisset)


#Para eliminar un elemento de un conjunto, utilice el método remove()o el discard()método.

thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)



"""
También puedes usar este pop()método para eliminar un elemento, pero eliminará uno al azar, por lo que no puedes estar seguro de qué elemento se eliminará.

El valor de retorno del pop()método es el elemento elimina

"""

thisset = {"apple","banana","cherry"}

x = thisset.pop()

print(x)

print(thisset)

#para eliminar todos los elementos de un conjunto se escoje CLEAR


#Este union()método devuelve un nuevo conjunto con todos los elementos de ambos conjuntos.


set1 = {"a","b","c"}
set2 = 1,2,3

set3 = set1.union(set2)

print(set3)

#Puedes usar el |operador en lugar del union()método y obtendrás el mismo resultado.
"""
Nota: Este  | operador solo permite unir conjuntos con otros conjuntos, y no con otros tipos de datos como se puede hacer con el  union()método.
"""

set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1|set2

print(set3)

#Este intersection()método devolverá un nuevo conjunto que solo contendrá los elementos presentes en ambos conjuntos.
#Puedes usar el &operador en lugar del método y obtendrás el mismo resultado. intersection()

"""Nota: Este & operador solo permite unir conjuntos con otros conjuntos, y no con otros tipos de datos como se puede hacer con el intersection()método."""

set1 = {"apple","banana","cherry"}
set2 = {"google","Microsoft","apple"}

set3 = set1.intersection(set2)

print(set3)

"""
frozensetes una versión inmutable de un conjunto.

Al igual que los conjuntos, contiene elementos únicos, no ordenados e inmutables.

A diferencia de los conjuntos, no se pueden agregar ni eliminar elementos de un conjunto congelado.

"""

"""Ser inmutable significa que no se pueden agregar ni eliminar elementos. Sin embargo, los conjuntos congelados admiten todas las operaciones que no modifican los conjuntos."""

x = frozenset({"apple","banana","cherry"})
print(x)
print(type(x))


