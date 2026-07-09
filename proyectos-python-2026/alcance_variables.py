# 1. Variable GLOBAL (Vive afuera de las funciones, en todo el archivo)
meta_horas_semanal = 15

def registrar_estudio_dia(horas_hoy):
    # 2. variable LOCAL (Solo exite aquí adentro de la función)
    mensaje_exito = "¡Horas procesadas con éxito!"

    # La función puede LEER la variable global de afuera sin problema
    horas_restantes = meta_horas_semanal - horas_hoy

    print (mensaje_exito)
    return horas_restantes

# 3. Probamos el funcionamiento en la terminal
print("--- 🔬 EXPERIMENTO DE ALCANCE DE VARIABLES ---")
restante = registrar_estudio_dia(3)
print(f"Te falta {restante} horas para cumplir tu meta de {meta_horas_semanal}")
