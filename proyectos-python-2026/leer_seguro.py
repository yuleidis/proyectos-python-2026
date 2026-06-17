minutos_totales = 0

# 1. Usamos 'try' (intentar) para proteger el código

try:
    with open("progreso.txt","r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            minutos_de_la_linea = int(datos[1])
            minutos_totales = minutos_totales + minutos_de_la_linea

    print(f"Reporte actualizado: Llevas un total de {minutos_totales} minutos estudiados.")

# 2. Si el archivo no existe, Python entra aquí en vez de romperse
except FileNotFoundError:
 print("¡Ojo! El archivo 'progreso.txt' aun no existe.")
 print("Crea una sesion primero con tu otro archivo para que se genere automáticamente. ")