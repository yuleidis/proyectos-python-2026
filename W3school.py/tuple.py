#Forma alternativa para modificar una tupla

x = ("apple", "banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(x)

print(type(x))
#Forma alternativa para agregar algo en la tupla


thistuple = ("apple", "banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)


# Al crear una tupla con 1 solo elemento se le coloca la coma ejemplo
y = ("orange",)


#Para eliminar una tupla tambien se hace e mismo procedimiento

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
y = tuple(thistuple)

print(thistuple)