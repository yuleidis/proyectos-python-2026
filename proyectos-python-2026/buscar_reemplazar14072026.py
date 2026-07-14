# 1. Tenemos un texto con un error ortográfico o un formato viejo
oracion_estudio = "Hoy estudié el tema de Programasion en la mañana"

# 2. Usamos .replace() para corregir la palabra mal escrita
# El primer dato es lo que quieres buscar, y el segundo es el reemplazo correcto
oracion_corregida = oracion_estudio.replace("Programasion","Programación")


# 3. Usamos 'in' para verificar si una palabra clave exite en el texto
# Esto nos devuelve un valor Booleano (True o False)
tiene_saber_pro = "Saber pro" in oracion_corregida
tiene_python = "Programación" in oracion_corregida

# 4. Mostramos los resultado analícos en la termimnal
print("--- 🔍 BUSCADOR Y REEMPLAZADOR DE TEXTOS ---")
print(f"Texto corregido: {oracion_corregida}")
print(f"¿La sesión es de Saber Pro?: {tiene_saber_pro}")
print(f"¿La sesión es de Python?:    {tiene_python}")