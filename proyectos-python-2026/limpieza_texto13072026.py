# 1. Simulamos que el usuario escribe con errores comunes
# Pusimos espacios vacíos a los lados a propósito y desorden de mayúsculas
tema_sucio = "    lEctUrA crItIca     "

# 2. Aplicamos los superpoderes de los métodos de string
# .strip() elimina los espacios vacíos invisibles de los extremos
tema_sin_espacios = tema_sucio.strip()


# .title() convierte la primera letra de cada palabra en mayúscula
tema_formateado = tema_sin_espacios.title()

# .upper() convierte absolutamente todo a mayúsculas sostenidas
tema_grito =tema_sin_espacios.upper()


# 3. Mostramos los resultados en la termianl para comparar

print("--- 🧼 LAVANDERÍA DIGITAL DE TEXTOS ---")
print(f"Texto original: '{tema_sucio}' (Tiene espacios y desorden)")
print(f"Texto limpio:   '{tema_sin_espacios}' (Sin espacios a los lados)")
print(f"Formato Título: '{tema_formateado}' (Perfecto para reportes)")
print(f"Formato Grito:  '{tema_grito}' (Excelente para alertas)")
