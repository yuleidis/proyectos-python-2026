# 1. le pedimos los datos al usuario desde la consola
tema_estudiados = input("¿Qué temas estudiaste hoy?:")
minutos = input("¿Cuántos minutos le dedicaste?")

# 2.Abrimos (o creamos) un archivo de texto llamado progreso.txt
#usamos a (append) para que escriba al final del archivo sin borrar lo anterior

with open("progreso.txt", "a", encoding="utf-8") as archivo:
  #Escribimos los datos separados por coma y saltamos de linea (\n)

  archivo.write(f"{tema_estudiados},{minutos} \n" )

print("Tu sesión ha sido guardad con exito en progreso.txt")