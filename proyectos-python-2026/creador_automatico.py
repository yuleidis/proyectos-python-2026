"""
Vamos a hacer que tu programa sea inteligente. Si el archivo progreso.txt no existe, Python no solo te va a avisar, sino que lo va a crear automáticamente desde cero para que no tengas que hacerlo tú a mano.Aprenderás a usar el modo w (write / escribir) combinado con tu estructura de control de errores.
"""
minutos_totales = 0

try:
    #intentamos leer el archivo normalmente
    with open("progreso.txt", "r", encoding ="utf-8") as archivo:
     for linea in archivo:
        datos = linea.strip().split(",")
        minutos_totales = minutos_totales + int(datos[1])
    print(f"📊 Reporte Actualizado: Llevas {minutos_totales} minutos.")

except FileNotFoundError:
   #Si no existe, python entra aquí y lo crea automáticamente
   print("⚠️ El archivo no existía. ¡Pero no te preocupes, lo estoy creando ahora mismo!")

   #Abrimos con 'w' para crear el archivo en blanco
   with open("progreso.txt", "w", encoding ="utf=-8") as archivo:
    pass #'pass' significa dejarlo vacío por ahora

   print("✨ ¡Archivo 'progreso.txt' creado con éxito! Ya puedes usar tu programa.")    