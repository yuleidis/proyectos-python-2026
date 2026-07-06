#06/JULIO/2026

#1. Creamos una función que CALCULA Y DEVOLVERÁ el total
# En lugar de imprimir, usa 'return' para entregar el valor en la mano

def calcular_horas_reales(minutos_totales):
    #convertimos los minutos a horas dividiendo por 60
    horas_calculadas = minutos_totales/60
    return horas_calculadas #Entrega el resultado final

# 2. Simulamos que extraemos estos minutos de tu archivo JSON
mis_minutos_de_hoy = 150

#3. Llamamos a la función y GUARDAMOS su retorno en una variable nueva
horas_de_estudio = calcular_horas_reales(mis_minutos_de_hoy)


# 4. Mostramos el resultado limpio en la pantalla
print("--- ⏱️ CONVERSOR AUTOMÁTICO DE TIEMPO ---")
print(f"Llevas acumulados {mis_minutos_de_hoy} minutos.")
print(f"Eso equivale exactamente a: {horas_de_estudio} horas de estudio real.")