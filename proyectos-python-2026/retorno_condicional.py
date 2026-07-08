# 1. Función que evalúa la meta y devuelve True o False
def verificar_meta_cumplida(minutos_estudiados, metas_del_dia):
    if minutos_estudiados >= metas_del_dia:
        return True
    
    else:
        return False
    

# 2. Datos reales de tu bitácora de estudio

mis_minutos_de_hoy = 130
meta_establecida = 120 # Tu meta ideal de 2 horas

# 3. Usamos el retorno de la función directamente como la condición 'if'

print("--- 🎯 VERIFICADOR DE METAS DIARIAS ---")

if verificar_meta_cumplida(mis_minutos_de_hoy, meta_establecida):

    print(" 🎉 ¡Felicidades! Cumpliste tu meta de estudio de hoy.")
    print("Tu cerebro y tu portafolio de GitHub te lo agradecen.")

else:
    print("⚠️ No alcanzaste la meta establecida para hoy.")
    print("No te preocupes, mañana compensamos el tiempo restante.")
