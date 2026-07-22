# 1. Tenemos una lista con los minutos de tus últimas sesiones desordenadas
minutos_estudiados = [45, 120, 30, 60, 15]

# 2. La función Len() CUENTA cuaántos elementos hay en total dentro de la lista
cantidad_sesiones = len(minutos_estudiados)

# 3. El método .sort() ORDENA los elementos de menos a mayor automáticameente
minutos_estudiados.sort()

# 4. Mostramos el análisis en la terminal
print("--- 📊 ANALIZADOR Y ORDENADOR DE HISTORIAL ---")
print(f"Número total de sesiones registradas: {cantidad_sesiones}")
print(f"Tus tiempos ordenados de menor a mayor: {minutos_estudiados}")

# 💡 Truco extra: Si quieres ordenarlos de MAYOR a MENOR, usas reverse=True
minutos_estudiados.sort(reverse=True)
print(f"Tus tiempos ordenados de mayor a menor: {minutos_estudiados}")



