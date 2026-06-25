# Para escribir "W"
with open("mensaje.txt", "w") as archivo:
    archivo.write("Hola mundo")

print(archivo)

#Para agregar "a" y no borrar lo que ya esta

with open("datos.txt", "a") as archivo:
    archivo.write("Estoy aprendiendo Python")