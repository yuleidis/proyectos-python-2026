# 1. El usuario ingresa un dato con múltiples errores de formato
entrada_sucia = "  pYtHoN  "

# 2. ENCADENAMIENTO DE MÉTODOS: Se ejecutan de izquierda a derecha en una sola línea
# Primero elimina espacios (.strip) y de inmediato convierte a mayúsculas (.upper)
entrada_impecable = entrada_sucia.strip().upper()

# 3. También podemos limpiar y validar de inmediato
# Limpia los espacios invisibles y verifica de una vez si lo que quedó son solo letras
es_letra_pura = entrada_sucia.strip().isalpha()

# 4. Mostramos el análisis en la terminal
print("--- 🔗 CADENA DE MONTAJE DE TEXTOS ---")
print(f"Original: '{entrada_sucia}'")
print(f"Limpio y en Mayúsculas: '{entrada_impecable}'")
print(f"¿Al quitar espacios contiene solo letras?: {es_letra_pura}")

