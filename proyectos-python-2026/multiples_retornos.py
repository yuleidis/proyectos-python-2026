# 1. Función que procesa los datos y devuelve DOS resultados a la vez

def analizar_rendimiento(minutos_p, minutos_s):
    # Calculamos los porcentajes(asumiendo una meta diaria de 120 min por materia)
    meta = 120
    porcentaje_python = (minutos_p / meta) * 100
    porcentaje_saber = (minutos_s / meta) * 100

    # Retornamos ambos valores separados por una coma
    return porcentaje_python, porcentaje_saber

#2. Datos simulados de tu historial de estudio de ayer
mis_minutos_python = 90
mis_minutos_saber_pro = 60


# 3. Al llamar la función, usamos DOS variable para atrapar los DOS retornos
porc_py, porc_sp = analizar_rendimiento(mis_minutos_python, mis_minutos_saber_pro)


# 4. Mostramos el reporte analítico en la terminal
print("--- 📈 PANEL METRICOS DE RENDIMIENTO ---")
print(f"💻 Progreso Meta Python: {porc_py:.1f}% ")
print(f"📝 Progreso Meta Saber Pro: {porc_sp:.1f}%")
