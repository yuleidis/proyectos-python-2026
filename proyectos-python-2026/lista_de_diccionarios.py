# 1. Creamos una lista vacía para guardar nuestras sesiones

historial_estudio = []

# 2.  Creamos dos sesiones individuales (cada una es un diccionario)

sesion1 = {
    "tema": "Diccionarios",
    "minutos": 40,
    "materia": "Python"
}

sesion2 ={
    "tema": "Lectura critica",
    "minutos": 50,
    "materia": "Saber Pro"
}

# 3. Guardamos los diccionarios dentro de la lista usando .append()
historial_estudio.append(sesion1)
historial_estudio.append(sesion2)

# 4. Usamos un bucle 'for' para recorrer la lista y mostrar el reporte completo
print("--- 📊 REPORTE DE SESIONES AVANZADO ---")
for sesion in historial_estudio:
    #Entramos a las etiquetas de cada diccionario dentro de la lista
    print(f"• Estudié {sesion['tema']} ({sesion['materia']}) por {sesion['minutos']} minutos.")