#Metodo get
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.get("model")
"""
# Este keys()método devolverá una lista con todas las claves del diccionario.
"""
x = thisdict.keys()

print(x)

x = thisdict.values()

print(x)"""


#Agregar un nuevo elemento
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car.keys()

print(car)

car["color"] = "while"

print(car)
"""

# Este update()método actualizará el diccionario con los elementos del argumento proporcionado.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({"year": 2020})

print(thisdict)


