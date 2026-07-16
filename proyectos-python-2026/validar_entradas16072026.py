# 1. Simulamos dos datos que ingresa el usuario por la terminal
entrada_minutos = "45"
entrada_tema = "Diccionarios"
entrada_con_error = "45min"

# 2. .isdigit() verifica si el texto contiene ÚNICAMENTE números
es_numero_valido = entrada_minutos.isdigit()
es_error_digito = entrada_con_error.isdigit()

# 3. .isalpha() verifica si el texto contiene Únicamente letras sin espacios ni números)
es_texto_valido = entrada_tema.isalpha()

# 4. Mostramos el análisis en la terminal
print("--- 🛡️ ESCUDO DE VALIDACIÓN DE DATOS ---")
print(f"¿'{entrada_minutos}' es un número válido para operar?: {es_numero_valido}")
print(f"¿'{entrada_con_error}' es un número válido para operar?: {es_error_digito}")
print(f"¿'{entrada_tema}' contiene solo letras?: {es_texto_valido}")

# 5. Ejemplo de cómo se usa en un control real
print("\n🤖 Simulando validación en tu App:")
if entrada_minutos.isdigit():
    minutos_finales = int(entrada_minutos)
    print(f"✅ Éxito: Se transformó a número ({minutos_finales} min) de forma segura.")
else:
    print("❌ Error: Los minutos deben contener solo números enteros.")

