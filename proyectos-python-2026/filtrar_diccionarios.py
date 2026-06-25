# 1. Tu lista con tres diccionario de estudio
historial_estudio = [
    {"tema": "Diccionarios", "minutos": 40, "materia": "Python"},
    {"tema": "Lectura Critica", "minutos": 50, "materia": "Saber Pro"},
    {"tema": "Listas Avanzadas", "minutos": 30, "materia": "Python"}
]

# 2. Creamos la variable acumuladora para la suma

minutos_totales = 0

# 3. Recorremos la lista y sumamos los valores de la etiqueta 'minutos'

print("--- ⏱️ PROCESANDO MINUTOS DEL HISTORIAL ---")

for sesion in historial_estudio:
    #Sumamos el valor numérico que está dentro de la clave 'minutos'

    minutos_totales = minutos_totales + sesion["minutos"]

    #Mostramos el desglose en pantalla
    print(f"Sumamados {sesion['minutos']} min de {sesion['tema']}")

# 4. Mostramos el resultado final de la operación
print(f"\n📊 Resultado Final: Has estudiado un total de {minutos_totales} minutos.")
