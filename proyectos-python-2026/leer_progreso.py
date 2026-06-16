#Creamos una variable para acumular los minutos totales
minutos_totales = 0

# 2. Abrimos el archivo en modo 'r' (leer/lectura)

with open("progreso.txt", "r", encoding="utf-8") as archivo:
    # El bucle 'for' lee el archivo linea por linea
    for linea in archivo:
        #Quitamos los espacios vacios y separamos el texto por coma
        datos = linea.strip().split(",")

        #El segunto dato (posicion 1) son los minutos. Los convertimos a numero entero(int)
        minutos_de_la_linea = int(datos[1])

        minutos_totales =  minutos_totales + minutos_de_la_linea


# 3. Mostramos el resultado final en la pantalla

print(f"Reporte Actualizado: Llevas un total de {minutos_totales} minutos estudiados.")